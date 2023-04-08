# IPS - Internet Provider management System
### IPS is an simple internet provider management system made with DRF.

:warning: **This project is still in the development phase. In the coming days, new features will be added and better documentation.**

## What does the IPS System do :interrobang:
The IPS System have 4 main apps: The user management app, the customer management app, the service management app, and the payment and monthly fee management app.

## Used technologies and libraries :books:
- Python
- Django
- Django Rest Framework
- Decouple
- Validate DocBr
- SimpleJWT
- PostgreSQL
- Docker-compose
- Pandas *(Not implemented yet)*

## How to setup the project
1. Do `git clone https://github.com/marquesdavi/ips-api.git`
2. Type `python -m venv venv` and then `source venv/bin/activate`(Linux users) or `venv/Scripts/activate`(Windows users)
3. Create a `.env` file in the "Backend" path
4. Add the following enviroment variables:
    ```
    SECRET_KEY=yourownsecretkey

    EMAIL_HOST_USER=youremail@email.com
    EMAIL_HOST_PASSWORD=youremailpassword
    EMAIL_USE_TLS=True
    EMAIL_PORT=emailsmtpport
    EMAIL_HOST=youremailsmtpserver

    DATABASE_DB=ips_db
    DATABASE_USER=postgres
    DATABASE_PASSWORD=postgres
    DB_HOST=localhost
    DB_PORT=5432
    ```
5. Create a file called `.env.docker` in the main repository folder
6. Add the following enviroment variables:
    ```
    SECRET_KEY=yourownsecretkey

    EMAIL_HOST_USER=youremail@email.com
    EMAIL_HOST_PASSWORD=youremailpassword
    EMAIL_USE_TLS=True
    EMAIL_PORT=emailsmtpport
    EMAIL_HOST=youremailsmtpserver

    DATABASE_DB=ips_db
    DATABASE_USER=postgres
    DATABASE_PASSWORD=postgres
    DB_HOST=db
    DB_PORT=5432
    ```
7. Open the terminal again and type `sudo docker-compose up --build`
8. Open another terminal
9. Type `python manage.py createsuperuser` and follow the steps.

**Extra:** Run the `python populate_database.py` if you want to have some data in your database.(folder path: Backend/populate_database.py)

