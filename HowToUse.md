## How to use

### Setup

- [Download](https://download.slicer.org) and install a recent 3D Slicer Preview Release (2024-11-23 or later)
- Install the SlicerLanguagePacks extension. 
  - `1` : Open the `extension manager`
  - `2` : Type LanguagePacks in the `search bar`
  - `3` : Click on `Install`
  - `4` : Click on `Restart`.
  ![](Docs/LanguageInstall.png)

### Download and install the latest translations

- `1` : Download the latest translations
  - Option A: `Weblate`. Download selected languages directly from Slicer Weblate. This enables getting the most recent translations, which is useful for translators who want to test their translated application immediately.
  - Option B: `GitHub`. Download all languages from the[SlicerLanguageTranslations](https://github.com/Slicer/SlicerLanguageTranslations) repository. This is the fastest way to get updated translation files for all languages, but these translations files are updated only once a day.
- `2` : Refresh the language list by clicking `refresh` button to query the Weblate server.
- `3` : Select the languages that will be installed in the `languages` field.
- `4` : Compile the translation files and install them into the application by clicking the `Update translation files` button.

![](Docs/UpdateTranslation.png)

### Set the language of the application

- Set the language of application in the `Application language` field.
- Click on the `Restart the application` button to start using the new translation files in the user interface.

![](Docs/SetLanguage.png)


A video tutorial of the different steps is available [here](https://www.youtube.com/watch?v=8Omd_qQTJOk).
