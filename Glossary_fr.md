Glossaire

Les termes utilisés dans divers domaines de l'informatique médicale et biomédicale ainsi que dans les images cliniques ne sont pas toujours cohérents. Cette section définit les termes couramment utilisés dans 3D Slicer, en particulier ceux qui peuvent avoir des significations différentes dans d'autres contextes.

Limites: Décrit la boîte englobante d'un objet spatial le long de 3 axes. Défini en VTK par 6 valeurs à virgule flottante : Xmin, Xmax, Ymin, Ymax, Zmin, Zmax.

Luminosité / Contraste : Spécifie la correspondance linéaire des valeurs de voxel à la luminosité d'un pixel affiché. La luminosité est décalage linéaire, le contraste est le multiplicateur. En imagerie médicale, cette correspondance linéaire est plus communément spécifiée par des valeurs de fenêtre/niveau.

Cellule : Les cellules de données sont des éléments topologiques simples de maillages, tels que des lignes, des polygones, des tétraèdres, etc.

Légende des couleurs (ou barre de couleur, barre scalaire) : Un widget superposé sur des vues en coupes ou en 3D qui affiche une légende des couleurs, indiquant la signification des couleurs.

Système de coordonnées (ou cadre de coordonnées, référentiel, espace) :Spécifié par la position de l'origine, les directions des axes et l'unité de distance. Tous les systèmes de coordonnées en 3D Slicer sont droitiers.

Extension: Une collection de modules qui n'est pas incluse dans l'application principale, mais qui peut être téléchargée et installée à l'aide du gestionnaire d'extensions.

Gestionnaire d'extensions: Un composant logiciel de Slicer qui permet de parcourir, d'installer et de désinstaller des extensions dans le catalogue des extensions (également connu sous le nom de boutique d'applications Slicer) directement à partir de l'application.

Index des extensions : Un référentiel qui contient la description de chaque extension à partir duquel le catalogue des extensions est construit.

Étendue : Plage de coordonnées entières le long de 3 axes. Défini en VTK par 6 valeurs, pour les axes IJK : I_min, I_max, J_min, J_max, K_min, K_max. Les valeurs minimales et maximales sont inclusives, donc la taille d'un tableau est (I_max - I_min + 1) x (J_max - J_min + 1) x (K_max - K_min + 1).

Repère fiducial : Représente un point dans l'espace 3D. Le terme provient de la chirurgie guidée par l'image, où des "marqueurs fiduciaires" sont utilisés pour marquer les positions des points.

Cadre : Un point temporel dans une séquence temporelle. Pour éviter toute ambiguïté, ce terme n'est pas utilisé pour désigner une coupe d'un volume.

Géométrie : Spécifie l'emplacement et la forme d'un objet dans l'espace 3D. Voir le terme "Volume" pour la définition de la géométrie d'image.

Intensité de l'image : Elle réfère généralement à la valeur d'un voxel. La luminosité et la couleur des pixels affichés sont calculées à partir de cette valeur en fonction de la fenêtre/niveau choisie et de la table de recherche de couleurs.

IJK : Axes du système de coordonnées du voxel. Les valeurs de coordonnées entières correspondent aux positions centrales des voxels. Les valeurs IJK sont souvent utilisées comme valeurs de coordonnées pour désigner un élément dans un tableau 3D. Selon la convention VTK, I indexe la colonne, J indexe la ligne, K indexe la tranche. Notez que numpy utilise la convention inverse, où a[K][J][I]. Parfois, cette disposition de la mémoire est décrite comme I étant l'indice le plus rapide et K étant l'indice le plus lent.

ITK : Bibliothèque logicielle utilisée par Slicer pour la plupart des opérations de traitement d'image.

Labelmap /Carte d'étiquette (ou volume de labelmap, nœud de volume de labelmap) : Nœud de volume qui a des valeurs de voxel discrètes (entières). Chaque valeur correspond généralement à une structure ou à une région spécifique. Cela permet une représentation compacte de régions non superposées dans un seul tableau 3D. La plupart des logiciels utilisent une seule image de labelmap pour stocker une segmentation d'image, mais Slicer utilise un nœud de segmentation dédié, qui peut contenir plusieurs représentations (multiples images de labelmap pour permettre le stockage de segments superposés ; représentation de surface fermée pour une visualisation 3D rapide, etc.).

LPS (Left-posterior-superior) :Système de coordonnées anatomiques gauche-postérieur-supérieur. Système de coordonnées le plus couramment utilisé en informatique médicale d'imagerie. Slicer stocke toutes les données dans le système de coordonnées LPS sur le disque (et convertit en/from RAS lors de l'écriture/lecture depuis le disque).

Markups: Objets géométriques simples et mesures que l'utilisateur peut placer dans les vues. Le module "Markups" peut être utilisé pour créer de tels objets. Il existe plusieurs types, tels que liste de points, ligne, courbe, plan, ROI (Région d'Intérêt).

Volume source : Les valeurs de voxel de ce volume sont utilisées pendant la segmentation par les effets qui dépendent de l'intensité d'un volume sous-jacent.

MRML (Medical Reality Markup Language): Une bibliothèque logicielle pour le stockage, la visualisation et le traitement d'objets d'informations qui peuvent être utilisés dans des applications médicales. La bibliothèque est conçue pour être réutilisable dans différentes applications logicielles, mais 3D Slicer est la seule application majeure connue pour l'utiliser.

Modèle (ou nœud de modèle) : Nœud MRML stockant un maillage de surface (composé de triangles, polygones ou autres cellules 2D) ou un maillage volumétrique (composé de tétraèdres, de coins ou d'autres cellules 3D).

Module (ou module Slicer) : Un module Slicer est un composant logiciel composé d'une interface utilisateur graphique (affichée dans le panneau du module lorsque le module est sélectionné), d'une logique (implémentant des algorithmes qui opèrent sur les nœuds MRML) et peut fournir de nouveaux types de nœuds MRML, des gestionnaires d'affichage (responsables de l'affichage de ces nœuds dans les vues), des greffons d'entrée/sortie (responsables du chargement/sauvegarde de nœuds MRML dans des fichiers) et divers autres greffons. Les modules sont généralement indépendants et ne communiquent entre eux que par la modification des nœuds MRML, mais parfois, un module utilise des fonctionnalités fournies par d'autres modules en appelant des méthodes dans sa logique

Nœud (ou nœud MRML) : Un objet de données dans la scène. Un nœud peut représenter des données (comme une image ou un maillage), décrire comment elles sont affichées (couleur, opacité, etc.), stockées sur le disque, les transformations spatiales qui leur sont appliquées, etc. Il existe une hiérarchie de classes C++ pour définir les comportements communs des nœuds, tels que la propriété d'être stockable sur le disque ou d'être transformable géométriquement. La structure de cette hiérarchie de classes peut être inspectée dans le code ou dans la documentation de l'API.

Marqueur d'orientation : Flèche, boîte ou marqueur en forme d'humain pour montrer les directions des axes dans les vues en tranches et en 3D.

RAS (Right-anterior-superior) : Système de coordonnées anatomiques droite-antéro-supérieure. Système de coordonnées utilisé en interne dans Slicer. Il peut être converti vers/depuis le système de coordonnées LPS en inversant la direction des deux premiers axes.

Référence : Elle (la référence) n'a pas de signification spécifique, mais fait généralement référence à une entrée secondaire (objet de données, cadre de coordonnées, géométrie, etc.) pour une opération.

ROI (Region of interest) : Spécifie une région en forme de boîte en 3D. Peut être utilisée pour rogner des volumes, découper des modèles, etc.

Enregistrement : processus d'alignement d'objets dans l'espace. Le résultat de l'enregistrement est une transformation, qui transforme l'objet "en mouvement" en objet "fixe".

Résolution: Taille du voxel d'un volume, généralement spécifiée en mm/pixel. Elle est rarement utilisée dans l'interface utilisateur car son sens est légèrement trompeur : une valeur de haute résolution signifie un grand espacement, ce qui correspond à une résolution d'image grossière (basse).

Régle : Cela peut se référer à : 1. Règle d'affichage : La ligne qui est affichée en superposition dans les vues pour servir de référence de taille. 2. Ligne de marquage : outil de mesure de distance.

Composant scalaire : Un élément d'un vecteur. Le nombre de composants scalaires correspond à la longueur du vecteur.

Valeur scalaire : Un nombre simple . Généralement à virgule flottante.

Scène (ou scène MRML) : C'est la structure de données qui contient toutes les données actuellement chargées dans l'application et des informations supplémentaires sur la façon dont elles doivent être affichées ou utilisées. Le terme provient de l'infographie.

Segment :Correspond à une structure unique dans une segmentation. Voir plus d'informations dans la section Segmentation d'image.

Segmentation (également connue sous le nom de délimitation, annotation, ensemble de structures, masque) : Processus de délimitation de structures 3D dans des images. La segmentation peut également se référer au nœud MRML qui est le résultat du processus de segmentation. Un nœud de segmentation contient généralement plusieurs segments (chaque segment correspond à une structure 3D). Les nœuds de segmentation ne sont pas des nœuds de labelmap ou de modèle, mais ils peuvent stocker plusieurs représentations (labelmap binaire, surface fermée, etc.). Voir plus d'informations dans la section Segmentation d'image.

Coupe : Intersection d'un objet 3D avec un plan.

Annotations des vues en coupe : texte dans le coin des vues en coupes affichant le nom et les balises DICOM sélectionnées des volumes affichés.

Espacement : Taille du voxel d'un volume, généralement spécifiée en mm/pixel.

Transformation : Peut transformer n'importe quel objet 3D d'un système de coordonnées à un autre. Le type le plus courant est la transformation rigide, qui peut changer la position et l'orientation d'un objet. Les transformations linéaires peuvent mettre à l'échelle, refléter, ciseler les objets. Les transformations non linéaires peuvent déformer arbitrairement l'espace 3D. Pour afficher un volume dans le système de coordonnées du monde, le volume doit être rééchantillonné, donc une transformation du système de coordonnées du monde au volume est nécessaire (elle est appelée transformation de rééchantillonnage). Pour transformer tous les autres types de nœuds dans le système de coordonnées du monde, tous les points doivent être transformés dans le système de coordonnées du monde (transformation de modélisation). Étant donné qu'un nœud de transformation doit être applicable à n'importe quel nœud, les nœuds de transformation peuvent fournir à la fois "de" et "vers" le parent (stocker un et calculer l'autre à la volée).

Volume (ou nœud de volume, volume scalaire, image) :  Nœud MRML stockant un tableau 3D de voxels. Les indices du tableau sont généralement désignés sous le nom de IJK. L'étendue des coordonnées IJK est appelée étendue. La géométrie du volume est spécifiée par son origine (position du point IJK=(0,0,0)), son espacement (taille d'un voxel le long des axes I, J, K), les directions des axes (direction des axes I, J, K dans le système de coordonnées de référence) par rapport à un référentiel. Les images 2D sont des volumes 3D à une seule tranche, dont la position et l'orientation sont spécifiées dans l'espace 3D.

Voxel :Un élément d'un volume 3D. Il a une forme de prisme rectangulaire. Les coordonnées d'un voxel correspondent à la position de son point central. La valeur d'un voxel peut être une valeur scalaire simple ou un vecteur.

VR: Abréviation qui peut se référer au rendu de volume ou à la réalité virtuelle. Pour éviter toute ambiguïté, il est généralement recommandé d'utiliser le terme complet (ou de définir explicitement la signification de l'abréviation dans le contexte donné).

VTK (Visualization Toolkit) : Bibliothèque logicielle utilisée par Slicer pour la représentation et la visualisation des données. Étant donné que la plupart des classes Slicer sont dérivées des classes VTK et qu'elles utilisent largement d'autres classes VTK, Slicer a adopté de nombreuses conventions du style et de l'interface de programmation de VTK.

Fenêtre/niveau (ou largeur de fenêtre/niveau de fenêtre): Spécifie la correspondance linéaire des valeurs de voxel à la luminosité d'un pixel affiché. La fenêtre est la plage d'intensité qui est mappée sur la plage d'intensité complète affichable. Le niveau est la valeur du voxel qui est mappée au centre de la plage d'intensité complète affichable.
