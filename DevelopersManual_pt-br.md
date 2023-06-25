
# Guia para desenvolvedores de módulos do Slicer

Essas instruções destinam-se aos desenvolvedores de módulos do Slicer (no núcleo do Slicer ou nas extensões do Slicer) que desejam tornar seus módulos traduzíveis.

## Preparando arquivos .ui para tradução

Por padrão, a maioria das propriedades de string e stringlist que aparecem nos arquivos .ui são disponibilizadas para tradução. Normalmente, esse é o comportamento correto, mas, em alguns casos, as string contêm strings que não devem ser traduzidas e não devem aparecer nos arquivos de origem da tradução (.ts).

Propriedades que **devem ser marcadas como não traduzíveis no Qt designer** desmarcando a opção `Translatable`, a menos que sejam definidas com seu valor padrão (normalmente vazio):

- Em widgets de seletor de nódulos, como qMRMLNodeComboBox, qMRMLCheckableNodeComboBox, qMRMLSubjectHierarchyTreeView, qMRMLTreeView:
  - `nodeTypes`
  - `hideChildNodeTypes`
  - `interactionNodeSingletonTag` (se não for o valor padrão "Singleton")
  - `sceneModelType`
  - `levelFilter`
- Em widgets MRML (qMRML...Widget) que suportam quantidades, como qMRMLRangeWidget ou qMRMLCoordinatesWidget:
  - `quantity`
- Em widgets que salvam dados nas configurações do aplicativo, como ctkPathLineEdit, qMRMLSegmentationFileExportWidget, qMRMLSegmentEditorWidget:
  - `settingKey`
  - `defaultTerminologyEntrySettingsKey`
- Em widgets que salvam dados em atributos de hierarquia de nódulos ou objetos, como qMRMLSubjectHierarchyComboBox, SubjectHierarchyTreeView:
  - `includeItemAttributeNamesFilter`
  - `excludeItemAttributeNamesFilter`
  - `includeNodeAttributeNamesFilter`
  - `excludeNodeAttributeNamesFilter`
- Em widgets de visualização de fatias, como qMRMLSliceControllerWidget e qMRMLSliceWidget:
  - `sliceViewName`
  - `sliceOrientation`
- Em qMRMLSegmentationConversionParametersWidget:
  - `targetRepresentationName`
- Em qSlicerMouseModeToolBar:
  - `defaultPlaceClassName`

![](Docs/DesignerMarkAsNonTranslatable.png)

## Uso correto da função de tradução

Sempre que seu programa usar uma string literal (texto entre aspas) que será exibida na interface do usuário, certifique-se de que ela seja processada pela [*função de tradução*] (https://doc.qt.io/qt-5/i18n-source-translation.html#using-tr-for-all-literal-text). Nos códigos-fonte, a função `tr()` é de fato usada para marcar strings traduzíveis para que, em tempo de execução, o `Qt` possa substituí-las por sua versão traduzida que corresponda ao idioma de exibição.

No processo de tradução, é muito importante saber como chamar corretamente a função `tr()`, pois ela determina o contexto que será associado a qualquer string quando ela estiver prestes a ser traduzida.

Portanto, no processo de internacionalização do Slicer, mantivemos algumas recomendações sobre como usar corretamente a função de tradução. Essas diretrizes são descritas nas seções a seguir.

### Como usar *tr()* nas classes QObject

Em uma classe herdeira de QObject, seja essa herança direta ou não, tudo o que é necessário fazer é usar a função [tr()](https://doc.qt.io/qt-5/qobject.html#tr) para obter o texto traduzido para suas classes.
```c++
LoginWidget::LoginWidget()
{
    QLabel *label = new QLabel(tr("Password:"));
    ...
}
````
As classes que herdam o QObject devem adicionar a macro [Q_OBJECT](https://doc.qt.io/qt-5/i18n-source-translation.html#defining-a-translation-context) em sua definição para que o contexto de tradução seja tratado corretamente pelo `Qt`.
```c++
class MainWindow : public QMainWindow
{
    Q_OBJECT

    public:
        MainWindow();
        ...
```

**_NOTA:_** Para evitar erros com algumas ferramentas de compilação (por exemplo, cmake), recomenda-se sempre declarar classes com a macro Q_OBJECT no arquivo de cabeçalho (.h), não no arquivo de implementação (.cpp). Se, por algum motivo, sua classe QObject precisar ser declarada no arquivo .cpp (**por exemplo**, classes de implementação de baixo nível), recomendamos não adicionar a macro Q_OBJECT a essa classe, mas prefixar todas as chamadas `tr()` com a classe pública associada, da seguinte forma `PublicClassName::tr("texto para traduzir")`

### Como usar *tr ()* em classes que não sejam QObject

As classes que não são QObject não têm uma função de tradução, portanto, chamar diretamente `tr()` nelas pode resultar em erros.

Uma prática comum é prefixar as chamadas `tr()` nessas classes com uma classe do núcleo do Qt como `QObject::tr()`, `QLabel::tr()`, etc. Entretanto, não recomendamos essa abordagem, pois o `lupdate` associará essas strings traduzíveis a um contexto diferente da classe em que estão localizadas.
Portanto, quando se trata de traduzir classes que não são do Qt, recomendamos fornecer suporte à tradução para a classe adicionando diretamente a macro [Q_DECLARE_TR_FUNCTIONS](https://doc.qt.io/qt-5/i18n-source-translation.html#translating-non-qt-classes) nela.
```c++
class MyClass
{
    Q_DECLARE_TR_FUNCTIONS(MyClass)

    public:
        MyClass();
        ...
};
```
Isso fornecerá à classe a função `tr()` que pode ser usada diretamente para traduzir as cadeias de caracteres associadas à classe e possibilitará que o `lupdate` encontre cadeias de caracteres traduzíveis no código-fonte.

>**Observação:** Se, por algum motivo, o nome da classe não deve ser exposto a outros desenvolvedores ou tradutores (classes privadas, ...), recomendamos prefixar as chamadas `tr()` com a classe pública associada, da seguinte forma  `PublicClassName::tr("texto para traduzir")`

### Tradução de strings de várias linhas

Strings longas podem ser definidas em várias linhas, como a seguir:

```
QString help = QString(
  "Volume Rendering Module provides advanced tools for toggling interactive "
  "volume rendering of datasets."
  );
```

Traduzir essas strings de várias linhas usando uma função `tr()`, como essa, para permitir que os tradutores traduzam frases completas:

```
QString help = tr(
  "Volume Rendering Module provides advanced tools for toggling interactive "
  "volume rendering of datasets."
  );
```

Não traduza dessa forma, pois as cstrings traduzíveis conteriam fragmentos de frases:

```
// ISSO ESTÁ ERRADO!
QString help =
  tr("Volume Rendering Module provides advanced tools for toggling interactive ") +
  tr("volume rendering of datasets.");
```

### Tradução de atalhos de teclado

De acordo com as [Recomendações do Qt] (https://doc.qt.io/qt-6/qkeysequence.html#keyboard-layout-issues), os atalhos de teclado devem ser especificados usando strings traduzíveis para poder acomodar melhor os diferentes layouts de teclado comumente usados em um idioma específico.

Exemplos:

```c++
this->RunFileAction->setShortcut(QKeySequence::Print);  // melhor opção (se houver uma sequência de teclas padrão disponível)
this->RunFileAction->setShortcut(ctkConsole::tr("Ctrl+g"));  // opção preferida, se uma sequência de teclas padrão não estiver disponível
this->RunFileAction->setShortcut("Ctrl+g");  // não use
this->RunFileAction->setShortcut(Qt::CTRL | Qt::Key_G);  // não use
```

### Tradução de título do módulo

O título do módulo (o nome que é visível no seletor de módulo) é retornado pela classe do módulo e deve ser traduzido.

Em módulos carregáveis C++ mais antigos, o nome do módulo foi definido em CMakeLists.txt usando uma macro e foi definido no arquivo de cabeçalho do módulo usando a definição do pré-compilador `QTMODULE_TITLE`. Para tornar o título do módulo carregável em C++ traduzível (consulte o exemplo [aqui](https://github.com/Slicer/Slicer/commit/3f05bc595f25c49b0b213c6b116eebec595e03b2)):
- Remova as linhas `set(MODULE_TITLE ${MODULE_NAME})` e `TITLE ${MODULE_TITLE}` do arquivo `CMakeLists.txt`.
- Use `tr("qSlicerLoadableModuleTemplateModule")` em `qSlicerGetTitleMacro()` no arquivo de cabeçalho do módulo

### Avisos comuns do Qt lupdate

Se as chamadas `tr()` não forem tratadas corretamente no código-fonte, alguns avisos poderão ser exibidos durante a execução do `lupdate`.

#### Não é possível chamar tr() desta forma

A ferramenta Qt lupdate lança o aviso `Cannot invoke tr() like this` quando a função de tradução é chamada utilizando um objeto como `q->tr(...)`. O problema é que o lupdate não pode determinar o nome da classe em que o `tr()` é chamado e, portanto, ele não sabe o contexto da tradução.

Esse problema pode ser resolvido explicitando o nome da classe na chamada, por exemplo, `qSlicerScalarVolumeDisplayWidget::tr(...)`, conforme descrito nas seções anteriores.

#### Class  _'SomeClassName'_  lacks Q_OBJECT macro

A ferramenta Qt lupdate lança o aviso `Class 'SomeClassName' lacks Q_OBJECT macro` quando a função de tradução é chamada em uma classe QObject sem a macro Q_OBJECT em sua definição. O problema também é que o `lupdate` não pode determinar o nome da classe em que `tr()` é chamado e, portanto, não conhece o contexto da tradução.

A solução é adicionar a macro `Q_OBJECT` na classe em que `tr()` é chamada ou, no caso de classes que não devem ser expostas (classes privadas, classes de implementação de baixo nível, ...), prefixar as chamadas `tr()` com a classe pública associada, conforme descrito nas seções anteriores.

## Identificação de strings traduzíveis

No processo de tradução, somente as strings que são exibidas no nível da interface do usuário devem ser consideradas. Portanto, as cadeias de caracteres referentes a nomes de módulos, conteúdo de arquivos, extensões de arquivos, comunicações com o desenvolvedor, como mensagens de registro (por exemplo, saídas `PrintSelf` ou `qCritical`) ou qualquer conteúdo relacionado ao desenvolvedor, devem ser consideradas como não traduzíveis.

Para deixar claro que uma cadeia de caracteres não deve ser traduzida, o comentário `/*no tr*/` pode ser adicionado a uma cadeia de caracteres para indicar que a função `tr()` não é usada intencionalmente.

## Uso de classes de base comuns para strings compartilhadas

Para evitar a duplicação de strings de origem, um método `tr()` de uma classe base comum deve ser usado para as seguintes strings:
- Nomes de categorias de módulos (`Informatics`, `Registration`, `Segmentation`, ...) devem ser traduzidos usando `qSlicerAbstractCoreModule::tr()`

## Extrair strings traduzíveis

Contamos com a ferramenta lupdate do Qt para extrair strings traduzíveis do código-fonte e mesclá-las com os arquivos de tradução existentes. Executamos etapas adicionais para extrair o script traduzível da descrição XML dos módulos da CLI e dos arquivos Python e também oferecemos suporte a vários idiomas. Portanto, é criado um script Python que pode executar todas as etapas de processamento: [update_translations.py]([url](https://github.com/Slicer/Slicer/blob/main/Utilities/Scripts/update_translations.py)).

### Como atualizar strings traduzíveis

#### pré-requisitos
- Clonar o repositório https://github.com/Slicer/SlicerLanguageTranslations
- Clone o repositório https://github.com/Slicer/Slicer
- Instale o Qt-6.3 ou posterior (as versões anteriores não têm o lupdate que pode extrair strings do código Python)
- Instale o Python-3.9 ou posterior

#### Atualizar arquivos de origem da tradução
- Certifique-se de que todas as pull requests no repositório enviadas pela Weblate sejam mescladas (para evitar conflitos de mesclagem). Se forem esperadas alterações no repositório (por exemplo, porque houve algumas atualizações recentes), pode valer a pena esperar até que essas alterações sejam concluídas. Também é possível bloquear temporariamente o Weblate para não aceitar nenhuma modificação enquanto executamos as etapas abaixo.
- Verifique se o repositório clonado está atualizado e se não há arquivos modificados localmente. (para evitar conflitos de mesclagem e evitar que conteúdo obsoleto entre nos arquivos de origem da tradução)
- Execute estes comandos:

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
