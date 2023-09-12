# Pautas de traducción.

El propósito de este documento es darles a los nuevos contribuidores de la comunidad consejos de lo fácil y preciso que es la ayuda en la traducción de la interfaz del software del 3D Slicer en [Weblate](https://hosted.weblate.org/projects/3d-slicer/3d-slicer/).


El trabajo de este documento está en proceso. Siéntase libre de sugerir cambios por [GitHub "solicitud de cambios"](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).


## Comenzar a utilizar Weblate

Weblate es una herramienta colaborativa de traducción para proyectos de código abierto. Con la ayuda de nuestros maravillosos contribuidores, estamos trabajando en conjunto en una traducción completa de la interfaz de 3D Slicer, basándonos principalmente en el esfuerzo de nuestra comunidad. Gracias por acompañarnos.!

Puede encontrar [aquí](https://youtu.be/LSvc9MmrxPA)  un video del tutorial de cómo crear una cuenta de Weblate. 

Si crea una cuenta usando su email y su usuario , recibirá una confirmación de email. Abra el link que contiene el correo de confirmación y siga las instrucciones. 

Es recomendable que use una cuenta de Github para acceder a Weblate. Esto le permitirá a Weblate sincronizar automáticamente sus proyectos asociados con el repositorio de Github. 

Si accedió usando Github, será redirigido a la página de Weblate en donde se le pedirá la confirmación de autorización de Weblate para acceder a la cuenta de Github.  

[Aquí](https://github.com/Slicer/SlicerLanguagePacks/blob/main/HowToUse.md) hay un enlace a un tutorial sobre cómo instalar y configurar el paquete de idiomas de Slicer para habilitar otros idiomas en la aplicación.


**Nota:** Asegúrese de repetir los pasos `Actualizar archivos de traducción` y `Reiniciar la aplicación de vez en cuando` para disponer de las traducciones más recientes y completas, ya que es posible que se hayan traducido nuevos términos desde la última vez que utilizó Slicer.

## Localización de una cadena en la interfaz gráfica de usuario (GUI) de Slicer.

Una cadena específica puede tener muchas apariciones diferentes en la interfaz gráfica de Slicer, a veces incluso en el mismo módulo. La posición y la función de un elemento en la interfaz pueden afectar a su significado y, por tanto, a su traducción. Por lo tanto, es útil conocer estos consejos para identificar exactamente qué elemento de la interfaz está traduciendo Weblate en un determinado momento.

### El indicador "clave"
En la esquina superior derecha de la traducción en Weblate, verá la palabra `Clave` en negrita, seguida de una cadena. Dicha cadena  puede ayudarle a saber aproximadamente (a veces exactamente) en qué modulo o ventana de la GUI se encuentra el término que está traduciendo, como se ilustra continuación.

![](DOCS/key1.png)

![](DOCS/key2.png)

### Buscar cadenas sin traducir

Puede ser aconsejable iniciar la traducción de cadenas con la interfaz de usuario principal de la aplicación. Puede ser aconsejable iniciar la traducción de cadenas con la interfaz de usuario principal de la aplicación. Para ello, introduzca un término de búsqueda que excluya las cadenas de los módulos CLI (módulos de interfaz de línea de comandos): `NOT state:translated AND NOT (key:"CLI_")`

### Cadenas cercanas
Como ya se ha mencionado, es posible que haya varias apariciones de un término en la interfaz del mismo módulo. En ese caso, puede ser útil basarse en los elementos que rodean al que está traduciendo. Weblate empareja cada cadena con una lista de cadenas que se encuentran justo antes o después del elemento en el código de la interfaz gráfica de usuario.

![](DOCS/nearbyStrings.png)

![](DOCS/nearbyStrings2.png)

### "Ubicación de la cadena de origen"
La etiqueta `Ubicación de la cadena fuente o de origen` en Webalte puede ayudarle a ir un nivel más alla y encontrar exactamente qué **línea de código contiene la cadena** que está traduciendo en ese momento. Se encuentra en el cuadro de `Información de cadena` de la parte inferior derecha.

![](DOCS/stringlocation1.png)


![](DOCS/stringlocation2.png)
![](DOCS/stringlocation3.png)

*(la razón por la que los números de línea no coinciden en este ejemplo concreto es que el código se ha actualizado entre el momento en que se cargaron los archivos de traducción y ahora)*

## Traducción de términos

En la compleja interfaz de 3D Slicer, ciertos términos pueden tener significados en contextos muy específicos que pueden perder su precisión si no se traducen con precaución. Localizar la cadena en la interfaz o utilizar el elemento que designa puede ayudar a comprender mejor la definición exacta del término y, por tanto, a traducirlo con la mayor precisión posible. 
Otra forma de garantizar la máxima calidad de la traducción es aprovechar el enfoque comunitario en el que se basa nuestro proceso de internacionalización.

### El botón `Sugerir`
Al traducir una cadena en Weblate, tiene la opción de enviar su traducción e ir al siguiente término, enviar su traducción y quedarse en la misma página o enviar su traducción como una sugerencia.

![](DOCS/suggest1.png) 

 Si elige esta última opción, las diferencias entre su traducción y la actual se resaltan en verde y las partes que sustituyen se tachan y resaltan en rojo, como se muestra a continuación.
 
![](DOCS/suggest2.png) 

La sugerencia puede ser aprobada, editada, o descartada por usted mismo, por algún otro usuario o un corrector asignado.

![](DOCS/suggest3.png) 

Esta opción sirve en caso que no esté seguro de la traducción que envió y le gustaría tomar su tiempo para entenderla mejor antes de confirmar o si le gustaría tener una segunda opinión de otros usuarios.

### La sección de comentarios
Weblate también ofrece la posibilidad de dejar un comentario en la página de traducción de una cadena. De este modo, podrá entablar una conversación con otros participantes en su lengua sobre la interpretación que cada uno tiene del término y, finalmente, acordar un significado y una traducción comunes.

![](DOCS/comments1.png) 

Para asegurarse de que sigue participando en los debates relacionados con el proyecto, puede actualizar su configuración para recibir una notificación cuando se publique un nuevo comentario; y en caso de que las notificaciones le resulten abrumadoras, siempre puede ajustarlas a su medida. Por ejemplo: mientras que un corrector asignado tendría que recibir notificaciones de todas las actualizaciones de los debates, usted puede optar por configurar Weblate para que le notifique sólo los comentarios relacionados con las traducciones que ha enviado o en las que se le menciona.

![](DOCS/comments2.png) 

Puede cambiar la configuración de las notificaciones [aquí.](https://hosted.weblate.org/accounts/profile/#notifications).

### Cadenas intraducibles
Cualquier cadena que empiece por `vtk` o  `MRML` no debe ser traducida y debe ser reportada como error en los informes de errores de Slicer.


**Ejemplo:**

![](DOCS/untranslatable1.png)

También puede etiquetarlos con la bandera de  `solo lectura` (más información sobre las banderas de Weblate [aquí](https://docs.weblate.org/en/latest/admin/checks.html#customizing-behavior-using-flags))

![](DOCS/untranslatable2.png)
![](DOCS/untranslatable3.png)

## Validación de la traducción

Hay muchas maneras para indicar cuando una traducción necesita ser revisada.  Las más utilizadas por nuestros colaboradores son la casilla `Necesita revisión` y la función `Sugerir`.  

![](DOCS/validation1.png)

![](DOCS/validation2.png)

## Estilo

Para tener un estilo constante, es importante que todos los traductores tengan el mismo estilo de lenguaje. Hay Guías de Estilo las cuales están disponibles en el [sitio web de Microsoft](https://www.microsoft.com/en-us/language/StyleGuides). Si los traductores concuerdan en usar la misma guía de estilo, solo necesitan proporcionar un link para descargar esta guía y escriban alguna diferencia que desean hacer a esas guías. 

## Términos del glosario

Algunas palabras en inglés se usan en Slicer con un significado muy específico. Por ejemplo los `volúmenes` se refieren a las imágenes 3D. Algunas de estas palabras se enlistan en el [Glosario de Slicer](https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#glossary).

Al traducir estas palabras a otro idioma, a menudo tiene sentido no traducirlas directamente, sino encontrar una palabra que describa mejor el significado real y traducir esa palabra. Por ejemplo, en lugar de traducir `volumen`, es mejor traducir la palabra `imagen`.

Si encuentra una palabra cuya traducción parece tener sentido a partir de una palabra inglesa diferente, añádala al glosario de weblate haciendo clic en el enlace  `Añadir término al glosario` situado a la derecha de la pantalla y describa qué palabra se ha utilizado añadiéndola a la explicación: `Traducir como "algo""`.
Véase por ejemplo el término `glifo` term: https://hosted.weblate.org/translate/3d-slicer/glossary/en/?checksum=d948d4a61ccd080a

Cada proyecto en Weblate tiene un **glosario** asociado. Se trata de una colección de términos, normalmente de significado complejo o muy específicos del ámbito del proyecto, por lo que requieren una definición extensa y, a veces, precisiones adicionales sobre el significado y el uso de la cadena.Los elementos que figuran en el glosario se vinculan a las cadenas que los contienen, en el componente principal de traducción (cuando una cadena contenga un término del glosario, habrá una referencia al término a la derecha de la interfaz, en un panel denominado `Glosario`). Esto puede ser útil para traducir términos más o menos difíciles de la interfaz.


![](DOCS/glossary1.png)

El panel `Glosario` no contendrá ninguna información en el caso de un término o cadena que no figure en el glosario. Sin embargo, si se hace referencia al término en el glosario, dispondrá de una`traducción` sugerida, asi como de una `explicación` del término. Puede confiar en estos últimos para asegurarse de que comprende mejor el término y, por lo tanto, ofrecerle una traducción lo más exacta posible.

Tenga en cuenta que la `explicación` sólo está disponible en inglés.

Para encontrar una buena traducción de términos informáticos genéricos, puede utilizar la función de [búsqueda terminológica de Microsoft](https://www.microsoft.com/en-us/language/Search).