Glossário

Os termos utilizados em vários domínios da computação de imagens médicas e biomédicas e de imagens clínicas nem sempre são consistentes. Esta seção define os termos que são habitualmente utilizados no 3D Slicer, especialmente aqueles que podem ter um significado diferente em outros contextos.

Limites: Descreve a caixa delimitadora de um objeto espacial ao longo de 3 eixos. Definido no VTK por 6 valores de ponto flutuantes: X_mín., X_máx., Y_mín., Y_máx., Z_mín., Z_máx.

Brilho/contraste: Especifica o mapeamento linear dos valores de vóxel para o brilho de um pixel apresentado. O brilho é o desvio linear; já o contraste é o multiplicador. Na imagiologia médica, este mapeamento linear é mais frequentemente especificado por valores de janela/nível.

Célula: As células de dados são elementos topológicos simples de malhas, tais como linhas, polígonos, tetraedros etc.

Legenda de cores (ou barra de cores, barra de escalas): um widget sobreposto em fatias ou em 3D que apresenta uma legenda de cores, indicando o significado das cores.

Sistema de coordenadas (ou quadro de coordenadas, quadro de referência, espaço): Especifica-se pela posição de origem, pelas direções de eixo e pela unidade de distância. Todos os sistemas de coordenadas no 3D Slicer são destros.

Extensão (ou extensão do Slicer): Uma coleção de módulos que não está incluída na aplicação principal, mas que pode ser transferida e instalada por meio do gestor de extensões.

Gestor de extensões: Um componente de software do Slicer que permite navegar, instalar e desinstalar extensões no catálogo de extensões (também conhecido como loja de aplicativos do Slicer) diretamente do aplicativo.

Índice de extensões: Um repositório que contém a descrição de cada extensão a partir da qual o catálogo de extensões é criado.

Extensão: Gama de coordenadas de números inteiros ao longo de 3 eixos. Definida em VTK por 6 valores, para os eixos IJK: I_mín., I_máx., J_mín., J_máx., K_mín., K_máx. Os valores mínimos e máximos são inclusivos, pelo que o tamanho de uma matriz é (I_máx - I_mín + 1) x (J_máx - J_mín + 1) x (K_máx - K_mín + 1).

Fiducial: Representa um ponto no espaço 3D. O termo tem origem na cirurgia guiada por imagem, em que são utilizados “marcadores fiduciais” para marcar as posições dos pontos.

Quadro: Um ponto de tempo numa sequência temporal. Para evitar ambiguidades, este termo não é utilizado para se referir a uma fatia de um volume.

Geometria: Especifica a localização e a forma de um objeto no espaço 3D. Ver o termo “Volume” para a definição de geometria da imagem.

Intensidade da imagem: Normalmente, refere-se ao valor de um vóxel. Calculam-se o brilho e a cor do pixel apresentado a partir desse valor, baseado na janela ou no nível escolhido e na tabela de pesquisa de cores.

IJK: Eixos do sistema de coordenadas do vóxel. Os valores de coordenadas de número inteiro correspondem às posições centrais do vóxel. Os valores IJK são frequentemente utilizados como valores de coordenadas para designar um elemento dentro de uma matriz 3D. Por convenção VTK: I indexa a coluna; J indexa a linha; K indexa a fatia. Note-se que o NumPy utiliza a convenção de ordenação oposta, em que: [K][J][I]. Por vezes, descreve-se esse layout de memória como sendo I o índice que se move mais rapidamente e K o que se move mais lentamente.

ITK: Insight Toolkit. Biblioteca de software que o Slicer utiliza para a maioria das operações de processamento de imagens.

Mapa de rótulos (ou volume de mapa de rótulos, nó de volume de mapa de rótulos): Nó de volume que tem valores de vóxel discretos (inteiros). Normalmente, cada valor corresponde a uma estrutura ou região específica. Isso permite a representação compacta de regiões não sobrepostas numa única matriz 3D. A maior parte do software usa um único mapa de rótulos para armazenar uma segmentação de imagem, mas o Slicer usa um nó de segmentação dedicado, que pode conter várias representações (vários mapas de rótulos para permitir o armazenamento de segmentos sobrepostos; representação de superfície fechada para uma visualização 3D rápida etc.).

LPS: Sistema de coordenadas anatômicas esquerdo-posterior-superior. Sistema de coordenadas mais utilizado na computação de imagens médicas. O Slicer armazena todos os dados no sistema de coordenadas LPS no disco (e converte-os de/para RAS ao escrever ou ler em um disco).

Marcações: Objetos geométricos simples e medidas que o usuário pode colocar nos visualizadores. O módulo de marcações pode ser utilizado para criar tais objetos. Existem vários tipos, tais como lista de pontos, linha, curva, plano, ROI.

Volume de origem: Os valores de vóxel desse volume são utilizados durante a segmentação pelos efeitos que dependem da intensidade de um volume subjacente.

MRML: Medical Reality Markup Language - Linguagem de Marcação da Realidade Médica: Biblioteca de software para armazenamento, visualização e processamento de objetos de informação que podem ser utilizados em aplicações médicas. A biblioteca foi concebida para ser reutilizável em várias aplicações de software, mas o 3D Slicer é a única aplicação importante que é conhecida por utilizá-la.

Modelo (ou nó de modelo): Nó MRML que armazena malha de superfície (consiste em células triangulares, poligonais ou outras células 2D) ou malha volumétrica (consiste em células tetraédricas, em cunha ou outras células 3D).

Módulo (ou módulo do Slicer): Um módulo Slicer é um componente de software que consiste numa interface gráfica de utilizador (que é apresentada no painel de módulos quando o módulo é selecionado), uma lógica (que implementa algoritmos que operam em nós MRML) que pode fornecer novos tipos de nós MRML, gestores de visualização (que são responsáveis pela apresentação visual desses nós), plugins de entrada e saída (que são responsáveis por carregar/salvar nós MRML em ficheiros), além de vários outros plugins. Os módulos são normalmente independentes e apenas comunicam entre si por meio de modificação de nós MRML; mas às vezes um módulo utiliza funcionalidades fornecidas por outros módulos ao recorrer a métodos na sua lógica.

Nó (ou nó MRML): Um objeto de dados na cena. Um nó pode representar dados (como uma imagem ou uma malha) e descrever a forma como são apresentados (cor, opacidade etc.) e armazenados em disco, aplicadas transformações espaciais etc. Existe uma hierarquia de classes C++ para definir os comportamentos comuns dos nós, como a propriedade de serem armazenados em disco ou de serem geometricamente transformáveis. A estrutura dessa hierarquia de classes pode ser inspecionada no código ou na documentação da API.

Marcador de orientação: Seta, caixa ou marcador com forma humana para mostrar as direções dos eixos em visão de fatias e em 3D.

RAS: Sistema de coordenadas anatômicas superior--anterior-direito. Sistema de coordenadas utilizado internamente no Slicer. Pode ser convertido de/para o sistema de coordenadas LPS, ao inverter a direção dos dois primeiros eixos.

Referência: Não tem um significado específico, mas refere-se normalmente a uma entrada secundária (objeto de dados, quadro de coordenadas, geometria etc.) para uma operação.

Região de interesse (ROI): Especifica uma região em forma de caixa em 3D. Pode ser utilizada para recortar volumes, recortar modelos etc.

Registro: O processo de alinhamento de objetos no espaço. O resultado do registro é uma transformação, que transforma o objeto "em movimento" em objeto "fixo".

Resolução: Tamanho do vóxel de um volume, normalmente especificado em mm/píxel. Raramente é utilizada na interface do utilizador porque o seu significado é um pouco enganoso: um valor de resolução elevado significa um espaçamento grande, o que significa uma resolução ruim de imagem (baixa).

Regulador: Pode referir-se a: 1. Régua de visualização: A linha que é apresentada como uma sobreposição nos visualizadores para servir de referência de tamanho. 2. Linha de marcação: ferramenta de medição de distâncias.

Componente escalar: Um elemento de um vetor. O número de componentes escalares significa o comprimento do vetor.

Valor escalar: Um número simples. Normalmente de ponto flutuante.

Cena (ou cena MRML): É a estrutura de dados que contém todos os dados atualmente carregados na aplicação e as informações adicionais sobre a forma como devem ser apresentados ou utilizados. O termo tem origem na computação gráfica.

Segmento: Corresponde a uma única estrutura numa segmentação. Consulte mais informações na seção “Segmentação de imagens”.

Segmentação (também conhecida como contorno, anotação; região de interesse, conjunto de estruturas, máscara): Processo de delineamento de estruturas 3D em imagens. A segmentação também pode se referir ao nó MRML que é o resultado do processo de segmentação. Um nó de segmentação contém tipicamente múltiplos segmentos (cada segmento corresponde a uma estrutura 3D). Os nós de segmentação não são nós de mapa de rótulos ou nós de modelo, mas podem armazenar várias representações (mapa de rótulos binário, superfície fechada etc.). Ver mais informações na seção “Segmentação de imagens”.

Fatia: Intersecção de um objeto 3D com um plano.

Anotações na visão da fatia: texto no canto da visão de fatias com o nome e as etiquetas DICOM selecionadas dos volumes em exibição.

Espaçamento: Tamanho do vóxel de um volume, normalmente especificado em mm/píxel.

Transformar (ou transformação): Pode transformar qualquer objeto 3D de um sistema de coordenadas para outro. O tipo mais comum é a transformação rígida, que pode alterar a posição e a orientação de um objeto. As transformações lineares podem escalar, espelhar e cisalhar objetos. As transformações não lineares podem deformar arbitrariamente o espaço 3D. Para visualizar um volume no sistema de coordenadas do mundo, o volume tem de ser reamostrado, pelo que é necessária uma transformação do sistema de coordenadas do mundo para o volume (designada por transformação de reamostragem). Para transformar todos os outros tipos de nós para o sistema de coordenadas do mundo, todos os pontos devem ser transformados para o sistema de coordenadas do mundo (transformação de modelagem). Uma vez que um nó de transformação deve ser aplicável a quaisquer nós, os nós de transformação podem fornecer tanto para o nó pai quanto dele (armazena-se um e calcula-se o outro em tempo real).

Volume (ou nó de volume, volume escalar, imagem): Nó MRML, que armazena uma matriz 3D de vóxeis. Os índices da matriz são normalmente referidos como IJK. Designa-se o intervalo de coordenadas IJK por extensões. A geometria do volume é especificada pela sua origem (posição do ponto IJK=(0,0,0)), espaçamento (tamanho de um vóxel ao longo dos eixos I, J, K), direções dos eixos (direção dos eixos I, J, K no sistema de coordenadas de referência) em relação a um quadro de referência. As imagens 2D são volumes 3D de um único corte, com a sua posição e orientação especificadas no espaço 3D.

Vóxel: Um elemento de um volume 3D. Tem a forma de um prisma retangular. As coordenadas de um vóxel correspondem à posição do seu ponto central. O valor de um vóxel pode ser um valor escalar simples ou um vetor.

VR: Abreviatura que pode referir-se à renderização de volumes ou à realidade virtual. Para evitar ambiguidades, recomenda-se geralmente que se utilize o termo completo (ou que se defina explicitamente o significado da abreviatura em um determinado contexto).

VTK: Visualization Toolkit (Kit de ferramenta de visualização). Biblioteca de software que o Slicer utiliza para representação e visualização de dados. Uma vez que a maioria das classes do Slicer é derivada das classes do VTK e utiliza fortemente outras classes do VTK, o Slicer adotou muitas convenções do estilo do VTK e da interface de programação de aplicações.

Janela/nível (ou largura da janela/nível da janela): Especifica o mapeamento linear dos valores de vóxel para o brilho de um píxel exibido. Janela é o tamanho do intervalo de intensidade que é mapeado para o intervalo de intensidade totalmente exibível. Nível é o valor do vóxel que é mapeado para o centro do intervalo de intensidade totalmente exibível.
