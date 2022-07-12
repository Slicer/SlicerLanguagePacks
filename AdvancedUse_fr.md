## Conseils et astuces

### L'outil de recherche de texte

L'outil "Find Text" a été ajouté pour extraire rapidement un texte de l'application et trouver les occurrences de ce texte dans le site Web de traduction :

- Allez dans le module Language Tools
- Ouvrez la section `Find Text`.
- Définissez la langue d'édition : les chaînes extraites seront ouvertes sur le site Web, montrant les traductions dans cette langue. Exemple : `fr-FR`, `hu-HU`.
- Cochez la case "Activer la recherche de texte".
- Appuyez sur le raccourci `Ctrl+6` à tout moment pour afficher le sélecteur de widgets.
- Cliquez sur le widget qui contient du texte traduisible (appuyez sur n'importe quelle touche pour annuler la sélection du widget).
- Cliquez sur "OK" pour ouvrir le texte trouvé sur le site de traduction.

![](Docs/FindText.png)

Limitations connues :
- L'outil extrait uniquement les widgets des widgets Qt (pas des vues rendues par la bibliothèque VTK).
- L'extraction du texte des fenêtres flottantes et popup n'est pas supportée.

### Traduction des liens externes

Si le texte traduit contient des liens vers des sites externes qui prennent en charge plusieurs langues, il est généralement préférable de ne pas coder en dur une langue spécifique (pour permettre à ce site externe d'utiliser sa propre langue de préférence). Par exemple : <https://docs.github.com/get-started/quickstart/fork-a-repo> est préférable (au lieu de coder en dur l'anglais en ajoutant `/en` comme ceci : <https://docs.github.com/en/get-started/quickstart/fork-a-repo>).

Cependant, tous les sites ne peuvent pas définir automatiquement une langue de préférence. Par exemple, [ReadTheDocs](https://readthedocs.org) exige de spécifier explicitement le code de langue dans l'URL : <https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/import_process.html> est valide, mais <https://docs.godotengine.org/stable/tutorials/assets_pipeline/import_process.html> est une URL invalide. Dans ces cas, l'URL du lien doit être modifiée dans chaque traduction pour correspondre à la langue cible.

Voir la discussion connexe [ici](https://github.com/Slicer/Slicer/pull/6401#discussion_r884768951).

## Utilisation avancée

### Installer les fichiers de traduction hors ligne

Les fichiers de traduction (.ts) peuvent être téléchargés dans un dossier et installés à partir de celui-ci ultérieurement, sans accès au réseau.

Les fichiers de traduction peuvent être téléchargés depuis Weblate ou GitHub. Par exemple, ouvrez [Slicer project in Weblate](https://hosted.weblate.org/project/3d-slicer), sélectionnez la page de traduction d'une langue (telle que [Français](https://hosted.weblate.org/projects/3d-slicer/3d-slicer/fr/)), puis dans le menu choisissez `Files` -> `Download translation`.

Installez les fichiers de traduction :
- Sélectionnez l'option `Dossier local`.
- Définissez le dossier contenant le(s) fichier(s) .ts dans le `Dossier d'entrée` dans la section `Input translations`.
- Cochez l'option `Fichier le plus récent uniquement` pour n'utiliser que le dernier fichier .ts téléchargé. C'est utile si le dossier local est défini directement sur le dossier de téléchargement du navigateur web.
- Compilez les fichiers de traduction et installez-les dans l'application en cliquant sur le bouton "Mettre à jour les fichiers de traduction".
