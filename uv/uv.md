Instalar ubuntu


# Instalar uv
https://docs.astral.sh/uv/getting-started/installation/#installation-methods

# Config .bashrc final

```

```

# Instalar docker
https://docs.vultr.com/how-to-install-docker-on-ubuntu-24-04?ref=9141995&utm_source=performance-max-latam&utm_medium=paidmedia&obility_id=17096555207&&utm_campaign=LATAM_-_Brazil_-_Performance_Max_-_1001&utm_term=&utm_content=&ref=9141995&gad_source=1&gclid=CjwKCAiAwaG9BhAREiwAdhv6Y8XO6-zpBRZHeBgjhL3NQGtfWpkuScmxhI4WiajvLp5En6NM4y3CuBoCjPIQAvD_BwE

sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo docker --version



---



https://blog.pecar.me/uv-with-django




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

(folder-project) folder-project$ uv add --group dev pytest


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


# Outros comandos
https://medium.com/@petrica.leuca/what-ive-discovered-while-using-uv-436b4085b6d6