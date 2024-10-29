
# Guide pour les développeurs de modules Slicer

Ces instructions sont destinées aux développeurs de modules Slicer (dans le noyau Slicer ou dans les extensions Slicer) qui souhaitent rendre leurs modules traduisibles.

## Préparation des fichiers .ui pour la traduction

Par défaut, la plupart des propriétés de chaîne et de liste de chaînes qui apparaissent dans les fichiers.ui sont disponibles pour la traduction. Ceci est généralement le comportement correct, mais dans certains cas les propriétés contiennent des chaînes qui ne doivent pas être traduites (et donc ne doivent pas apparaître dans les fichiers source de traduction (.ts)).

Les développeurs **doivent cocher les propriétés qui ne doivent pas être traduites dans le concepteur Qt** en décochant l’option `Translatable`. La seule exception est que lorsque la valeur de propriété n’est pas définie (mais laissée à la valeur par défaut, cela signifie généralement qu’elle est laissée vide), dans ce cas l’option traduisible doit être laissée non définie.

Ces propriétés doivent être marquées comme non traduisibles :
- Dans les widgets de sélection de nœud, tels que qMRMLNodeComboBox, qMRMLCheckableNodeComboBox, qMRMLSubjectHierarchyTreeView, qMRMLTreeView :
  - `nodeTypes`
  - `hideChildNodeTypes`
  - `interactionNodeSingletonTag` (si ce n’est pas la valeur par défaut "Singleton")
  - `sceneModelType`
  - `levelFilter`
- Dans les widgets MRML (qMRML...Widget) qui prennent en charge des quantités, telles que qMRMLRangeWidget ou qMRMLCoordinatesWidget :
  - `quantity`
- Dans les widgets qui enregistrent des données dans les paramètres de l’application, tels que ctkPathLineEdit, qMRMLSegmentationFileExportWidget, qMRMLSegmentEditorWidget :
  - `settingKey`
  - `defaultTerminologyEntrySettingsKey`
- Dans les widgets qui enregistrent des données dans des attributs de hiérarchie de nœud ou de sujet, tels que qMRMLSubjectHierarchyComboBox, SubjectHierarchyTreeView :
  - `includeItemAttributeNamesFilter`
  - `excludeItemAttributeNamesFilter`
  - `includeNodeAttributeNamesFilter`
  - `excludeNodeAttributeNamesFilter`
- Dans les widgets de vue de coupe, tels que qMRMLSliceControllerWidget et qMRMLSliceWidget :
  - `sliceViewName`
  - `sliceOrientation`
- Dans qMRMLSegmentationConversionParametersWidget :
  - `targetRepresentationName`
- Dans qSlicerMouseModeToolBar :
  - `defaultPlaceClassName`

![](Docs/DesignerMarkAsNonTranslatable.png)

## Préparation des fichiers sources C++ basés sur Qt pour la traduction

Lorsque votre programme utilise une chaîne littérale (texte entre guillemets) qui sera affichée dans l’interface utilisateur, assurez-vous de la faire traiter par la [*fonction traduction*] (https://doc.qt.io/qt-5/i18n-source-translation.html#using-tr-for-all-literal-text). Dans les codes source, on utilise effectivement `tr()` pour marquer les chaînes traduisibles de sorte que, à l’exécution, `Qt` peut les remplacer par leur version traduite qui correspond au langage d’affichage.

Dans le processus de traduction, il est très important de savoir comment appeler correctement `tr()`, car cela détermine le contexte qui sera associé à toute chaîne lorsqu’elle sera traduite.

Par conséquent, dans le processus d’internationalisation de Slicer, nous avons retenu quelques recommandations sur la façon d’utiliser correctement la fonction de traduction. Cette ligne directrice est décrite dans les sections suivantes.

### Comment utiliser *tr()* dans les classes QObject

Dans une classe héritée de QObject, que cette héritage soit direct ou non, il suffit d’utiliser la fonction [tr()](https://doc.qt.io/qt-5/qobject.html#tr) pour obtenir le texte traduit pour vos classes.
```c++
LoginWidget::LoginWidget()
{
    QLabel *label = new QLabel(tr("Password:"));
    ...
}
````
Les classes héritées de QObject devraient ajouter la macro [Q_OBJECT](https://doc.qt.io/qt-5/i18n-source-translation.html#defining-a-translation-context) dans leur définition afin que le contexte de traduction soit correctement géré par `Qt`.
```c++
class MainWindow : public QMainWindow
{
    Q_OBJECT

    public:
        MainWindow();
        ...
```

> **_REMARQUE :_**  Pour éviter les erreurs avec certains outils de compilation (p.e. cmake), il est recommandé de toujours déclarer des classes avec la macro Q_OBJECT dans le fichier d’en-tête (.h) et non dans celui de l’implémentation (.cpp). Si pour une raison quelconque votre classe QObject doit être déclarée dans le fichier .cpp (**e.g.** classes d’implémentation de bas niveau), nous recommandons de ne pas ajouter la macro Q_OBJECT à cette classe, mais plutôt de préfixer tous les appels `tr()` avec la classe publique associée comme suit : `PublicClassName::tr("text to translate")`

### Comment utiliser *tr()* dans les classes non-QObject

Les classes non QObject n’ont pas de fonction de traduction, donc l’appel direct à `tr()` peut entraîner des erreurs.

Il est courant de préfixer `tr()` à ces classes avec une classe Qt core comme `QObject::tr()`, `QLabel::tr()`, etc. Cependant, nous ne recommandons pas cette approche puisque `lupdate` associera ces chaînes traduisibles à un contexte différent de la classe dans laquelle elles se trouvent.
Par conséquent, lorsqu’il s’agit de traduire des classes non-Qt, nous recommandons d’offrir un soutien à la traduction de la classe en ajoutant directement la macro [Q_DECLARE_TR_FUNCTIONS] (https://doc.qt.io/qt-5/i18n-source-translation.html#translating-non-qt-classes) sur celle-ci.
```c++
class MyClass
{
    Q_DECLARE_TR_FUNCTIONS(MyClass)

    public:
        MyClass();
        ...
};
```
Faire cela fournira à la classe la fonction `tr()` qui peut être utilisée directement pour traduire les chaînes associées à la classe, et permettra à `lupdate` de trouver les chaînes traduisibles dans le code source.

> **REMARQUE :** Si, pour une raison quelconque, le nom de la classe ne doit pas être exposé à d'autres développeurs ou traducteurs (classes privées, ...), nous recommandons de préfixer les appels à `tr()` avec le nom de la classe publique associée comme suit : `PublicClassName::tr("texte à traduire")`

### Traduction de chaînes multilignes

Les longues chaînes peuvent être définies sur plusieurs lignes comme ceci :

```
QString help = QString(
  "Volume Rendering Module provides advanced tools for toggling interactive "
  "volume rendering of datasets."
  );
```

Traduisons de telles chaînes multilignes en utilisant une seule fonction `tr()` comme ceci pour permettre aux traducteurs de traduire des phrases complètes :

```
QString help = tr(
  "Volume Rendering Module provides advanced tools for toggling interactive "
  "volume rendering of datasets."
  );
```

Ne traduisez pas comme ça, car les chaînes traduisibles contiendraient des fragments de phrases :

```
// C'est faux !
QString help =
  tr("Volume Rendering Module provides advanced tools for toggling interactive ") +
  tr("volume rendering of datasets.<br/>");
```

### Traduire les raccourcis clavier

Selon les [recommandations de Qt](https://doc.qt.io/qt-6/qkeysequence.html#keyboard-layout-issues), les raccourcis clavier doivent être spécifiés en utilisant des chaînes traduisibles afin de mieux s'adapter aux différents types de clavier couramment utilisés pour une langue spécifique.

Exemples :

```c++
this->RunFileAction->setShortcut(QKeySequence::Print);  // meilleure option (si une séquence de touches standard est disponible)
this->RunFileAction->setShortcut(ctkConsole::tr("Ctrl+g"));  // option préférée, si une séquence de touches standard n'est pas disponible
this->RunFileAction->setShortcut("Ctrl+g");  // ne pas utiliser
this->RunFileAction->setShortcut(Qt::CTRL | Qt::Key_G);  // ne pas utiliser
```

### Traduction du titre du module

Le titre du module (le nom visible dans le sélecteur de module) est renvoyé par la classe du module et doit être traduit.

Dans les anciens modules C++ chargeables, le nom du module était défini dans CMakeLists.txt à l'aide d'une macro et était réglé dans le fichier d'en-tête du module en utilisant la définition de précompilateur `QTMODULE_TITLE`. Pour rendre le titre du module C++ chargeable traduisible (voir l'exemple [ici](https://github.com/Slicer/Slicer/commit/3f05bc595f25c49b0b213c6b116eebec595e03b2)) :
- Supprimez les lignes `set(MODULE_TITLE ${MODULE_NAME})` et `TITLE ${MODULE_TITLE}` de `CMakeLists.txt`
- Utilisez `tr("qSlicerLoadableModuleTemplateModule")` dans `qSlicerGetTitleMacro()` dans le fichier d'en-tête du module

### Avertissements courants de Qt lupdate

Si les appels à `tr()` ne sont pas correctement gérés dans le code source, des avertissements peuvent apparaître lors de l'exécution de `lupdate`.

#### Impossible d'invoquer tr() de cette manière

L'outil Qt lupdate lance des avertissements `Impossible d'invoquer tr() de cette manière` lorsque la fonction de traduction est appelée en utilisant un objet comme `q->tr(...)`. Le problème est que lupdate ne peut pas déterminer le nom de la classe sur laquelle `tr()` est appelé et ne connaît donc pas le contexte de la traduction.

Ce problème peut être résolu en explicitant le nom de la classe dans l'appel, par exemple `qSlicerScalarVolumeDisplayWidget::tr(...)`, comme décrit dans les sections précédentes.

#### La classe _'SomeClassName'_ manque du macro Q_OBJECT 

L'outil Qt lupdate lance des avertissements `La classe 'SomeClassName' manque du macro Q_OBJECT` lorsque la fonction de traduction est appelée sur une classe QObject sans le macro Q_OBJECT dans sa définition. Le problème est également que `lupdate` ne peut pas déterminer le nom de la classe sur laquelle `tr()` est appelé et ne connaît donc pas le contexte de la traduction.

La solution consiste à ajouter le macro `Q_OBJECT` dans la classe où `tr()` est appelé, ou, dans le cas de classes qui ne devraient pas être exposées (classes privées, classes d'implémentation de bas niveau, ...), à préfixer les appels à `tr()` avec la classe publique associée, comme décrit dans les sections précédentes.

## Préparation des fichiers source C++ basés sur VTK pour la traduction

Utilisez la macro `vtkMRMLTr(context, sourceText)` pour traduire le texte qui sera affiché aux utilisateurs (comme les messages d'erreur). `context` doit être défini comme la classe VTK. Par exemple :

    std::string fileType = vtkMRMLTr("vtkMRMLLinearTransformSequenceStorageNode", "Séquence de transformation linéaire");

Des espaces réservés de style Qt (%1, %2, %3, ..., %9) peuvent être utilisés. Par exemple :

    std::string displayableText = vtkMRMLI18N::Format(
      vtkMRMLTr("vtkMRMLVolumeArchetypeStorageNode", "Impossible de lire le fichier '%1' en tant que volume de type '%2'."),
      filename.c_str(),
      volumeType.c_str());

Utilisez `%%` au lieu d'un simple `%` pour empêcher le remplacement. Par exemple, `"certain %%3 truc"` donnera `"certain %3 truc"` (et ne sera pas remplacé par le troisième argument de chaîne de remplacement).

## Préparation des fichiers source Python pour la traduction

Importez les méthodes `_` et `translate` depuis `slicer.i18n` :

```python
from slicer.i18n import tr as _
from slicer.i18n import translate
```

Traduisiez les chaînes en utilisant la fonction `_(translatableString)` (plus pratique, car le contexte est déterminé automatiquement) ou la fonction `translate(contextName, translatableString)`. Notez que les catégories de modules sont traduites en utilisant le contexte `qSlicerAbstractCoreModule`.

```python
...
class ImportItkSnapLabel(ScriptedLoadableModule):
    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = _("Importer la description des étiquettes ITK-Snap")
        self.parent.categories = [translate("qSlicerAbstractCoreModule", "Informatique")]
        ...
```

Vous pouvez utiliser des espaces réservés nommés au style Python :
```
someMessage = _("{missing_file_count} des {total_file_count} fichiers sélectionnés dans la base de données sont introuvables sur le disque.").format(
                    missing_file_count=missingFileCount, total_file_count=allFileCount))
```

Nous devons éviter les f-strings, car la partie entre {} est du code Python exécutable, et nous ne voulons pas que les gens puissent l'utiliser pour injecter un comportement incorrect via les fichiers de traduction.
```
```python
# Ce code est incorrect, car les traducteurs pourraient injecter du code Python arbitraire
# que l'application exécuterait. 
someText = _(f"{missingFileCount} des {allFileCount} fichiers sélectionnés listés dans la base de données ne peuvent pas être trouvés sur le disque.")
```

## Identification des chaînes traduisibles

Dans le processus de traduction, seules les chaînes affichées au niveau de l'interface utilisateur doivent être prises en compte. Ainsi, les chaînes faisant référence aux noms de modules, au contenu des fichiers, aux extensions de fichiers, aux communications entre développeurs telles que les messages de log (par exemple, les sorties `PrintSelf` ou `qCritical`) ou tout contenu lié aux développeurs doivent être considérées comme non traduisibles.

Pour bien faire comprendre qu'une chaîne ne doit pas être traduite, un commentaire `/*no tr*/` peut être ajouté à une chaîne pour indiquer que la fonction `tr()` n'est pas utilisée intentionnellement.

## Utilisation de classes de base communes pour les chaînes partagées

Pour éviter la duplication des chaînes sources, une méthode `tr()` d'une classe de base commune doit être utilisée pour les chaînes suivantes :
- Les noms de catégories de modules (`Informatique`, `Inscription`, `Segmentation`, ...) doivent être traduits en utilisant `qSlicerAbstractCoreModule::tr("SomeCategory")` en C++ et `translate("qSlicerAbstractCoreModule", "SomeCategory")` en Python.

## Extraire les chaînes traduisibles

Nous comptons sur l'outil lupdate de Qt pour extraire les chaînes traduisibles du code source et les fusionner avec les fichiers de traduction existants. Nous effectuons des étapes supplémentaires pour extraire des scripts traduisibles à partir de la description XML des modules CLI et des fichiers Python, et nous supportons également de nombreuses langues. Par conséquent, un script Python est créé pour effectuer toutes les étapes de traitement : [update_translations.py]([url](https://github.com/Slicer/Slicer/blob/main/Utilities/Scripts/update_translations.py)).

### Comment mettre à jour les chaînes traduisibles

#### Prérequis
- Clonez le dépôt https://github.com/Slicer/SlicerLanguageTranslations
- Clonez le dépôt https://github.com/Slicer/Slicer
- Installez Qt-6.3 ou une version ultérieure (les versions antérieures n'ont pas lupdate capable d'extraire les chaînes du code Python)
- Installez Python-3.9 ou une version ultérieure

#### Mettre à jour les fichiers source de traduction
- Assurez-vous que toutes les demandes de tirage dans le dépôt soumises par Weblate soient fusionnées (pour éviter les conflits de fusion). Si des changements sont attendus dans le dépôt (par exemple, à cause de mises à jour récentes), il peut être utile d’attendre que ces changements soient terminés. Il est également possible de verrouiller temporairement Weblate pour ne pas accepter de modifications pendant que nous effectuons les étapes ci-dessous.
- Assurez-vous que le dépôt cloné est à jour et qu'il n'y a pas de fichiers modifiés localement. (pour éviter les conflits de fusion et éviter que du contenu obsolète n'entre dans les fichiers source de traduction)
- Exécutez ces commandes :

```
set LUPDATE=c:\Qt6\6.3.0\msvc2019_64\bin\lupdate.exe
set PYTHON=c:\Users\andra\AppData\Local\Programs\Python\Python39\python.exe
set TRANSLATIONS=c:/D/SlicerLanguageTranslations/translations
set SLICER_SOURCE=c:/D/S4
set SLICER_BUILD=c:/D/S4D
%PYTHON% %SLICER_SOURCE%\Utilities\Scripts\update_translations.py -t %TRANSLATIONS% --lupdate %LUPDATE% -v --component Slicer -s %SLICER_SOURCE%
%PYTHON% %SLICER_SOURCE%\Utilities\Scripts\update_translations.py -t %TRANSLATIONS% --lupdate %LUPDATE% -v --component CTK -s %SLICER_BUILD%/CTK
@echo Sortie du processus : %errorlevel%
```

## Comment rendre une extension traduisible

### Tâches pour le développeur d'extension

- Créez un fichier de traduction source pour l'extension en locale en-US en utilisant `update_translations.py` :

Dans les étapes suivantes, `MyExtension` sera utilisé comme exemple, remplacez-le par le nom réel de l'extension (par exemple, `SlicerIGT`).

Exemple (mettez à jour les chemins en fonction des emplacements sur votre ordinateur) :

```
set LUPDATE=c:\Qt6\6.3.0\msvc2019_64\bin\lupdate.exe
set PYTHON=c:\Users\andra\AppData\Local\Programs\Python\Python39\python.exe
set TRANSLATIONS=c:/D/SlicerLanguageTranslations/translations
set SLICER_SOURCE=c:/D/S4
%PYTHON% %SLICER_SOURCE%\Utilities\Scripts\update_translations.py -t %TRANSLATIONS% --lupdate %LUPDATE% -v --component MyExtension -s c:\D\MyExtension
```
- Contribuez le fichier nouvellement créé `MyExtension_en-US.ts` au dépôt https://github.com/Slicer/SlicerLanguageTranslations en utilisant une demande de tirage GitHub.
- Attendez que l'équipe des SlicerLanguagePacks fusionne la demande de tirage et crée le nouveau composant de traduction. Vous recevrez des mises à jour sur l'avancement via des commentaires dans la demande de tirage.

### Tâches pour un membre de l'équipe SlicerLanguagePacks

Chaque fois qu'une demande de tirage est reçue ajoutant une traduction pour une nouvelle extension :

- Examinez et fusionnez la demande de tirage
- Créez un nouveau composant sur Weblate, en utilisant le nom de l'extension.
  - Allez sur https://hosted.weblate.org/projects/3d-slicer/
  - Cliquez sur le bouton `+` au-dessus de la liste des composants
  - Remplissez le formulaire :
    - Nom du composant : nom de l'extension
    - Répertoire du code source : `https://github.com/Slicer/SlicerLanguageTranslations`
    - Branche du répertoire : `main`
    - Cliquez sur `Continuer`
  - Remplissez le formulaire `Choisir les fichiers de traduction à importer` :
    - Sélectionnez : `Format de fichier Qt Linguist translation file, Masque de fichier translations/MyExtension_*.ts`
    - Cliquez sur `Continuer`
  - Remplissez le formulaire :
    - Système de contrôle de version : `Demande de tirage GitHub`
    - Modèle pour les nouvelles traductions : `translations/MyExtension_en-US.ts`
    - Licence de traduction : `ISC License`
    - Cliquez sur `Enregistrer`
  - Attendez que la mise à jour soit terminée
  - Vérifiez que ce sont les seuls avertissements :
    - `Configurer les hooks du répertoire pour un flux automatisé de mises à jour vers Weblate.`
    - `Ajoutez des captures d'écran pour montrer où les chaînes sont utilisées.`
    - `Utilisez des drapeaux pour indiquer des chaînes spéciales dans votre traduction.`
    - `Activer le module complémentaire : Ajouter des langues manquantes`
- Commentez sur la demande de tirage que les traductions peuvent être ajoutées sur Weblate.
