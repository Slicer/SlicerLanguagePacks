
# Guide for Slicer module developers

These instructions are for Slicer module developers (in Slicer core or in Slicer extensions) who want to make their modules to be translatable.

## Preparing .ui files for translation

By default, most string and stringlist properties that appear in .ui files are made available for translation. This is usually the correct behavior, but in some cases properties contain strings that must not be translated (and therefore must not appear in translation source (.ts) files).

Developers **must mark properties that should not be translated in Qt designer** by unchecking the `Translatable` option. The only exception is that when the property value is not set (but left at default value, typically it means that is left empty), in which case translatable option should be left unset.

These properties must be marked as non-translatable:
- In node selector widgets, such as qMRMLNodeComboBox, qMRMLCheckableNodeComboBox, qMRMLSubjectHierarchyTreeView, qMRMLTreeView:
  - `nodeTypes`
  - `hideChildNodeTypes`
  - `interactionNodeSingletonTag` (if not the default "Singleton" value)
  - `sceneModelType`
  - `levelFilter`
- In MRML widgets (qMRML...Widget) that support quantities, such as qMRMLRangeWidget or qMRMLCoordinatesWidget:
  - `quantity`
- In widgets that save data into application settings, such as ctkPathLineEdit, qMRMLSegmentationFileExportWidget, qMRMLSegmentEditorWidget:
  - `settingKey`
  - `defaultTerminologyEntrySettingsKey`
- In widgets that save data into node or subject hierarchy attributes, such as qMRMLSubjectHierarchyComboBox, SubjectHierarchyTreeView:
  - `includeItemAttributeNamesFilter`
  - `excludeItemAttributeNamesFilter`
  - `includeNodeAttributeNamesFilter`
  - `excludeNodeAttributeNamesFilter`
- In slice view widgets, such as qMRMLSliceControllerWidget and qMRMLSliceWidget:
  - `sliceViewName`
  - `sliceOrientation`
- In qMRMLSegmentationConversionParametersWidget:
  - `targetRepresentationName`
- In qSlicerMouseModeToolBar:
  - `defaultPlaceClassName`

![](Docs/DesignerMarkAsNonTranslatable.png)

## Preparing Qt-based C++ source files for translation

Wherever your program uses a string literal (quoted text) that will be displayed in the user interface, make sure to get it processed by the [*translation function*](https://doc.qt.io/qt-5/i18n-source-translation.html#using-tr-for-all-literal-text). In source codes, `tr()` is indeed used to mark translatable strings so that, at runtime, `Qt` may replace them by their translated version that corresponds to the display language.

In the translation process, it's very important to know how to correctly call `tr()` since it determines the context that will be associated with any string when it's about to translate it.

Therefore, in the Slicer internationalization process, we have retained some recommendations on how to correctly use the translation function. Such guideline is described in the following sections.

### How to use *tr()* in QObject classes

Within a class inheriting from QObject, whether this inheritance is direct or not, all that is necessary to do is to use the [tr()](https://doc.qt.io/qt-5/qobject.html#tr) function to obtain translated text for your classes.
```c++
LoginWidget::LoginWidget()
{
    QLabel *label = new QLabel(tr("Password:"));
    ...
}
````
Classes inheriting from QObject should add the [Q_OBJECT](https://doc.qt.io/qt-5/i18n-source-translation.html#defining-a-translation-context) macro in their definition so that the translation context is correctly handled by `Qt`.
```c++
class MainWindow : public QMainWindow
{
    Q_OBJECT

    public:
        MainWindow();
        ...
```

> **_NOTE:_**  To avoid errors with some build tools (e.g. cmake), it's recommanded to always declare classes with Q_OBJECT macro in the header file (.h), not in the implementation one (.cpp). If for any reason your QObject class must be declared in the .cpp file (**e.g.** low level implementation classes), we recommand not to add the Q_OBJECT macro to that class, but rather, to prefix all `tr()` calls with the associated public class as follows : `PublicClassName::tr("text to translate")`

### How to use *tr()* in non-QObject classes

Non-QObject classes don't have a translation function, so directly calling `tr()` on them may result in errors.

A common practice is to prefix `tr()` calls on these classes with a Qt  core class like `QObject::tr()`, `QLabel::tr()`, etc. However, we don't recommend this approach since `lupdate` will associate such translatable strings with a context that is different from the class where they are located.
Therefore, when it's about to translate non-Qt classes, we recommand to provide translation support to the class by directly adding the [Q_DECLARE_TR_FUNCTIONS](https://doc.qt.io/qt-5/i18n-source-translation.html#translating-non-qt-classes) macro on it.
```c++
class MyClass
{
    Q_DECLARE_TR_FUNCTIONS(MyClass)

    public:
        MyClass();
        ...
};
```
Doing so will provide the class with `tr()` function that can be directly used to translate strings associated with the class, and makes it possible for `lupdate` to find translatable strings in the source code.

>**NOTE:** If for any reason the class name should not be exposed to other developers or translators (private classes, ...), we recommand to prefix `tr()` calls with the associated public class as follows :  `PublicClassName::tr("text to translate")`

### Translating multiline strings

Long strings may be defined in multiple lines like this:

```
QString help = QString(
  "Volume Rendering Module provides advanced tools for toggling interactive "
  "volume rendering of datasets."
  );
```

Translate such multiline strings using one `tr()` function like this to allow translators to translate complete sentences:

```
QString help = tr(
  "Volume Rendering Module provides advanced tools for toggling interactive "
  "volume rendering of datasets."
  );
```

Do not translate like this, as the translatable strings would contain sentence fragments:

```
// THIS IS WRONG!
QString help =
  tr("Volume Rendering Module provides advanced tools for toggling interactive ") +
  tr("volume rendering of datasets.<br/>");
```

### Translating keyboard shortcuts

According to [Qt recommendations](https://doc.qt.io/qt-6/qkeysequence.html#keyboard-layout-issues), keyboard shortcuts should be specified using translatable strings to be able to better accommodate different keyboard layouts commonly used for a specific language.

Examples:

```c++
this->RunFileAction->setShortcut(QKeySequence::Print);  // best option (if a standard key sequence is available)
this->RunFileAction->setShortcut(ctkConsole::tr("Ctrl+g"));  // preferred option, if a standard key sequence is not available
this->RunFileAction->setShortcut("Ctrl+g");  // do not use
this->RunFileAction->setShortcut(Qt::CTRL | Qt::Key_G);  // do not use
```

### Translating module title

Module title (the name that is visible in the module selector) is returned by the module class and it should be translated.

In older C++ loadable modules, the module name was set in CMakeLists.txt using a macro and was set in the module's header file using `QTMODULE_TITLE` precompiler definition. To make C++ loadable module title translatable (see example [here](https://github.com/Slicer/Slicer/commit/3f05bc595f25c49b0b213c6b116eebec595e03b2)):
- Remove `set(MODULE_TITLE ${MODULE_NAME})` and `TITLE ${MODULE_TITLE}` lines from `CMakeLists.txt`
- Use `tr("qSlicerLoadableModuleTemplateModule")` in `qSlicerGetTitleMacro()` in the module header file

### Qt lupdate common warnings

If `tr()` calls are not correctly handled on the source code, some warnings may appear when running `lupdate`.

#### Cannot invoke tr() like this

Qt lupdate tool throws `Cannot invoke tr() like this` warnings when translation function is called using an object like `q->tr(...)`. The problem is that lupdate cannot determine the class name `tr()` is called on and therefore it does not know the translation context.

This problem may be solved by spelling out the class name in the call, for example `qSlicerScalarVolumeDisplayWidget::tr(...)`, as described in the previous sections.

#### Class  _'SomeClassName'_  lacks Q_OBJECT macro

Qt lupdate tool throws `Class 'SomeClassName' lacks Q_OBJECT macro` warnings when translation function is called on a QObject class with no Q_OBJECT macro in its definition. The problem is also that `lupdate` cannot determine the class name `tr()` is called on and therefore it doesn't know the translation context.

The solution is to add the `Q_OBJECT` macro in the class where `tr()` is called, or, in case of classes that should not be exposed (private classes, low level implementation classes, ...), to prefix `tr()` calls with the associated public class, as described in the previous sections.

## Preparing VTK-based C++ source files for translation

Use the `vtkMRMLTr(context, sourceText)` macro for translating text that will be displayed to users (such as error messages). `context` must be set to the VTK class. For example:

    std::string fileType = vtkMRMLTr("vtkMRMLLinearTransformSequenceStorageNode", "Linear transform sequence");

Placeholders (strings that are replaced by values at runtime) are currently not supported.

## Preparing Python source files for translation

Import `_` and `translate` methods from `slicer.i18n`:

```python
from slicer.i18n import tr as _
from slicer.i18n import translate
```

Translate strings using `_(translatableString)` function (more convenient, as context is determined automatically) or `translate(contextName, translatableString)` function. Note that module categories are translated using the `qSlicerAbstractCoreModule` context.

```python
...
class ImportItkSnapLabel(ScriptedLoadableModule):
    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = _("Import ITK-Snap label description")
        self.parent.categories = [translate("qSlicerAbstractCoreModule", "Informatics")]
        ...
```

You can use Python-style named placeholders:
```
someMessage = _("{missing_file_count} of {total_file_count} selected files listed in the database cannot be found on disk.").format(
                    missing_file_count=missingFileCount, total_file_count=allFileCount))
```

## Identifying translatable strings

In the translation process, only strings that are displayed at the user interface level should be considered. Thus, strings refering to module names, file contents, file extensions, developer communications such as log messages (e.g. `PrintSelf` or `qCritical` outputs ) or any developer-related content, should be considered as non translatable.

To make it clear that a string must not be translated, `/*no tr*/` comment can be added to a string to indicate that the `tr()` function is intentionally not used.

## Using common base classes for shared strings

To prevent duplication of source strings, a `tr()` method of a common base class should be used for the following strings:
- Module category names (`Informatics`, `Registration`, `Segmentation`, ...) should be translated using `qSlicerAbstractCoreModule::tr("SomeCategory")` in C++ and `translate("qSlicerAbstractCoreModule", "SomeCategory")` in Python.

## Extract translatable strings

We rely on Qt's lupdate tool for extracting translatable strings from source code and merge it with existing translation files. We perform additional steps to extract translatable script from XML description of CLI modules and from Python files and we also support many languages. Therefore, a Python script is created that can perform all the processing steps: [update_translations.py]([url](https://github.com/Slicer/Slicer/blob/main/Utilities/Scripts/update_translations.py)).

### How to update translatable strings

#### Prerequisites
- Clone the https://github.com/Slicer/SlicerLanguageTranslations repository
- Clone the https://github.com/Slicer/Slicer repository
- Install Qt-6.3 or later (earlier versions do not have lupdate that can extract strings from Python code)
- Install Python-3.9 or later

#### Update translation source files
- Make sure that all pull requests on the repository submitted by Weblate are merged (to avoid merge conflicts). If changes are expected in the repository (for example, because there have been some recent updates) then it may worth waiting until those changes are completed. It is also possible to temporarily lock Weblate to not accept any modifications while we perform the steps below.
- Make sure the cloned repository is up-to-date and there are no locally modified files. (to avoid merge conflicts and avoid obsolete content getting into the translation source files)
- Run these commands:

```
set LUPDATE=c:\Qt6\6.3.0\msvc2019_64\bin\lupdate.exe
set PYTHON=c:\Users\andra\AppData\Local\Programs\Python\Python39\python.exe
set TRANSLATIONS=c:/D/SlicerLanguageTranslations/translations
set SLICER_SOURCE=c:/D/S4
set SLICER_BUILD=c:/D/S4D
%PYTHON% %SLICER_SOURCE%\Utilities\Scripts\update_translations.py -t %TRANSLATIONS% --lupdate %LUPDATE% -v --component Slicer -s %SLICER_SOURCE%
%PYTHON% %SLICER_SOURCE%\Utilities\Scripts\update_translations.py -t %TRANSLATIONS% --lupdate %LUPDATE% -v --component CTK -s %SLICER_BUILD%/CTK
@echo Process output: %errorlevel%
```

## How to make an extension translatable

### Tasks for extension developer

- Create source translation file for the extension in en-US locale using `update_translations.py`:

In the following steps, `MyExtension` will be used as example, replace that by the actual extension name (e.g., `SlicerIGT`).

Example (update paths according to locations on your computer):

```
set LUPDATE=c:\Qt6\6.3.0\msvc2019_64\bin\lupdate.exe
set PYTHON=c:\Users\andra\AppData\Local\Programs\Python\Python39\python.exe
set TRANSLATIONS=c:/D/SlicerLanguageTranslations/translations
set SLICER_SOURCE=c:/D/S4
%PYTHON% %SLICER_SOURCE%\Utilities\Scripts\update_translations.py -t %TRANSLATIONS% --lupdate %LUPDATE% -v --component MyExtension -s c:\D\MyExtension
```
- Contribute the newly created `MyExtension_en-US.ts` file to the https://github.com/Slicer/SlicerLanguageTranslations repository using a GitHub pull request.
- Wait for SlicerLanguagePacks team to merge the pull request and create the new translation component. You will get updates about the progress via comments in the pull request.

### Tasks for SlicerLanguagePacks team member

Whenever a pull request is received that adds translation for a new extension:

- Review and merge the pull request
- Create a new component on weblate, using the extension name.
  - Go to https://hosted.weblate.org/projects/3d-slicer/
  - Click on the `+` button above the list of components
  - Fill the form:
    - Component name: extension name
    - Source code repository: `https://github.com/Slicer/SlicerLanguageTranslations`
    - Repository branch: `main`
    - Click `Continue`
  - Fill the `Choose translation files to import` form:
    - Select: `File format Qt Linguist translation file, File mask translations/MyExtension_*.ts`
    - Click `Continue`
  - Fill the form:
    - Version control system: `GitHub pull request`
    - Template for new translations: `translations/MyExtension_en-US.ts`
    - Translation license: `ISC License`
    - Click `Save`
  - Wait until the update is completed
  - Check that these are the only warnings:
    - `Configure repository hooks for automated flow of updates to Weblate.`
    - `Add screenshots to show where strings are being used.`
    - `Use flags to indicate special strings in your translation.`
    - `Enable add-on: Add missing languages`
- Commment on the pull request that the translations can be added on Weblate.
