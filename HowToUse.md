## How to use

### Setup

- [Download](https://download.slicer.org) and install a recent 3D Slicer Preview Release (released 2023-05-17 or later)
- Install SlicerLanguagePacks extension. 

[1] Click on the `Extensions Manager` icon.

[2] Write the word `Language` in the search box.
[3] Click on `Install` button.
[4] Click on `Restart` button.
  ![](Docs/LanguageInstall.png)

### Download and install latest translations

- Download latest translation
  - Option A: `Weblate`. Download selected langauges directly from Weblate. This allows getting the most recent translations immediately, which is useful for translators wanting to test their translated application immediately.
  - Option B: `GitHub`. Download all languages from [SlicerLanguageTranslations](https://github.com/Slicer/SlicerLanguageTranslations) repository. This is the fastest way to get updated translation files for all languages, but these translations files are updated only once a day.
- Refresh Weblate language list by querying the weblate server by clicking `refresh` button.
- Select all language that will be downloaded and installed in the `languages`
- Compile the translation files and install them into the application by clicking `Update translation files` button.
- Set the language of application in the `Application languge`
- Click `Restart the application` button to start using the new translation files in the user interface.

![](Docs/UpdateTranslation.png)

![](Docs/SetLanguage.png)


In order to understand more you can see an explanatory video [here](https://www.youtube.com/watch?v=pANAmbhl36o&t=10s).
