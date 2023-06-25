## Dicas e Truques

### Ferramenta *Find text*

A ferramenta `Find text` foi adicionada para extração rápida do texto da aplicação e encontrar ocorrências desse texto no site de traduções:

- Vá para o módulo `Language Tools`
- Abra a seção `Find text`
- Defina o idioma editado: as string extraídas serão abertas no site, mostrando traduções nesse idioma. Exemplo: `pt-BR`, `fr-FR`, `hu-HU`.
- Marque a caixa `Enable text finder`
- Aperte o atalho `Ctrl+6` a qualquer momento para exibir o seletor de widget
- Clique no widget que contenha texto traduzível (pressione qualquer tecla para cancelar a seleção do widget)
- Clique em `OK` para abrir o texto encontrado no site de tradução

![](Docs/FindText.png)

Limitações Conhecidas:
- A ferramenta apenas extraí Qt widgets (não de views renderizadas pela biblioteca VTK).
- Extração de texto de janelas flutuantes e pop-up não é suportada.

### Tradução de links externos

Se o texto traduzido contém links para sites externos que suportam vários idiomas, geralmente é preferível não codificar fixamente um idioma específico (para permitir que o site externo use seu próprio idioma preferido). Por exemplo: <https://docs.github.com/get-started/quickstart/fork-a-repo> é preferível (em vez de fixar em inglês adicionando `/en` dessa forma: <https://docs.github.com/en/get-started/quickstart/fork-a-repo>).

Entretanto, nem todos os sites podem definir automaticamente um idioma preferencial. Por exemplo, [ReadTheDocs](https://readthedocs.org) exige a especificação explícita da linguagem na URL: <https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/import_process.html> é válido, mas <https://docs.godotengine.org/stable/tutorials/assets_pipeline/import_process.html> é um URL inválido. Nesses casos, o URL do link deve ser alterado em cada tradução para corresponder ao idioma de destino.

Veja a discussão relacionada [aqui](https://github.com/Slicer/Slicer/pull/6401#discussion_r884768951).

## Uso avançado

### Instalar arquivos de tradução off-line

Os arquivos de tradução (.ts) podem ser baixados para uma pasta e instalado a partir dela posteriormente, sem acesso à rede.

Os arquivos de tradução podem ser baixados do Weblate ou do GitHub. Por exemplo, abra o [projeto Slicer no Weblate](https://hosted.weblate.org/project/3d-slicer) selecione a página de tradução de um idioma (como [Português Brasileiro](https://hosted.weblate.org/projects/3d-slicer/3d-slicer/pt_BR/)), e, no menu, selecione `Arquivos` -> `Baixar tradução`.

Instale os arquivos de tradução:
- Selecione a opção `Local folder`
- Selecione a pasta que contém o(s) arquivo(s) .ts no campo `Input folder` na seção `Input translations`.
- Marque a opção `Latest file only` para utilizar somente o último arquivo .ts baixado. Isso é útil se a pasta local for definida diretamente como a pasta de download do navegador da Web.
- Compile os arquivos de tradução e instale-os no aplicativo clicando no botão `Update translation files`.
