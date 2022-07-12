## Comment utiliser le pack Language Extension de Slicer

### Installation

- Téléchargez et installez Qt toolkit. C'est gratuit. Allez sur le site Web de Qt, faites défiler la page, cliquez sur le bouton `Télécharger le programme d'installation en ligne de Qt` et suivez les instructions. N'importe quelle version de Qt peut être utilisée.
  - Qt est nécessaire car il contient l'outil `lrelease`, qui permet de compiler un fichier de traduction lisible par l'homme( fichier .ts, qui sont édités sur Hosted Weblate) en un fichier binaire ( fichier .qm, que l'application peut utiliser).
  - La société Qt a ajouté de nombreuses déclarations trompeuses sur son site web pour tenter de pousser les utilisateurs à acheter une licence commerciale de Qt.
  - Une licence commerciale n'est pas nécessaire, même pour les utilisations commerciales de Qt. La version gratuite et open-source est suffisante.
- Téléchargez et installez version 5.x de 3D Slicer.
- Installez l'extension SlicerLanguagePacks.

![](Docs/ExtensionInstall.png)

- Dans Slicer, allez dans le module Language Tools et définissez le chemin de l'outil Qt lrelease. Il est situé dans le dossier où Qt a été installé.
L'emplacement par défaut sous Windows ressemble à ceci : `c:\Qt\5.15.0\msvc2019_64\bin\lrelease.exe`


### Télécharger et installer les dernières traductions

- Télécharger la dernière traduction
  - Option A : télécharger automatiquement depuis SlicerLanguageTranslations. C'est le moyen le plus simple d'obtenir des fichiers de traduction mis à jour, mais ces fichiers de traduction ne sont mis à jour qu'une fois par jour. Sélectionnez l'option `Github` dans la section `Input translations`.
  - Option B : téléchargez manuellement une langue depuis `Weblate`. Le téléchargement manuel nécessite plus d'étapes, mais il permet d'obtenir immédiatement les traductions les plus récentes.
    - Ouvrez le projet Slicer dans Weblate et ouvrez la page de traduction d'une langue (par exemple, le français).
    - Depuis Fichiers → Télécharger la traduction vous pouvez télécharger Hit `3d-slicer-3d-slicer-fr-ts`
    - Sélectionnez l'option de dossier Crowdin .ts files dans la section Input translations.
    - Définissez le chemin du dossier de téléchargement dans le dossier d'entrée de la section Traductions d'entrée.
    - Note : Il est recommandé de garder l'option Dernier fichier seulement cochée pour n'utiliser que le dernier fichier .ts téléchargé dans ce dossier car le navigateur web ne remplace généralement pas les fichiers précédemment téléchargés mais continue à ajouter des fichiers. En activant cette option, tous les anciens fichiers .ts sont ignorés.
  - Option C : téléchargement manuel de toutes les langues depuis Hosted Weblate. Le téléchargement manuel nécessite plus d'étapes, mais permet d'obtenir immédiatement les traductions les plus récentes.
    - Ouvrir le projet Slicer sur Hosted Weblate
    - Cliquez sur Fichiers → Télécharger la traduction sous forme de fichier ZIP pour télécharger 3d-slicer-3d-slicer.zip.
    - Sélectionnez l'option multilingue de Crowdin dans la section Traductions d'entrée.
    - Définissez le chemin du fichier zip dans Fichier ZIP d'entrée dans la section Traductions d'entrée.
    - Compilez les fichiers de traduction et installez-les dans l'application en cliquant sur le bouton Mettre à jour les fichiers de traduction.
    - Cliquez sur le bouton Redémarrer l'application pour commencer à utiliser les nouveaux fichiers de traduction.

![](Docs/LanguageTools.png)

### Définir la langue de l'application

La langue peut être sélectionnée dans le menu : Edit -> Application Settings, General Section -> Language. Si le sélecteur de langue n'apparaît pas, allez dans la section "Internationalisation" et cochez la case. L'application doit être redémarrée après avoir changé de langue.

![](Docs/LanguageSelector.png)
