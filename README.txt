
CONFIGURACION E INSTALACION 

Instalar y activar el entorno virtual
python3 -m venv venv
source venv/bin/activate

Clonar codigo fuente
git clone https://github.com/betovone/tmob.git

Instalar librerias necesarias
pip install -r requeriments.txt

Configurar archivo de datos propios de la aplicacion
(dicho archivo no debe ir en GIT pero lo agrego porque es un proyecto de prueba y 
para que tengan una guia de como realizar la configuracion)
secret.json


Ejecutar - (no olvidarse de levantar servidor de memcached y servidor mysql)
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Admin:
http://127.0.0.1:8000/admin/


Peticiones GET a realizar desde cliente (ENDPOINTS):
Usando libreria JSONResponse:
http://127.0.0.1:8000/api/redirect/by-key/KEY/

Usando Rest Framework:
http://127.0.0.1:8000/api/redirect/by-key-rest/KEY/



ANEXO

Instalacion MEMCACHED en UBUNTU 20.04

sudo apt update
sudo apt install memcached
sudo apt install libmemcached-tools
sudo systemctl start memcached

sudo systemctl status memcached

#memcached -vvv

Instalacion MYSQL en Ubuntu 20.04

sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation

#mysql -p -u root
mysql> show databases;
mysql> CREATE DATABASE tmob;
mysql> GRANT ALL PRIVILEGES ON tmob.* TO ‘root’@‘localhost’;
mysql> use tmob;


