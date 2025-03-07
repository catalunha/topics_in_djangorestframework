# Tópicos em DjangoRestFramework

Anotei aqui alguns tópicos importantes em DjangoRestFramework.

Mas é importante consultar a documentação original da linguagem em:

0. https://www.django-rest-framework.org/
0. https://www.djangoproject.com/
0. https://learndjango.com/
0. https://www.w3schools.com/django/
0. https://www.geeksforgeeks.org/django-tutorial/
0. https://www.tutorialspoint.com/django/index.htm
0. https://learndjango.com/tutorials/

# Sumário dos tópicos

1. ([select_related](select_related/readme.md)) select_related
1. ([prefetch_related](prefetch_related/readme.md)) prefetch_related
1. [Celery, redis, django](celery/celery_django_1/readme.md)

Meu Script para criar pasta
```
mkdir input; cd input; touch readme.md; touch code_1.py; cd ..
```

# Ambiente de desenvolvimento


## Linux
Para Linux segue meu roteiro.

Crie uma pasta para o projeto de sua API com djangoRestFramework, e acesse esta pasta
```
mkdir project_name
cd project_name
```

Verificar se o python 3.12 esta ativo
```
pyenv versions
```

Se nao estiver instalado, então instalar com 
```
pyenv install 3.12.0
```

Marcar como o compilador local
```
pyenv local 3.12.0
```
Fixar a versão do python na venv
poetry env use python3.11


Iniciar o poetry
```
poetry init

Would you like... no
Would you like... no
```

Conferindo se a pasta .venv foi criada. Senão verifique estas configs
```
poetry config --list

poetry config virtualenvs.create = true
poetry config virtualenvs.in-project = true
```

Instalando pacotes
```
poetry add boto3
poetry add dj-database-url
poetry add django
poetry add django-cors-headers
poetry add django-debug-toolbar
poetry add django-filter
poetry add django-imagekit
poetry add django-storages[s3]
poetry add djangorestframework
poetry add djangorestframework-simplejwt
poetry add drf-spectacular
poetry add gunicorn
poetry add mailtrap
poetry add pillow
poetry add psycopg2-binary
poetry add python-decouple
poetry add requests
```
Se já houver um pyproject.toml use apenas o comando a seguir. Ou

Se assim que adicionar com poetry add ele não instalar. Apenas adicionar. Então tem que instalar após add.
```
poetry install
```

Ativar poetry a cada trabalho
```
poetry shell
```

Executar um comando lendo o ambiente do poetry
```
poetry run <comando>
```

anotacao

## Linux - old
Criando ambiente sem utilizar poetry
```
$ mkdir project_name
$ cd project_name
$ python -m venv venv
$ source ./venv/bin/activate
$ pip install django
$ django-admin --version
$ django-admin startproject project .
$ python manager.py migrate
$ python manager.py createsuperuser
$ python manager.py runserver <ip_local>:8000
$ cd project
$ python manager.py startapp app1
```

## VSCode
Instale as seguintes extensões:

![](images/extensions.png)


# Criando projeto DjangoRF
Na pasta do projeto digite, para iniciar ambiente virtual
```
poetry shell
```
## Criando projeto

Estando em uma pasta qualquer
```
django-admin startproject django_project .
```
## Criando apps
Sempre criar apps internos no django_project
```
cd django_project
django-admin startapp users
django-admin startapp core
```

Os demais apps são de acordo com o projeto.
```
django-admin startapp app1
```


## Cadatrando app no settings
Antes, mudar o app.apps.py de:
```py
from django.apps import AppConfig


class App1Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app1"
```
para
```py
from django.apps import AppConfig


class App1Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.app1"
```
E depois cadastrar no INSTALLED_APPS com

```
INSTALLED_APPS = [
    "app.users.apps.UsersConfig",
    "app.core.apps.CoreConfig",
    "app.app1.apps.App1Config",
]
```

## Iniciar banco de dados

```
python manage.py makemigrations; python manage.py migrate
```

## Criar super user
```
python manage.py createsuperuser
```
Sugestão de email e senha é:
username/email: admin@django.com
senha: drf@10

# Comandos de dev diario

## iniciar poetry
Na pasta do projeto digite
```
poetry shell
```
Entao vai aparecer
```
(nomeDoProjeto-py3.12) catalunha@pop-os:~/.../pastaDoProjeto$
```

## ativar servidor
(nomeDoProjeto-py3.12) catalunha@pop-os:~/.../pastaDoProjeto$
python manage.py runserver 192.168.10.117:8000
192.168.10.117:8000

## acessar admin ou recriar senha
(nomeDoProjeto-py3.12) catalunha@pop-os:~/.../pastaDoProjeto$
python manage.py changepassword admin@gmail.com

senha atual da conta admin@gmail.com é: django@123

## aplicar migrações
(nomeDoProjeto-py3.12) catalunha@pop-os:~/.../pastaDoProjeto$
python manage.py makemigrations; python manage.py migrate



# Usando uv

```
folder-project$ uv python pin 3.12
Pinned `.python-version` to `3.12`
folder-project$ uv venv
Using CPython 3.12.0
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
folder-project$ uv init
Initialized project `folder-project`
folder-project$ source .venv/bin/activate
(folder-project) folder-project$ python hello.py 
Hello from folder-project!
(folder-project) folder-project$ uv add django


uv add boto3
uv add dj-database-url
uv add django
uv add django-cors-headers
uv add django-filter
uv add django-imagekit
uv add django-storages[s3]
uv add djangorestframework
uv add djangorestframework-simplejwt
uv add gunicorn
uv add pillow
uv add psycopg2-binary
uv add python-decouple
uv add requests
```


```
uv add drf-spectacular
uv add django-debug-toolbar
uv add mailtrap
```


Se o project ja existir use uv sync para pegar os packages do pyproject e recriar o pylock