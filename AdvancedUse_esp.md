## Sugerencias y trucos

### Herramienta de búsqueda de texto

Se ha añadido la herramienta `Buscar texto` para extraer rápidamente el texto de la aplicación y encontrar las apariciones de ese texto en el sitio web de traducción:

- Ir al módulo Herramienta de idiomas
- Abra la sección  `Buscar texto` 
- Establecer idioma editado: las cadenas extraídas se abrirán en el sitio web, mostrando las traducciones en este idioma. Ejemplo: `es-419`.
- Marque la casilla `Activar buscador de texto` 
- Pulse `Ctrl+6` en cualquier momento para mostrar el selector de widgets. 
- Haga click en el widget que contenga texto traducible (pulse cualquier tecla para cancelar la selección del widget).
- Haga click en `Aceptar` para abrir el texto encontrado en el sitio web de traducción. 

![](Docs/FindText.png)

Sobre las restricciones:
- La herramienta sólo extrae widgets de Qt (no de vistas renderizadas por la librería VTK).
- La extracción de texto de ventanas flotantes y emergentes no está disponible.

### Traducción de links externos

Si el texto traducido tiene links externos de sitios que contienen múltiples idiomas, en general, es preferible no codificar un idioma específico (para permitir que el sitio externo utilice su propio idioma preferido). Por ejemplo: es mejor  <https://docs.github.com/get-started/quickstart/fork-a-repo> es mejor (en lugar de agregar `/en` como en el siguiente link: <https://docs.github.com/en/get-started/quickstart/fork-a-repo>).

Sin embargo, no todos los sitios automáticamente pueden cargar el lenguaje elegido. Por ejemplo, [ReadTheDocs](https://readthedocs.org) requiere explícitamente el código URL específico del lenguaje: <https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/import_process.html> es valido, pero <https://docs.godotengine.org/stable/tutorials/assets_pipeline/import_process.html> es una URL inválida. En estos casos, la URL del enlace debe cambiarse en cada traduccion para que coincida con el idioma de destino.

Véase la conversación relacionada [aquí](https://github.com/Slicer/Slicer/pull/6401#discussion_r884768951).

## Uso avanzado

### Instale los archivos de traducción sin conexión a internet

Los archivos de traducción (.ts) pueden descargarse en el folder e instalarse de ahi más tarde, sin necesidad de conexión a internet.

Los archivos traducidos pueden descargarse de Weblate o Github. Por ejemplo, Abra un [proyecto Slicer en la sección](https://hosted.weblate.org/project/3d-slicer) de la pagina traducida en Weblate (como 
[Español](https://hosted.weblate.org/projects/3d-slicer/3d-slicer/es-419/)), Luego en el menú vaya a  `Archivos` -> `Descargar traducción`.

Instale los archivos traducidos:
- Seleccione la opción del`Folder Local` 
- Establezca la carpeta que contiene los archivos .ts en `Carpeta de entrada` en la sección `Traducciones de entrada`.
- Marque la opción  `Sólo el ultimo archivo` para utilizar unicamente el ultimo archivo .ts descargado. Es útil si la carpeta local se establece directamente en la carpeta de descarga del navegador web.
- Compile los archivos de traducción e instalelos en la aplicación haciendo click en el botón   `Actualizar archivos de traducción`.
