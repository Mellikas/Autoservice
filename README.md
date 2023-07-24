# Autoservice

The first Django website project created during the CodeAcademy course.

**DESCRIPTION**

The website was created to familiarize with:
- Django framework
- HTML templates
- SQLite

**HOW TO INSTAL AND RUN**

1. Create a new project in your IDE (e.g. PyCharm)
2. Download zipped project
3. Upload the unzipped files to the newly created project
4. In terminal run: `pip install -r requirements.txt`
6. In terminal run: `python manage py makemigrations`
7. In terminal run: `python manage py migrate`
8. In terminal run: `python manage.py createsuperuser` and creat admin user (while typing pasword it won't appear)
9. In terminal run: `python manage.py runserver localhost:18080` (or similar `localhost: 18000` etc.) 
10. Push on active server link in terminal.
11. Go to http://localhost:18080/admin/ and add data in this order:
    1. Car models
    2. Service
    3. Users
    4. Client autos
12. Go to http://localhost:18080/car_service/ and check it.

**CREDITS**
   
The project was created with CodeAcademy (https://codeacademy.lt/en/) educational materials.
