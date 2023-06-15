# Guía para desarrolladores del módulo Slicer

Estas instrucciones son para desarrolladores del módulo de Slicer (en el núcleo de Slicer o en las extensiones de Slicer) quien quiera hacer que sus módulos sean traducibles

## Preparación de archivos .ui para traducción

Por defecto, la mayoría de las propiedades de cadenas y lista de cadenas que aparecen en los archivos .ui están disponibles para su traducción. Este suele ser el comportamiento correcto, pero en algunos casos las cadenas contienen cadenas que no deben traducirse y no deben aparecer en los archivos fuente de traducción (.ts).

Propiedades que **deben marcarse como no traducibles en Qt designer** desmarcando la opción `Translatable`, a menos que se establezcan a su valor por defecto (normalmente vacío):


- En widgets selectores de nodos, como qMRMLNodeComboBox, qMRMLCheckableNodeComboBox, qMRMLSubjectHierarchyTreeView, qMRMLTreeView:
  - `nodeTypes`
  - `hideChildNodeTypes`
  - `interactionNodeSingletonTag` (si no es el valor predeterminado "Singleton")
  - `sceneModelType`
  - `levelFilter`
- En widgets  MRML (qMRML...Widget) que admiten cantidades, como qMRMLRangeWidget o qMRMLCoordinatesWidget:
  - `Cantidad`
- En widgets que guardan datos en la configuración de la aplicación, como ctkPathLineEdit, qMRMLSegmentationFileExportWidget, qMRMLSegmentEditorWidget:
  - `settingKey`
  - `defaultTerminologyEntrySettingsKey`
- En widgets que guardan datos en atributos de jerarquia de nodos o materias, como qMRMLSubjectHierarchyComboBox, SubjectHierarchyTreeView:
  - `includeItemAttributeNamesFilter`
  - `excludeItemAttributeNamesFilter`
  - `includeNodeAttributeNamesFilter`
  - `excludeNodeAttributeNamesFilter`
- En widgets de vista de corte, como qMRMLSliceControllerWidget y qMRMLSliceWidget:
  - `sliceViewName`
  - `sliceOrientation`
- En qMRMLSegmentationConversionParametersWidget:
  - `targetRepresentationName`
- En qSlicerMouseModeToolBar:
  - `defaultPlaceClassName`

![](Docs/DesignerMarkAsNonTranslatable.png)

## Utilizar correctamente la función de traducción

Siempre que su programa utilice una cadena literal (texto entrecomillado) que se mostrará en la interfaz de usuario, asegúrese de que sea procesada por la [*Función de traducción*](https://doc.qt.io/qt-5/i18n-source-translation.html#using-tr-for-all-literal-text). En los códigos fuente, `tr()` se utiliza para marcar cadenas traducibles de modo que, al ejecutarse, `Qt` pueda sustituirlas por su versión traducida correspondiente al idioma de visualización.

En el proceso de traducción, es importante saber llamar correctamente a `tr()`ya que determina el contexto que se asociará a cualquier cadena cuando vaya a traducirla.

Por ello, en el proceso de internacionalización de Slicer 
se han mantenido algunas recomendaciones sobre cómo utilizar correctamente la función de traducción. Dichas pautas se describen en las secciones siguiente
.

### Cómo utilizar *tr()* en las clases QObject

Dentro de una clase que hereda de QObject, tanto si esta herencia es directa como si no, todo lo que hay que hacer es utilizar la función [tr()](https://doc.qt.io/qt-5/qobject.html#tr) para obtener el texto traducido de sus clases.

```c++
LoginWidget::LoginWidget()
{
    QLabel *label = new QLabel(tr("Password:"));
    ...
}
````
Las clases que heredan de QObject deben añadir la macro [Q_OBJECT](https://doc.qt.io/qt-5/i18n-source-translation.html#defining-a-translation-context) en su definición para que el contexto de traducción sea manejado correctamente por `Qt`.
```c++
class MainWindow : public QMainWindow
{
    Q_OBJECT

    public:
        MainWindow();
        ...
```

> **_NOTA:_**  Para evitar errores con algunas herramientas de compilación (p.e. cmake), se recomienda declarar siempre las clases con la macro Q_OBJECT en el archivo de cabecera (.h), no en el de implementación (.cpp). Si por alguna razón tu clase QObject debe ser declarada en el archivo .cpp (**p.e.** clases de implementación de bajo nivel), recomendamos no añadir la macro Q_OBJECT a esa clase, sino prefijar todas las llamadas a  `tr()` con la clase pública asociada como sigue: `PublicClassName::tr("text to translate")`

### Cómo utilizar *tr ()* en clases que no son QObject

Las clases que no son QObject no tienen una función de traducción, por lo que  QObject llamar directamente a `tr()` sobre ellas puede dar lugar a errores.

Una práctica común es  llamar con prefijos a `tr()`  en estas con una clase del núcleo de `QObject::tr()`, `QLabel::tr()`, etc. Sin embargo, no le recomendamos este enfoque, ya que `lupdate` asociará dichas cadenas traducibles a un contexto diferente de la clase en la que se encuentran.
Por lo tanto, cuando se trate de traducir clases que no sean Qt, le recomendamos proporcionar soporte de traducción a la clase añadiendo directamente la macro [Q_DECLARE_TR_FUNCTIONS](https://doc.qt.io/qt-5/i18n-source-translation.html#translating-non-qt-classes) sobre ella.
```c++
class MyClass
{
    Q_DECLARE_TR_FUNCTIONS(MyClass)

    public:
        MyClass();
        ...
};
```
Al hacerlo, la clase dispondrá de la función `tr()`, que puede utilizarse directamente para traducir las cadenas asociadas a la clase, y hará posible que `lupdate` to find translatable strings in the source code.

>**NOTA:** Si por alguna razón el nombre de la clase no debe ser expuesto a otros desarrolladores o traductores (clases privadas, ...), recomendamos prefijar las llamadas a `tr()` con la clase pública asociada como sigue:  `PublicClassName::tr("text to translate")`

### Traducir cadenas multilínea 

Las cadenas largas pueden definirse en varias líneas de esta forma:

```
QString help = QString(
  "Volume Rendering Module provides advanced tools for toggling interactive "
  "volume rendering of datasets."
  );
```

Traduzca este tipo de cadenas multilínea utilizando una función `tr()` como ésta para que los traductores puedan traducir oraciones completas:

```
QString help = tr(
  "Volume Rendering Module provides advanced tools for toggling interactive "
  "volume rendering of datasets."
  );
```

No traducir así, ya que las cadenas traducibles contendrían fragmentos de frases: 

```
// ¡ESTO ESTÁ MAL!
QString help =
  tr("Volume Rendering Module provides advanced tools for toggling interactive ") +
  tr("volume rendering of datasets.<br/>");
```

### Traducir los atajos de teclado

De acuerdo con las [recomendaciones Qt](https://doc.qt.io/qt-6/qkeysequence.html#keyboard-layout-issues), los atajos de teclado deben especificarse utilizando cadenas traducibles para poder adaptarse mejor a las diferentes configuraciones de teclado utilizadas habitualmente para un idioma específico.

Ejemplos:

```c++
this->RunFileAction->setShortcut(QKeySequence::Print);  // es mejor opción (si hay disponible una secuencia de teclas estándar)
this->RunFileAction->setShortcut(ctkConsole::tr("Ctrl+g"));  // opción preferida, si una secuencia de teclas estándar no está disponible
this->RunFileAction->setShortcut("Ctrl+g");  // no usar esta forma
this->RunFileAction->setShortcut(Qt::CTRL | Qt::Key_G);  // no usar esta forma
```

### Traducir el título del módulo

El título del módulo (el nombre que es visible en el selector de módulo) es devuelto por la clase de módulo y debe ser traducido.

En los antiguos módulos cargables C++, el nombre del módulo se establecía en CMakeLists.txt mediante una macro y se establecía en el archivo de cabecera del módulo mediante la definición del precompilado `QTMODULE_TITLE`  Para hacer traducible el título del módulo cargable en C++ (ver ejemplo [aqui](https://github.com/Slicer/Slicer/commit/3f05bc595f25c49b0b213c6b116eebec595e03b2)):
- Eliminar las lineas `set(MODULE_TITLE ${MODULE_NAME})` y `TITLE ${MODULE_TITLE}` de `CMakeLists.txt`
- Usar `tr("qSlicerLoadableModuleTemplateModule")` en `qSlicerGetTitleMacro()` en el archivo de cabecera del módulo

### Advertencias comunes de lupdate Qt

Si las llamadas a `tr()` no se gestionan correctamente en el código fuente, pueden aparecer algunas advertencias al ejecutar `lupdate`.

#### No se puede ejecutar tr() de esta forma

La herramienta lupdate de Qt lanza el aviso  `Cannot invoke tr() like this` cuando se 
llama a la función de traducción utilizando un objeto como `q->tr(...)`. El problema es que lupdate no puede determinar el nombre de la clase sobre la que se llama a `tr()` y por tanto no conoce el contexto de traducción. 

Este problema puede resolverse escribiendo el nombre de la clase en la llamada, por ejemplo `qSlicerScalarVolumeDisplayWidget::tr(...)`, como se describe en las secciones anteriores.

#### La clase  _'SomeClassName'_  carece de la macro Q_OBJECT 

La herramienta lupdate de Qt lanza el aviso  `Class 'SomeClassName' macro` cuando se llama a la función de traducción en una clase QObject sin macro Q_OBJECT en su definición. El problema es también que `lupdate` no puede determinar el nombre de la clase sobre la que se llama a `tr()` y por ello desconoce el contexto de traducción.


La solución es añadir la macro `Q_OBJECT` en la clase donde se llama a `tr()` o, en caso de clases que no deban ser expuestas (clases privadas, clases de implementación de bajo nivel, ...), prefijar las llamadas a `tr()` con la clase pública asociada, tal y como se ha descrito en los apartados anteriores.

## Identificación de cadenas traducibles

En el proceso de traducción, sólo deben tenerse en cuenta las cadenas que se muestran a nivel de interfaz de usuario. Por lo que, las cadenas que hacen referencia a nombres de módulos, contenidos de archivos, extensiones de archivos, comunicaciones de desarrollador como mensajes de registro (p.e. Salidas `PrintSelf` o `qCritical`) o cualquier contenido relacionado con el desarrollador, deben considerarse como no traducibles.

Para dejar claro que una cadena no debe traducirse, puede añadirse el comentario, `/*no tr*/` a una cadena para indicar que la función `tr()` no se utiliza intencionadamente.

## Uso de clases base comunes para cadenas compartidas

Para evitar la duplicación de cadenas de origen, se debe utilizar un método `tr()` de una clase base común para las siguientes cadenas:
- Los nombres de las categorías de los módulos  (`Informática`, `Registro`, `Segmentación`, ...) deben traducirse utilizando  `qSlicerAbstractCoreModule::tr()`

## Extraer cadenas traducibles

La herramienta lupdate de Qt permite extraer cadenas traducibles del código fuente y combinarlas con los archivos de traducción existentes. Se realizan pasos adicionales para extraer la secuencia de comandos traducible de la descripción XML de los módulos CLI y de los archivos Python, y también se da soporte a muchos idiomas. Por lo tanto, se crea un script de Python que puede realizar todos los pasos de procesamiento: [update_translations.py]([url](https://github.com/Slicer/Slicer/blob/main/Utilities/Scripts/update_translations.py)).

### Cómo actualizar cadenas traducibles

#### requisitos previos
- Clonar el repositorio https://github.com/Slicer/SlicerLanguageTranslations 
- Clonar el repositorio https://github.com/Slicer/Slicer 
- Instalar Qt-6.3 o posterior (las versiones anteriores no tienen lupdate que pueda extraer cadenas del código Python)
- Instalar Python-3.9 o posterior

#### Actualizar los archivos fuente de la traducción
- Asegúrese de que todos los pull requests en el repositorio enviados por Weblate están fusionados (para evitar conflictos de fusión). Si se esperan cambios en el repositorio (por ejemplo, debido a actualizaciones recientes), puede que convenga esperar hasta que esos cambios se hayan completado. También es posible bloquear temporalmente Weblate para que no acepte ninguna modificación mientras realizamos los pasos siguientes.
- Asegúrese de que el repositorio clonado está actualizado y no hay archivos modificados localmente. (para evitar conflictos de fusión y evitar que contenido obsoleto llegue a los archivos fuente de traducción)
- Ejecute estos comandos:

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
# Guía para desarrolladores del módulo Slicer

Estas instrucciones son para desarrolladores del módulo de Slicer (en el núcleo de Slicer o en las extensiones de Slicer) quien quiera hacer que sus módulos sean traducibles

## Preparación de archivos .ui para traducción

Por defecto, la mayoría de las propiedades de cadenas y lista de cadenas que aparecen en los archivos .ui están disponibles para su traducción. Este suele ser el comportamiento correcto, pero en algunos casos las cadenas contienen cadenas que no deben traducirse y no deben aparecer en los archivos fuente de traducción (.ts).

Propiedades que **deben marcarse como no traducibles en Qt designer** desmarcando la opción `Translatable`, a menos que se establezcan a su valor por defecto (normalmente vacío):


- En widgets selectores de nodos, como qMRMLNodeComboBox, qMRMLCheckableNodeComboBox, qMRMLSubjectHierarchyTreeView, qMRMLTreeView:
  - `nodeTypes`
  - `hideChildNodeTypes`
  - `interactionNodeSingletonTag` (si no es el valor predeterminado "Singleton")
  - `sceneModelType`
  - `levelFilter`
- En widgets  MRML (qMRML...Widget) que admiten cantidades, como qMRMLRangeWidget o qMRMLCoordinatesWidget:
  - `Cantidad`
- En widgets que guardan datos en la configuración de la aplicación, como ctkPathLineEdit, qMRMLSegmentationFileExportWidget, qMRMLSegmentEditorWidget:
  - `settingKey`
  - `defaultTerminologyEntrySettingsKey`
- En widgets que guardan datos en atributos de jerarquia de nodos o materias, como qMRMLSubjectHierarchyComboBox, SubjectHierarchyTreeView:
  - `includeItemAttributeNamesFilter`
  - `excludeItemAttributeNamesFilter`
  - `includeNodeAttributeNamesFilter`
  - `excludeNodeAttributeNamesFilter`
- En widgets de vista de corte, como qMRMLSliceControllerWidget y qMRMLSliceWidget:
  - `sliceViewName`
  - `sliceOrientation`
- En qMRMLSegmentationConversionParametersWidget:
  - `targetRepresentationName`
- En qSlicerMouseModeToolBar:
  - `defaultPlaceClassName`

![](Docs/DesignerMarkAsNonTranslatable.png)

## Utilizar correctamente la función de traducción

Siempre que su programa utilice una cadena literal (texto entrecomillado) que se mostrará en la interfaz de usuario, asegúrese de que sea procesada por la [*Función de traducción*](https://doc.qt.io/qt-5/i18n-source-translation.html#using-tr-for-all-literal-text). En los códigos fuente, `tr()` se utiliza para marcar cadenas traducibles de modo que, al ejecutarse, `Qt` pueda sustituirlas por su versión traducida correspondiente al idioma de visualización.

En el proceso de traducción, es importante saber llamar correctamente a `tr()`ya que determina el contexto que se asociará a cualquier cadena cuando vaya a traducirla.

Por ello, en el proceso de internacionalización de Slicer 
se han mantenido algunas recomendaciones sobre cómo utilizar correctamente la función de traducción. Dichas pautas se describen en las secciones siguiente
.

### Cómo utilizar *tr()* en las clases QObject

Dentro de una clase que hereda de QObject, tanto si esta herencia es directa como si no, todo lo que hay que hacer es utilizar la función [tr()](https://doc.qt.io/qt-5/qobject.html#tr) para obtener el texto traducido de sus clases.

```c++
LoginWidget::LoginWidget()
{
    QLabel *label = new QLabel(tr("Password:"));
    ...
}
````
Las clases que heredan de QObject deben añadir la macro [Q_OBJECT](https://doc.qt.io/qt-5/i18n-source-translation.html#defining-a-translation-context) en su definición para que el contexto de traducción sea manejado correctamente por `Qt`.
```c++
class MainWindow : public QMainWindow
{
    Q_OBJECT

    public:
        MainWindow();
        ...
```

> **_NOTA:_**  Para evitar errores con algunas herramientas de compilación (p.e. cmake), se recomienda declarar siempre las clases con la macro Q_OBJECT en el archivo de cabecera (.h), no en el de implementación (.cpp). Si por alguna razón tu clase QObject debe ser declarada en el archivo .cpp (**p.e.** clases de implementación de bajo nivel), recomendamos no añadir la macro Q_OBJECT a esa clase, sino prefijar todas las llamadas a  `tr()` con la clase pública asociada como sigue: `PublicClassName::tr("text to translate")`

### Cómo utilizar *tr ()* en clases que no son QObject

Las clases que no son QObject no tienen una función de traducción, por lo que  QObject llamar directamente a `tr()` sobre ellas puede dar lugar a errores.

Una práctica común es  llamar con prefijos a `tr()`  en estas con una clase del núcleo de `QObject::tr()`, `QLabel::tr()`, etc. Sin embargo, no le recomendamos este enfoque, ya que `lupdate` asociará dichas cadenas traducibles a un contexto diferente de la clase en la que se encuentran.
Por lo tanto, cuando se trate de traducir clases que no sean Qt, le recomendamos proporcionar soporte de traducción a la clase añadiendo directamente la macro [Q_DECLARE_TR_FUNCTIONS](https://doc.qt.io/qt-5/i18n-source-translation.html#translating-non-qt-classes) sobre ella.
```c++
class MyClass
{
    Q_DECLARE_TR_FUNCTIONS(MyClass)

    public:
        MyClass();
        ...
};
```
Al hacerlo, la clase dispondrá de la función `tr()`, que puede utilizarse directamente para traducir las cadenas asociadas a la clase, y hará posible que `lupdate` to find translatable strings in the source code.

>**NOTA:** Si por alguna razón el nombre de la clase no debe ser expuesto a otros desarrolladores o traductores (clases privadas, ...), recomendamos prefijar las llamadas a `tr()` con la clase pública asociada como sigue:  `PublicClassName::tr("text to translate")`

### Traducir cadenas multilínea 

Las cadenas largas pueden definirse en varias líneas de esta forma:

```
QString help = QString(
  "Volume Rendering Module provides advanced tools for toggling interactive "
  "volume rendering of datasets."
  );
```

Traduzca este tipo de cadenas multilínea utilizando una función `tr()` como ésta para que los traductores puedan traducir oraciones completas:

```
QString help = tr(
  "Volume Rendering Module provides advanced tools for toggling interactive "
  "volume rendering of datasets."
  );
```

No traducir así, ya que las cadenas traducibles contendrían fragmentos de frases: 

```
// ¡ESTO ESTÁ MAL!
QString help =
  tr("Volume Rendering Module provides advanced tools for toggling interactive ") +
  tr("volume rendering of datasets.<br/>");
```

### Traducir los atajos de teclado

De acuerdo con las [recomendaciones Qt](https://doc.qt.io/qt-6/qkeysequence.html#keyboard-layout-issues), los atajos de teclado deben especificarse utilizando cadenas traducibles para poder adaptarse mejor a las diferentes configuraciones de teclado utilizadas habitualmente para un idioma específico.

Ejemplos:

```c++
this->RunFileAction->setShortcut(QKeySequence::Print);  // es mejor opción (si hay disponible una secuencia de teclas estándar)
this->RunFileAction->setShortcut(ctkConsole::tr("Ctrl+g"));  // opción preferida, si una secuencia de teclas estándar no está disponible
this->RunFileAction->setShortcut("Ctrl+g");  // no usar esta forma
this->RunFileAction->setShortcut(Qt::CTRL | Qt::Key_G);  // no usar esta forma
```

### Traducir el título del módulo

El título del módulo (el nombre que es visible en el selector de módulo) es devuelto por la clase de módulo y debe ser traducido.

En los antiguos módulos cargables C++, el nombre del módulo se establecía en CMakeLists.txt mediante una macro y se establecía en el archivo de cabecera del módulo mediante la definición del precompilado `QTMODULE_TITLE`  Para hacer traducible el título del módulo cargable en C++ (ver ejemplo [aqui](https://github.com/Slicer/Slicer/commit/3f05bc595f25c49b0b213c6b116eebec595e03b2)):
- Eliminar las lineas `set(MODULE_TITLE ${MODULE_NAME})` y `TITLE ${MODULE_TITLE}` de `CMakeLists.txt`
- Usar `tr("qSlicerLoadableModuleTemplateModule")` en `qSlicerGetTitleMacro()` en el archivo de cabecera del módulo

### Advertencias comunes de lupdate Qt

Si las llamadas a `tr()` no se gestionan correctamente en el código fuente, pueden aparecer algunas advertencias al ejecutar `lupdate`.

#### No se puede ejecutar tr() de esta forma

La herramienta lupdate de Qt lanza el aviso  `Cannot invoke tr() like this` cuando se 
llama a la función de traducción utilizando un objeto como `q->tr(...)`. El problema es que lupdate no puede determinar el nombre de la clase sobre la que se llama a `tr()` y por tanto no conoce el contexto de traducción. 

Este problema puede resolverse escribiendo el nombre de la clase en la llamada, por ejemplo `qSlicerScalarVolumeDisplayWidget::tr(...)`, como se describe en las secciones anteriores.

#### La clase  _'SomeClassName'_  carece de la macro Q_OBJECT 

La herramienta lupdate de Qt lanza el aviso  `Class 'SomeClassName' macro` cuando se llama a la función de traducción en una clase QObject sin macro Q_OBJECT en su definición. El problema es también que `lupdate` no puede determinar el nombre de la clase sobre la que se llama a `tr()` y por ello desconoce el contexto de traducción.


La solución es añadir la macro `Q_OBJECT` en la clase donde se llama a `tr()` o, en caso de clases que no deban ser expuestas (clases privadas, clases de implementación de bajo nivel, ...), prefijar las llamadas a `tr()` con la clase pública asociada, tal y como se ha descrito en los apartados anteriores.

## Identificación de cadenas traducibles

En el proceso de traducción, sólo deben tenerse en cuenta las cadenas que se muestran a nivel de interfaz de usuario. Por lo que, las cadenas que hacen referencia a nombres de módulos, contenidos de archivos, extensiones de archivos, comunicaciones de desarrollador como mensajes de registro (p.e. Salidas `PrintSelf` o `qCritical`) o cualquier contenido relacionado con el desarrollador, deben considerarse como no traducibles.

Para dejar claro que una cadena no debe traducirse, puede añadirse el comentario, `/*no tr*/` a una cadena para indicar que la función `tr()` no se utiliza intencionadamente.

## Uso de clases base comunes para cadenas compartidas

Para evitar la duplicación de cadenas de origen, se debe utilizar un método `tr()` de una clase base común para las siguientes cadenas:
- Los nombres de las categorías de los módulos  (`Informática`, `Registro`, `Segmentación`, ...) deben traducirse utilizando  `qSlicerAbstractCoreModule::tr()`

## Extraer cadenas traducibles

La herramienta lupdate de Qt permite extraer cadenas traducibles del código fuente y combinarlas con los archivos de traducción existentes. Se realizan pasos adicionales para extraer la secuencia de comandos traducible de la descripción XML de los módulos CLI y de los archivos Python, y también se da soporte a muchos idiomas. Por lo tanto, se crea un script de Python que puede realizar todos los pasos de procesamiento: [update_translations.py]([url](https://github.com/Slicer/Slicer/blob/main/Utilities/Scripts/update_translations.py)).

### Cómo actualizar cadenas traducibles

#### requisitos previos
- Clonar el repositorio https://github.com/Slicer/SlicerLanguageTranslations 
- Clonar el repositorio https://github.com/Slicer/Slicer 
- Instalar Qt-6.3 o posterior (las versiones anteriores no tienen lupdate que pueda extraer cadenas del código Python)
- Instalar Python-3.9 o posterior

#### Actualizar los archivos fuente de la traducción
- Asegúrese de que todos los pull requests en el repositorio enviados por Weblate están fusionados (para evitar conflictos de fusión). Si se esperan cambios en el repositorio (por ejemplo, debido a actualizaciones recientes), puede que convenga esperar hasta que esos cambios se hayan completado. También es posible bloquear temporalmente Weblate para que no acepte ninguna modificación mientras realizamos los pasos siguientes.
- Asegúrese de que el repositorio clonado está actualizado y no hay archivos modificados localmente. (para evitar conflictos de fusión y evitar que contenido obsoleto llegue a los archivos fuente de traducción)
- Ejecute estos comandos:

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
