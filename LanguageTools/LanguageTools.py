import os
import unittest
import logging
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin

#
# LanguageTools
#

class LanguageTools(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "Language Tools"
    self.parent.categories = ["Utilities"]
    self.parent.dependencies = []
    self.parent.contributors = ["Andras Lasso (PerkLab)"]
    self.parent.helpText = """
This module can build translation files and install them locally. It is useful for creating and testing translations.
See more information in the <a href="https://github.com/Slicer/SlicerLanguagePacks">extension's documentation</a>.
"""
    self.parent.acknowledgementText = """
Developed of this module was partially funded by <a href="https://chanzuckerberg.com/eoss/proposals/3d-slicer-in-my-language-internationalization-and-usability-improvements/">CZI EOSS grant</a>.
"""

#
# LanguageToolsWidget
#

class LanguageToolsWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent=None):
    """
    Called when the user opens the module the first time and the widget is initialized.
    """
    ScriptedLoadableModuleWidget.__init__(self, parent)
    VTKObservationMixin.__init__(self)  # needed for parameter node observation
    self.logic = None
    self._parameterNode = None
    self._updatingGUIFromParameterNode = False

  def setup(self):
    """
    Called when the user opens the module the first time and the widget is initialized.
    """
    ScriptedLoadableModuleWidget.setup(self)

    # Load widget from .ui file (created by Qt Designer).
    # Additional widgets can be instantiated manually and added to self.layout.
    uiWidget = slicer.util.loadUI(self.resourcePath('UI/LanguageTools.ui'))
    self.layout.addWidget(uiWidget)
    self.ui = slicer.util.childWidgetVariables(uiWidget)

    # Set scene in MRML widgets. Make sure that in Qt designer the top-level qMRMLWidget's
    # "mrmlSceneChanged(vtkMRMLScene*)" signal in is connected to each MRML widget's.
    # "setMRMLScene(vtkMRMLScene*)" slot.
    uiWidget.setMRMLScene(slicer.mrmlScene)

    # Create logic class. Logic implements all computations that should be possible to run
    # in batch mode, without a graphical user interface.
    self.logic = LanguageToolsLogic()
    self.logic.logCallback = self.log

    # Connections

    # These connections ensure that whenever user changes some settings on the GUI, that is saved in the MRML scene
    # (in the selected parameter node).
    self.ui.githubSourceRadioButton.connect("toggled(bool)", lambda toggled, source="github": self.setTranslationSource(source, toggled))
    self.ui.crowdinTsFolderRadioButton.connect("toggled(bool)", lambda toggled, source="crowdinTsFolder": self.setTranslationSource(source, toggled))
    self.ui.crowdinZipFileRadioButton.connect("toggled(bool)", lambda toggled, source="crowdinZipFile": self.setTranslationSource(source, toggled))

    # Buttons
    self.ui.updateButton.connect('clicked(bool)', self.onUpdateButton)
    self.ui.restartButton.connect('clicked(bool)', self.onRestartButton)

    # Make sure parameter node is initialized (needed for module reload)
    self.updateGUIFromSettings()

  def cleanup(self):
    """
    Called when the application closes and the module widget is destroyed.
    """
    pass

  def enter(self):
    """
    Called each time the user opens this module.
    """
    pass

  def exit(self):
    """
    Called each time the user opens a different module.
    """
    pass

  def setTranslationSource(self, translationSource, toggled=True):
    if not toggled:
      # ignore when radiobutton is untoggled, we just process the toggled event
      return
    self.ui.gitRepositoryLabel.enabled = (translationSource == "github")
    self.ui.githubRepositoryEdit.enabled = (translationSource == "github")
    self.ui.crowdinTsFolderLabel.enabled = (translationSource == "crowdinTsFolder")
    self.ui.crowdinTsFolderPathLineEdit.enabled = (translationSource == "crowdinTsFolder")
    self.ui.latestTsFileOnlyLabel.enabled = (translationSource == "crowdinTsFolder")
    self.ui.latestTsFileOnlyCheckBox.enabled = (translationSource == "crowdinTsFolder")
    self.ui.crowdinZipFileLabel.enabled = (translationSource == "crowdinZipFile")
    self.ui.crowdinZipFilePathLineEdit.enabled = (translationSource == "crowdinZipFile")


  def updateGUIFromSettings(self):
    settings = slicer.app.userSettings()
    try:
      settings.beginGroup("Internationalization/LanguageTools")
      translationSource = settings.value("TranslationSource", "crowdinTsFolder")
      self.ui.crowdinTsFolderRadioButton.checked = (translationSource == "crowdinTsFolder")
      self.ui.crowdinTsFolderPathLineEdit.enabled = (translationSource == "crowdinTsFolder")
      self.ui.crowdinZipFileRadioButton.checked = (translationSource == "crowdinZipFile")
      self.ui.githubSourceRadioButton.checked = (translationSource == "github")
      self.setTranslationSource(translationSource)
      self.ui.githubRepositoryEdit.text = settings.value("GitRepository", "https://github.com/Slicer/SlicerLanguageTranslations")
      self.ui.slicerVersionEdit.text = settings.value("SlicerVersion", "master")
      self.ui.crowdinTsFolderPathLineEdit.currentPath = settings.value("CrowdinTsFolderPath", "")
      self.ui.latestTsFileOnlyCheckBox.checked = settings.value("UseLatestTsFile", True)
      self.ui.crowdinZipFilePathLineEdit.currentPath = settings.value("CrowdinZipFilePath", "")
      self.ui.lreleasePathLineEdit.currentPath = settings.value("LreleaseFilePath", "")
    finally:
      settings.endGroup()

    if not os.path.exists(self.ui.lreleasePathLineEdit.currentPath):
      self.ui.settingsCollapsibleButton.collapsed = False

  def updateSettingsFromGUI(self):
    settings = slicer.app.userSettings()
    try:
      settings.beginGroup("Internationalization/LanguageTools")
      if self.ui.crowdinTsFolderRadioButton:
        source = "crowdinTsFolder"
      elif self.ui.crowdinZipFileRadioButton:
        source = "crowdinZipFile"
      else:
        source = "github"
      settings.setValue("TranslationSource", source)
      settings.setValue("GithubRepository", self.ui.githubRepositoryEdit.text)
      settings.setValue("SlicerVersion", self.ui.slicerVersionEdit.text)
      settings.setValue("CrowdinTsFolderPath", self.ui.crowdinTsFolderPathLineEdit.currentPath)
      settings.setValue("UseLatestTsFile", self.ui.latestTsFileOnlyCheckBox.checked)
      settings.setValue("CrowdinZipFilePath", self.ui.crowdinZipFilePathLineEdit.currentPath)
      settings.setValue("LreleaseFilePath", self.ui.lreleasePathLineEdit.currentPath)
    finally:
      settings.endGroup()

    self.ui.crowdinTsFolderPathLineEdit.addCurrentPathToHistory()
    self.ui.crowdinZipFilePathLineEdit.addCurrentPathToHistory()

  def onUpdateButton(self):
    """
    Run processing when user clicks "Apply" button.
    """
    with slicer.util.tryWithErrorDisplay("Update failed.", waitCursor=True):
      self.ui.statusTextEdit.clear()
      self.updateSettingsFromGUI()

      self.logic.slicerVersion = self.ui.slicerVersionEdit.text
      self.logic.lreleasePath = self.ui.lreleasePathLineEdit.currentPath

      self.logic.removeTemporaryFolder()

      if self.ui.crowdinTsFolderRadioButton.checked:
        self.logic.copyTsFilesFromFolder(self.ui.crowdinTsFolderPathLineEdit.currentPath, self.ui.latestTsFileOnlyCheckBox.checked)
      elif self.ui.crowdinZipFileRadioButton.checked:
        self.logic.unpackTsFilesFromCrowdinZipFile(self.ui.crowdinZipFilePathLineEdit.currentPath)
      else:
        self.logic.downloadTsFilesFromGithub(self.ui.githubRepositoryEdit.text)

      self.logic.convertTsFilesToQmFiles()
      self.logic.installQmFiles()

  def onRestartButton(self):
    slicer.util.restart()

  def log(self, message):
    self.ui.statusTextEdit.append(message)

#
# LanguageToolsLogic
#

class LanguageToolsLogic(ScriptedLoadableModuleLogic):
  """This class should implement all the actual
  computation done by your module.  The interface
  should be such that other python code can import
  this class and make use of the functionality without
  requiring an instance of the Widget.
  Uses ScriptedLoadableModuleLogic base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self):
    """
    Called when the logic class is instantiated. Can be used for initializing member variables.
    """
    ScriptedLoadableModuleLogic.__init__(self)
    self.slicerVersion = "master"
    self.lreleasePath = None
    self._temporaryFolder = None
    self.translationFilesFolder = None
    self.crowdinProjectName = "Slicer"
    self.gitRepositoryName = "SlicerLanguageTranslations"
    self.gitBranchName = "main"  # we store translations for all Slicer versions in the main branch
    self.logCallback = None

  def log(self, message):
    if self.logCallback:
      self.logCallback(message)

  def temporaryFolder(self):
    if not self._temporaryFolder:
      self._temporaryFolder = slicer.util.tempDirectory()
    return self._temporaryFolder

  def removeTemporaryFolder(self):
    if not self._temporaryFolder:
      return
    import shutil
    shutil.rmtree(self._temporaryFolder)
    self._temporaryFolder = None
    self.translationFilesFolder = None

  def copyTsFilesFromFolder(self, tsFolder, latestTsFileOnly):
    """Extract .ts files from a zip file downloaded from Crowdin.
    This method requires a temporary folder that does not contain previous downloaded or extracted files.
    """

    tempFolder = self.temporaryFolder()
    self.translationFilesFolder = tempFolder

    import glob
    tsFiles = sorted(glob.glob(f"{tsFolder}/*.ts"), key=os.path.getmtime)

    if latestTsFileOnly:
      tsFiles = [tsFiles[-1]]
      self.log(f"Use translation file: {tsFiles[0]}")

    import shutil
    import xml.etree.cElementTree as ET
    for file in tsFiles:
      tree = ET.ElementTree(file=file)
      locale = tree.getroot().attrib['language']  # such as 'zh-CN'
      baseName = os.path.basename(file).split('_')[0]
      shutil.copy(file, f"{self.translationFilesFolder}/{baseName}_{locale}.ts")

  def unpackTsFilesFromCrowdinZipFile(self, crowdinZipFile):
    """Extract .ts files from a zip file downloaded from Crowdin.
    This method requires a temporary folder that does not contain previous downloaded or extracted files.
    """

    tempFolder = self.temporaryFolder()

    # Unzip file
    slicer.util.extractArchive(crowdinZipFile, tempFolder)

    # /temp/[Slicer.SlicerLanguageTranslations] main/translated/[Slicer.SlicerLanguageTranslations] main/master"
    self.translationFilesFolder = f'{tempFolder}/[{self.crowdinProjectName}.{self.gitRepositoryName}] {self.gitBranchName}/translated/[{self.crowdinProjectName}.{self.gitRepositoryName}] {self.gitBranchName}/{self.slicerVersion}'

  def downloadTsFilesFromGithub(self, githubRepositoryUrl):
    """Download .ts files from a Github repository.
    This method requires a temporary folder that does not contain previous downloaded or extracted files.
    """

    tempFolder = self.temporaryFolder()

    # Download file
    import SampleData
    dataLogic = SampleData.SampleDataLogic()
    translationZipFilePath = dataLogic.downloadFile(f'{githubRepositoryUrl}/archive/refs/heads/{self.gitBranchName}.zip', self.temporaryFolder(), 'CrowdinTranslations.zip')

    # Unzip file
    slicer.util.extractArchive(translationZipFilePath, tempFolder)

    # /temp.../SlicerLanguageTranslations-main/translated/master
    self.translationFilesFolder = f'{tempFolder}/{self.gitRepositoryName}-{self.gitBranchName}/translated/{self.slicerVersion}'

  def convertTsFilesToQmFiles(self):
    if not self.translationFilesFolder:
      raise ValueError("Translation files folder is not specified.")

    if (not self.lreleasePath) or (not os.path.exists(self.lreleasePath)):
      raise ValueError("lrelease tool path is not specified.")

    logging.info(f"Processing translation files in folder {self.translationFilesFolder}")
    import glob
    tsFiles = sorted(glob.glob(f"{self.translationFilesFolder}/*.ts"), key=os.path.getmtime)

    for file in tsFiles:
        lreleaseProcess = slicer.util.launchConsoleProcess([self.lreleasePath, str(file)])
        slicer.util.logProcessOutput(lreleaseProcess)

  def installQmFiles(self):
    if not self.translationFilesFolder:
      raise ValueError("Translation files folder is not specified.")

    import shutil
    from pathlib import Path
    tsFiles = Path(self.translationFilesFolder).glob('*.qm')

    applicationTranslationFolder = slicer.app.translationFolders()[0]

    # Make sure the translations folder exists
    os.makedirs(applicationTranslationFolder, exist_ok=True)

    numberOfInstalledFiles = 0
    for file in tsFiles:
      logging.debug(f"Installing translation file: {file} in {applicationTranslationFolder}")
      shutil.copy(file, applicationTranslationFolder)
      numberOfInstalledFiles += 1

    if numberOfInstalledFiles == 0:
      raise ValueError(f"No translation (qm) files were found at {self.translationFilesFolder}")
    
    self.log(f"Update successfully completed.\nInstalled {numberOfInstalledFiles} translation files in {applicationTranslationFolder}.")

#
# LanguageToolsTest
#

class LanguageToolsTest(ScriptedLoadableModuleTest):
  """
  This is the test case for your scripted module.
  Uses ScriptedLoadableModuleTest base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setUp(self):
    """ Do whatever is needed to reset the state - typically a scene clear will be enough.
    """
    slicer.mrmlScene.Clear()

  def runTest(self):
    """Run as few or as many tests as needed here.
    """
    self.setUp()
    self.test_LanguageTools1()

  def test_LanguageTools1(self):
    """ Ideally you should have several levels of tests.  At the lowest level
    tests should exercise the functionality of the logic with different inputs
    (both valid and invalid).  At higher levels your tests should emulate the
    way the user would interact with your code and confirm that it still works
    the way you intended.
    One of the most important features of the tests is that it should alert other
    developers when their changes will have an impact on the behavior of your
    module.  For example, if a developer removes a feature that you depend on,
    your test should break so they know that the feature is needed.
    """

    self.delayDisplay("Starting the test")

    logic = LanguageToolsLogic()

    import shutil
    logic.lreleasePath = shutil.which('lrelease')

    # Fallback for local testing on Windows in the install tree
    if not logic.lreleasePath:
      logic.lreleasePath = "c:/Qt/5.15.0/msvc2019_64/bin/lrelease.exe"

    logic.downloadTsFilesFromGithub("https://github.com/Slicer/SlicerLanguageTranslations")
    logic.convertTsFilesToQmFiles()
    logic.installQmFiles()

    logic.removeTemporaryFolder()

    self.delayDisplay('Test passed')
