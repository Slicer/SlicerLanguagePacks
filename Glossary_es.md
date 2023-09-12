### Glosario

Los términos utilizados en diversos campos de la informática médica, biomédica y en imágenes clínicas no siempre son coherentes. En esta sección se definen los términos utilizados habitualmente en 3D Slicer, en particular los que pueden tener significados diferentes en otros contextos.

 **Límites**: describe la caja delimitadora de un objeto espacial a lo largo de 3 ejes. Definido en VTK por 6 valores de coma flotante: X_min, X_max, Y_min, Y_max, Z_min, Z_max.

**Brillo/contraste:**: especifica el mapeo  lineal de los valores de vóxel para el brillo del píxel mostrado. El brillo es la compensación lineal, el contraste es el multiplicador. En la imagen médica, este mapeo lineal es comúnmente especificado por los valores de ventana/nivel. 

**Celdas**: las celdas de datos son elementos topológicos simples de las mallas, como líneas, polígonos o pirámides triangulares, etc. 

**Leyenda de colores (o barra de colores, barra escalar)**: widget superpuesto a las vistas segmentadas o vistas 3D que muestran una leyenda de colores, indicando el significado de los mismos.

**Sistema de coordenadas (o marco de coordenadas, marco de referencia, espacio)**: especificado por la posición del origen, las direcciones de los ejes y la unidad de distancia. Todos los sistemas de coordenadas en 3D Slicer son derechos.

**Extensión (o extensión Slicer)**: una colección de módulos que no forman parte de la aplicación principal, pero que se puede descargar e instalar usando el gestor de extensiones.

**Gestor de extensiones**: un software compuesto por Slicer que permite navegar y desinstalar extensiones en el catálogo de Extensiones (también conocido como la tienda de aplicaciones de Slicer) directamente de la aplicación.

**Índice de extensiones**: un repositorio que contiene la descripción de cada extensión a partir de la cual se construye el catálogo de extensiones

**Extensión**: rango de coordenadas enteras a lo largo de 3 ejes. Definido en VTK por 6 valores, para los ejes IJK: I_min, I_max, J_min, J_max, K_min, K_max. Los valores mínimo y máximo son inclusivos, por lo que el tamaño de una matriz es (I_max - I_min + 1) x (J_max - J_min + 1) x (K_max - K_min + 1).

**Fiducial**: representa un punto en el espacio tridimensional. El término tiene su origen en la cirugía guiada por imagen, en la que se utilizan "marcadores fiduciales" para señalar la posición de los puntos.

**Fotograma**: un punto temporal en una secuencia temporal. Para evitar ambigüedad, este término no se usa para referirse al corte de un volumen.

**Geometría**: especifica la ubicación y la forma de un objeto en el espacio 3D. Ver el término “volumen” para la definición de geometría de la imagen.

**Intensidad de la imagen**: típicamente se refiere al valor de un voxel. El brillo y el color del píxel mostrado se calculan a partir de este valor basándose en la ventana/nivel elegida y la tabla de colores. 

**IJK**: ejes del sistema de coordenadas del vóxel. Los valores de coordenadas enteros corresponden a las posiciones centrales de los vóxeles. Los valores IJK se utilizan a menudo como valores de coordenadas para designar un elemento dentro de una matriz 3D. Por convención VTK denota: I como índice de columna, J índice de fila, K índice  de los cortes. Nótese que numpy utiliza la convención de ordenación opuesta, que son a[K][J][I]. A veces esta disposición de memoria se describe como I siendo el índice que se mueve más rápido y K siendo el que se mueve más lento.

**ITK**: Insight Toolkit. Biblioteca que Slicer utiliza para la mayoría de las operaciones de procesamiento de imágenes.

**Mapas de etiquetas (volumen de mapas de etiquetas, nodo del volumen de mapas de etiquetas)**: nodo de volumen que tiene valores de vóxel determinados (enteros). Normalmente, cada valor corresponde a una estructura o región específica. Esto permite una representación compacta de regiones no superpuestas en una única matriz 3D. La mayoría de los programas utilizan un único mapa de etiquetas para almacenar la corte de una imagen, pero Slicer utiliza un nodo de segmentación específico, que puede contener múltiples representaciones (múltiples labelmaps para permitir el almacenamiento de segmentos superpuestos; representación de superficie cerrada para una rápida visualización en 3D, etc.).  

**LPS (Left-posterior-superior)**: sistema de coordenadas anatómicas izquierda-posterior-superior. Sistema de coordenadas más utilizado en el procesamiento de imágenes médicas. Slicer almacena todos los datos en el sistema de coordenadas LPS en el disco y convierte a/desde RAS (Right-anterior-superior) al escribir o leer del disco.

**Marcadores**: objetos geométricos simples y de medición que el usuario puede colocar en los visores. Los módulos Markups pueden ser usados para crear objetos. Existen varios tipos: lista de puntos, línea, curva, plano, ROI.

**Volumen fuente**: los valores de los vóxeles de este volumen son utilizados durante la segmentación mediante los efectos que se basan en la intensidad de un volumen subyacente.

**MRML (_Medical Reality Markup Language_)**: biblioteca para el almacenamiento, visualización y procesamiento de objetos de información que pueden utilizarse en aplicaciones médicas. La biblioteca está diseñada para ser reutilizable en varias aplicaciones de software, pero 3D Slicer es la única aplicación importante que se sabe que la utiliza.

**Modelo (o nodo de modelo)**: nodo MRML que almacena una malla de superficie (formada por celdas triangulares, poligonales u otras celdas 2D) o una malla volumétrica (formada por celdas tetraédricas, en cuña u otras celdas 3D). 

**Módulo (o módulo de Slicer)**: un módulo Slicer es un componente de software que consta de una interfaz gráfica de usuario (que se muestra en el panel de módulos cuando se selecciona el módulo), una lógica (que implementa algoritmos que operan sobre nodos MRML), y puede proporcionar nuevos tipos de nodos MRML, gestores visualizables (que se encargan de mostrar esos nodos en vistas), extensiones (plugins) de entrada/salida (que se encargan de cargar/guardar nodos MRML en archivos), y otras extensiones diversas. Los módulos suelen ser independientes y sólo se comunican entre sí a través de la modificación de los nodos MRML, pero a veces un módulo utiliza características de otros módulos llamando los métodos en su lógica. 

**Nodo (o Nodo MRML)**: un objeto de datos en la escena. Un nodo puede representar datos (como una imagen o una malla), describir cómo se muestran (color, opacidad, etc.), almacenarse en disco, transformaciones espaciales que se aplican sobre ellos, etc. Existe una jerarquía de clases C+ para definir los comportamientos comunes de los nodos, como la propiedad de ser almacenables en disco o ser transformables geométricamente. La estructura de esta jerarquía de clases puede consultarse en el código o en la documentación de la API (_Application Programming Interface_).

**Cursor**: flecha, caja o marcador con forma humana para mostrar las direcciones de los ejes en las vistas en corte y en 3D.

**RAS (Right-anterior-superior)**: sistema de coordenadas anatómicas derecha-anterior-superior. Sistema de coordenadas utilizado internamente en Slicer. Puede convertirse a/desde el sistema de coordenadas LPS invirtiendo la dirección de los dos primeros ejes.

**Referencia**: no tiene un significado específico, pero normalmente se refiere a una entrada secundaria (objeto de datos, marco de coordenadas, etc.) para una operación.

**Región de interés (ROI)**: especifica una región en forma de caja en 3D. Puede utilizarse para recortar volúmenes, recortar modelos, etc.

**Registro**: proceso de alineación de objetos en el espacio. El resultado del registro es una transformación, que convierte el objeto "móvil" en el objeto "fijo".

**Resolución**: tamaño del vóxel de un volumen, normalmente especificado en mm/píxel. Rara vez se utiliza en la interfaz de usuario porque su significado es ligeramente engañoso: un valor de resolución alto significa un espaciado grande, lo que significa una resolución de imagen mala (baja).

**Regla**: Puede referirse a: 1. Regla de visualización: La línea que se muestra superpuesta en los visores para servir de referencia de tamaño. 2. Línea de marcado: herramienta de medición de distancias.

**Componente escalar**: elemento de un vector. Número de componentes escalares significa la longitud  de un vector.

**Valor escalar**: un número real. Normalmente de punto flotante. 

**Escena (o escena MRML)**: es la estructura de datos que contiene todos los datos que se cargan actualmente en la aplicación e información adicional sobre cómo deben visualizarse o utilizarse. El término tiene su origen en los gráficos de ordenador.

**Segmento**: corresponde a una única estructura en una segmentación. Consulte más información en la sección Segmentación de imágenes. 

**Segmentación (también conocida como contorneado, anotación; región de interés, conjunto de estructuras, máscara)**: proceso de delineación de estructuras 3D en imágenes. La segmentación también puede referirse al nodo MRML que es el resultado del proceso de segmentación. Un nodo de segmentación suele contener varios segmentos (cada segmento corresponde a una estructura 3D). Los nodos de segmentación no son nodos labelmap ni nodos modelo, pero pueden almacenar múltiples representaciones (labelmap binario, superficie cerrada, etc.). Consulte más información en la sección Segmentación de imágenes.


**Corte (Slice)**: intersección de un objeto 3D con un plano

**Anotaciones en las vistas de corte**: es el texto que se muestra en las esquinas de las vistas de cortes desplegando el nombre y las etiquetas DICOM seleccionadas de los volúmenes mostrados.

**Espaciado**: tamaño del vóxel de un volumen, normalmente especificado en mm/pixel. 

**Transformar (o transformación)**: puede convertir cualquier objeto 3D de un sistema de coordenadas a otro. El tipo más común es la transformación rígida, que puede cambiar la posición y orientación de un objeto. Las transformaciones lineales pueden escalar, reflejar o deformar objetos. Las transformaciones no lineales pueden deformar arbitrariamente el espacio 3D. Para mostrar un volumen en el sistema de coordenadas globales, el volumen debe remuestrearse, por lo que se necesita una transformación del sistema de coordenadas globales al volumen necesario (se denomina transformación de remuestreo). Para transformar todos los demás tipos de nodos al sistema de coordenadas globales, todos los puntos deben transformarse al mismo (modelado de transformación). Dado que un nodo de transformación debe ser aplicable a cualquier otro, ambos pueden proporcionar información tanto de origen como de destino para la matriz (almacenar uno y calcular el otro sobre la marcha).


**Volumen (o nodo de volumen, volumen escalar, imagen)**: nodo MRML que almacena una matriz 3D de vóxeles. Los índices de la matriz suelen denominarse IJK. El rango de coordenadas IJK se denomina extensión. La geometría del volumen viene especificada por su origen (posición del punto IJK=(0,0,0)), espaciado (tamaño de un vóxel a lo largo de los ejes I, J, K), direcciones de los ejes (dirección de los ejes I, J, K en el sistema de coordenadas de referencia) con respecto a un marco de referencia. Las imágenes 2D son volúmenes 3D de un solo corte, con su posición y orientación especificadas en el espacio 3D.


**Vóxel**: un elemento de volumen 3D. Tiene forma de prisma rectangular. Las coordenadas del vóxel corresponden a la posición del punto central. El valor del vóxel puede ser un valor escalar  o un vector. 

**RV**: abreviatura que puede referirse al renderizado de volúmenes o a la realidad virtual. Para evitar ambigüedades, suele recomendarse utilizar el término completo (o definir explícitamente el significado de la abreviatura en el contexto dado).


**VTK (_Visualization Toolkit_)**: es una biblioteca que Slicer utiliza para la representación y visualización de datos. Dado que la mayoría de las clases de Slicer derivan de clases VTK y usan en gran medida otras clases VTK, Slicer adoptó muchas convenciones del estilo y la interfaz de programación de aplicaciones de VTK.

**Ventana/nivel (o ancho de ventana/nivel de ventana)**: especifica el mapeo lineal de los valores de vóxel para la luminosidad de un píxel visualizado. La ventana es el tamaño del rango de intensidad que se asigna a todo el campo de intensidad visible. El nivel es el valor del vóxel que se asigna al centro de todo el rango de intensidad visible.
