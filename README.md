# API de Previsão e Otimização

Uma API para realizar previsões de séries temporais e otimizações.

## Descrição

Esta aplicação consiste em uma API desenvolvida com FastAPI que fornece endpoints para realizar previsões de vendas. A API utiliza um modelo de série temporal (Prophet) para prever futuras vendas com base em dados históricos armazenados em um banco de dados PostgreSQL.

## Funcionalidades

-   **Previsão de Vendas:** Endpoint para prever o total de vendas para um número de dias no futuro.
-   **Autenticação:** Proteção dos endpoints com autenticação baseada em token.
-   **Integração com Banco de Dados:** Conexão com um banco de dados PostgreSQL para buscar dados de vendas.

## Tecnologias Utilizadas

-   **Python 3**
-   **FastAPI:** Framework web para a construção da API.
-   **Prophet:** Biblioteca do Facebook para previsão de séries temporais.
-   **Pandas:** Para manipulação de dados.
-   **Psycopg2:** Adaptador de banco de dados PostgreSQL para Python.
-   **Dotenv:** Para gerenciamento de variáveis de ambiente.
-   **Docker:** Para containerização da aplicação.

## Configuração e Instalação

### Pré-requisitos

-   Python 3.10.x
-   Docker (opcional, para rodar em um container)
-   Um banco de dados PostgreSQL

### Passos

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/gabrielalmir/techfinance-previsao/
    cd techfinance-previsao
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # No Windows, use `.venv\Scripts\activate`
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**

    Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

    ```
    DB_USER=seu_usuario_db
    DB_PASS=sua_senha_db
    DB_HOST=seu_host_db
    DB_PORT=sua_porta_db
    DB_NAME=seu_nome_db
    AUTHORIZATION=seu_token_de_autenticacao
    ```

5.  **Execute a aplicação:**

    ```bash
    uvicorn main:app --reload
    ```

    A API estará disponível em `http://127.0.0.1:8000`.

### Usando Docker

Você também pode rodar a aplicação usando Docker:

1.  **Construa a imagem Docker:**

    ```bash
    docker build -t previsao-api .
    ```

2.  **Rode o container:**

    Certifique-se de passar as variáveis de ambiente para o container. Você pode fazer isso usando a flag `--env-file`.

    ```bash
    docker run -d -p 8000:8000 --env-file .env previsao-api
    ```

## Endpoints da API

### `POST /previsao/vendas`

Realiza a previsão de vendas.

-   **Parâmetros de Query:**
    -   `dias_previsao` (int, opcional, default: 30): O número de dias no futuro para prever.
-   **Headers:**
    -   `Authorization`: `Bearer seu_token_de_autenticacao`
-   **Resposta de Sucesso (200 OK):**

    Um JSON array com a previsão. Cada objeto no array contém:
    -   `ds`: A data da previsão (YYYY-MM-DD).
    -   `yhat`: O valor previsto.
    -   `yhat_lower`: O limite inferior da previsão.
    -   `yhat_upper`: O limite superior da previsão.

-   **Resposta de Erro:**
    -   `401 Unauthorized`: Se o token de autenticação for inválido ou não for fornecido.
    -   `404 Not Found`: Se não houver dados de vendas no banco de dados.

## Modelos de Dados (Estrutura das Tabelas)

O arquivo `models.py` contém dataclasses que representam a estrutura esperada das tabelas no banco de dados.

-   `FatecVendas`: Armazena os dados de vendas.
-   `FatecClientes`: Armazena informações sobre os clientes.
-   `FatecProdutos`: Armazena informações sobre os produtos.
-   `FatecContasReceber`: Armazena informações sobre contas a receber.
