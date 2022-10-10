
[![Django CI](https://github.com/weslleycf/projeto-integrador/actions/workflows/django.yml/badge.svg?branch=main)](https://github.com/weslleycf/projeto-integrador/actions/workflows/django.yml)


# PROJETO INTEGRADOR UNIVESP 4º SEMESTRE UNIVESP

## Instalação do ambiente de desenvolvimento:

 - Instalar o [Python](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe)
 - Criar de um ambiente virtual de desenvolvimento com o comando `python -m venv [caminho]`
 - Ativar o ambiente virtual executando o comando no diretório de instalação do ambiente
    virtual `.\Scripts\Activate.bat` (para desativar execute o comando `deactivate`)
 - Clonar ou baixar o projeto uma pasta, na pasta do projeto execute o comando `pip install -r requeriments.txt` para instalar todas as dependências do projeto
 - Depois que as dependências foram instaladas, ainda na pasta do projeto execute o comando `python manage.py makemigrations` e em seguida `python manage.py migrate`, o primeiro
  cria os arquivos de migração de dados, ficam salvos na pasta "core/migrations" e o segundo comando aplica as migrações no banco de dados, o arquivo db.sqlite3 vai ser
  criado na pasta raiz do projeto.
  - Execute o comando `python manage.py createsuperuser` para criar o usuário administrator do sistema, depois de criado já é possivel acessar o admin do site.
  - Para iniciar o servidor execute ainda na pasta do projeto o comando `python manage.py runserver`, em seguida acesse o endereço http://127.0.0.1:8000/ no navegador.
  - Para acessar a pagina administrativa do site acesse http://127.0.0.1:8000/admin e faça o login com o usuario administrador criado anteriormente.


## Gitpod

  
- É possivel executar esse projeto na nuvem pelo [gitpod.io](https://gitpod.io/#https://github.com/weslleycf/projeto-integrador), só é necessário fazer o login com uma conta do github, depois de o ambiente de desenvolvimento abrir bastar abrir um novo terminal e executar o comando `pip install -r requirements.txt` para instalar as dependências, o gitpod é gratuito e disponibiliza 50 horas de uso por mês para contas gratuitas.   
 
 

