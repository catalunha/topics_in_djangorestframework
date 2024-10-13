Artigos:
+ https://medium.com/@akshatgadodia/introduction-to-python-poetry-why-its-a-game-changer-for-python-developers-2152c344cbfd
- https://medium.com/@akshatgadodia/getting-started-with-python-poetry-d67862199944
- https://medium.com/@akshatgadodia/diving-into-pyproject-toml-configuring-your-python-project-with-poetry-acabf7398e7a
- https://medium.com/@akshatgadodia/mastering-poetry-commands-unlocking-the-full-power-of-python-poetry-8363f347beb5




# Instalando
curl -sSL https://install.python-poetry.org | python3 -

# Mão na massa
catalunha@pop-os:~/apps/topics_in_djangorestframework/poetry$ poetry --version
Poetry (version 1.8.2)
catalunha@pop-os:~/apps/topics_in_djangorestframework/poetry$ poetry new my_project
```
catalunha@pop-os:~/apps/topics_in_djangorestframework/poetry/my_project$ tree .
.
├── my_project
│   └── __init__.py
├── pyproject.toml
├── README.md
└── tests
    └── __init__.py

2 directories, 4 files
catalunha@pop-os:~/apps/topics_in_djangorestframework/poetry/my_project$ 
```
atual pyproject.toml
```
python = "^3.11"

```

Modificar pyproject.toml 
```
python = "^3.12"

```
Apagar .venv e poetry.lock

catalunha@pop-os:~/apps/topics_in_djangorestframework/poetry/my_project$ poetry install

catalunha@pop-os:~/apps/topics_in_djangorestframework/poetry/my_project$ poetry add requests

catalunha@pop-os:~/apps/topics_in_djangorestframework/poetry/my_project$ poetry run start

catalunha@pop-os:~/apps/topics_in_djangorestframework/poetry/my_project$ poetry add --group dev pytest

catalunha@pop-os:~/apps/topics_in_djangorestframework/poetry/my_project$ poetry shell
Spawning shell within /home/catalunha/apps/topics_in_djangorestframework/poetry/my_project/.venv
. /home/catalunha/apps/topics_in_djangorestframework/poetry/my_project/.venv/bin/activate
catalunha@pop-os:~/apps/topics_in_djangorestframework/poetry/my_project$ . /home/catalunha/apps/topics_in_djangorestframework/poetry/my_project/.venv/bin/activate
(my-project-py3.12) catalunha@pop-os:~/apps/topics_in_djangorestframework/poetry/my_project$ poetry env list
.venv (Activated)

(my-project-py3.12) catalunha@pop-os:~/apps/topics_in_djangorestframework/poetry/my_project$ poetry export -f requirements.txt --output requirements.txt
Warning: poetry-plugin-export will not be installed by default in a future version of Poetry.
In order to avoid a breaking change and make your automation forward-compatible, please install poetry-plugin-export explicitly. See https://python-poetry.org/docs/plugins/#using-plugins for details on how to install a plugin.
To disable this warning run 'poetry config warnings.export false'.
