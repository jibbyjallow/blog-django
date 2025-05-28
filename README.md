# 📘 Blog Django

Aquest és un projecte desenvolupat amb **Django** com a part del mòdul de Programació del cicle de Desenvolupament d’Aplicacions Web.

## 📌 Introducció

L'objectiu principal d'aquest projecte és crear una aplicació web de tipus **blog**, on es poden publicar articles, gestionar autors i etiquetes, i consultar les notícies disponibles. El projecte permet també afegir comentaris a les entrades.

## 🚀 Instal·lació ràpida

Segueix aquests passos per fer-lo funcionar localment:

### 1. Clona el repositori

```bash
git clone https://github.com/jibbyjallow/blog-django.git
cd blog-django

### 2. Instal·la les dependències
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows

pip install -r requirements.txt

### 3. Executa les migracions
python manage.py migrate

Executar el servidor localment
python manage.py runserver

