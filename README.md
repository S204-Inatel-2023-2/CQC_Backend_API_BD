# API AWS Lambda_Function usando Neo4J

Trata-se de uma API Flask conectada com o banco Neo4j para o projeto EventNow. Foi dado Deploy usando o serviço AWS e o Lambda-Function oferecido também pela Amazon, mas roda
localmente tbm (parte comentada do Código app.py).

## Documentação sobre Teste de API no Postman com Newman e o Arquivo de CI

## Introdução

Este documento fornece uma visão geral e documentação para a execução de testes de API utilizando o Postman e Newman, integrado com GitHub Actions para automação contínua (CI/CD). O arquivo fornecido é um exemplo de um fluxo de trabalho (workflow) que executa testes de API após push ou pull request no repositório.

## Requisitos Prévios

- [Postman](https://www.postman.com/) instalado.
- [Node.js](https://nodejs.org/) instalado.
- Conta no GitHub para configurar ações.

## Estrutura do Projeto

- **postman:** Diretório contendo arquivos do Postman.
  - **EventNowDB.postman_collection.json:** Coleção de requisições Postman.
- **.github/workflows:** Diretório onde o arquivo CI/CD reside.
  - **main.yml:** Arquivo de workflow para GitHub Actions.

## Arquivo de CI/CD (main.yml)

### Disparadores (Triggers)

O workflow é acionado em três cenários:

1. **Push:** Executado quando há push na branch `main`.
2. **Pull Request:** Executado quando há pull request na branch `main`.
3. **Workflow Dispatch:** Pode ser manualmente acionado através da interface do GitHub.

### Estrutura do Workflow

O workflow consiste em uma série de passos (steps) que são executados em um ambiente Ubuntu.

1. **Checkout do Código:**
   - Usa a ação `actions/checkout@v2` para obter o código do repositório.

2. **Verificação de Versões:**
   - Verifica as versões do Newman e do Node no ambiente.

3. **Instalação do Newman-Reporter-Htmlextra:**
   - Utiliza o npm para instalar globalmente o reporter `newman-reporter-htmlextra`.

4. **Execução da Coleção do Postman:**
   - Executa a coleção do Postman usando o Newman.
   - Gera um relatório em formato HTML usando os reporters `cli` e `htmlextra`.
   - Exporta o relatório para `./results/Report.html`.

5. **Arquivamento de Artefatos de Produção:**
   - Utiliza a ação `actions/upload-artifact@v2` para arquivar o relatório HTML gerado.

### Como Usar

1. Configure o Postman e crie a coleção de testes.
2. Coloque a coleção no diretório `postman` do seu repositório.
3. Copie o arquivo `main.yml` para o diretório `.github/workflows` do seu repositório.
4. Faça push das alterações para o GitHub.
5. O workflow será acionado automaticamente em push, pull request ou manualmente.

### Resultados

- O relatório gerado estará disponível como um artefato de produção no GitHub.

Este arquivo de CI/CD automatiza a execução de testes de API, fornecendo feedback rápido sobre a integridade da API em diferentes situações, facilitando a detecção de regressões e problemas de integração.
