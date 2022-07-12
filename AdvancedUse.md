## Tips and tricks

### Find text tool

`Find text` tool is added for quick extraction of text from the application and find occurrences of that text in the translation website:

- Go to Language Tools module
- Open `Find text` section
- Set edited language: the extracted strings will be opened on the website, showing translations in this language. Example: `fr-FR`, `hu-HU`.
- Check `Enable text finder` checkbox
- Hit `Ctrl+6` shortcut anytime to show the widget selector
- Click on the widget that contains translatable text (hit any key to cancel widget selection)
- Click `OK` to open the found text on the translation website

![](Docs/FindText.png)

Known limitations:
- The tool only extract widgets from Qt widgets (not from views rendered by VTK library).
- Extraction text from floating and popup windows is not supported.

### Translation of external links

If the translated text contains links to external sites that support multiple languages, it is generally preferable to not hardcode a specific language (to allow that external site to use its own preferred language). For example: <https://docs.github.com/get-started/quickstart/fork-a-repo> is preferred (instead of hardcoding English by adding `/en` like this: <https://docs.github.com/en/get-started/quickstart/fork-a-repo>).

However, not all sites can automatically set a preferred language. For example, [ReadTheDocs](https://readthedocs.org) requires explicitly specifying language code in the URL: <https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/import_process.html> is valid, but <https://docs.godotengine.org/stable/tutorials/assets_pipeline/import_process.html> is an invalid URL. In these cases, the URL of the link should be changed in each translation to match the target language.

See related discussion [here](https://github.com/Slicer/Slicer/pull/6401#discussion_r884768951).

## Advanced use

### Install translation files offline

Translation (.ts) files can be downloaded to a folder and installed from there later, without network access.

Translation files can be downloaded from Weblate or GitHub. For example, open [Slicer project in Weblate](https://hosted.weblate.org/project/3d-slicer) select translation page of a language (such as [French](https://hosted.weblate.org/projects/3d-slicer/3d-slicer/fr/)), then in the menu choose `Files` -> `Download translation`.

Install the translation files:
- Select `Local folder` option
- Set the folder containing .ts file(s) in `Input folder` in `Input translations` section.
- Check `Latest file only` option to only use the latest downloaded .ts file. It is useful if local folder is set directly to the web browser's download folder.
- Compile the translation files and install them into the application by clicking `Update translation files` button.
