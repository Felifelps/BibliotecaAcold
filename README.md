# Biblioteca Acold

Este repositório contém o código-fonte para uma aplicação web de gerenciamento de biblioteca, desenvolvida com Django. A aplicação permite cadastrar, listar, atualizar e excluir autores, livros, categorias, empréstimos, leitores, editoras e localizações.

## Descrição do Projeto

O projeto "Biblioteca Acold" é uma aplicação web para gerenciar os recursos de uma biblioteca, permitindo o cadastro e controle de livros, autores, categorias, empréstimos, leitores, editoras e localizações.  A aplicação oferece funcionalidades para pesquisar, listar e detalhar os registros, e também para realizar empréstimos e controlar o retorno dos livros.  O sistema permite a administração de todos os dados da biblioteca de forma organizada e eficiente.

## Estrutura dos Arquivos

O repositório contém diversos arquivos e diretórios, organizados de acordo com a estrutura de um projeto Django:

* **`app/`**:
    * **`__init__.py`**: Módulo inicial do aplicativo.
    * **`models.py`**: Definições dos modelos de banco de dados (Autores, Livros, Categorias, Empréstimos, Leitores, Editoras e Localizações).
    * **`forms.py`**: Formulários Django para cada modelo.
    * **`urls.py`**: URLs do aplicativo.
    * **`views.py`**: Funções de visualização (views) para cada modelo, incluindo as listagens, criação, edição e exclusão de registros.
    * **`templates/`**: Arquivos de templates (HTML) para exibir as páginas da aplicação.  
    * **`static/`**: Arquivos estáticos (CSS, JavaScript, imagens).
    * **`app/templates/components/`:Componentes HTML reutilizáveis.**
* **`app/templates/`: Templates HTML para cada página da aplicação, incluindo componentes reutilizáveis.**
* **`app/static/`**: Arquivos estáticos, como CSS e JavaScript.
* **`app/urls.py`**: URLs do aplicativo.
* **`app/views.py`**: Funções de visualização (views) do aplicativo.
* **`app/models.py`**: Modelos de banco de dados do aplicativo.
* **`app/forms.py`**: Formulários Django para o aplicativo.
* **`asgi.py`**: Configurações ASGI para o projeto.
* **`wsgi.py`**: Configurações WSGI para o projeto.
* **`app/settings.py`**: Configurações do projeto Django.


## Instruções de Configuração e Execução

1. **Ambiente Virtual:** Crie um ambiente virtual Python.
2. **Instalação das dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configuração do Django:**
   Configure as variáveis de ambiente necessárias no arquivo `app/settings.py`, incluindo:
    * `SECRET_KEY`
    * `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD`, `DATABASE_HOST`, `DATABASE_PORT`
    * `ALLOWED_HOST`
    * `ENVIRONMENT` (para definir o modo de debug)
4. **Migração do banco de dados:**

   ```bash
   python manage.py migrate
   ```

5. **Execução do servidor:**

   ```bash
   python manage.py runserver
   ```

   Acesse a aplicação no seu navegador usando `http://127.0.0.1:8000/`.


## Exemplos de Uso

Para cada modelo (Autores, Livros, Categorias, etc.), existem exemplos de uso em `app/views.py`. Os templates HTML mostram como os dados são exibidos e manipulados.


## Requisitos

* **Python:** Versão 3.x
* **Django:** Versão 5.1.2 (ou compatível)
* **Banco de Dados (PostgreSQL):**  Necessário para armazenar os dados.

