# IPS - Internet Provider management System
### IPS is an simple internet provider management system made with DRF.

:warning: **This project is still in the development phase. In the coming days, new features will be added and better documentation.**

## Used technologies and libraries:
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
2. Open the terminal and type `cd Backend` to enter in the Backend folder.
3. Type `python -m venv venv` and then `source venv/bin/activate`(Linux users) or `venv/Scripts/activate`(Windows users)
4. Create a `.env` file in the "Backend" path
5. Add the following enviroment variables:
    ```
    SECRET_KEY=yourownsecretkey

    EMAIL_HOST_USER=youremail@email.com
    EMAIL_HOST_PASSWORD=youremailpassword
    EMAIL_USE_TLS=True
    EMAIL_PORT=emailsmtpport
    EMAIL_HOST=youremailsmtpserver

    DATABASE_DB=ipsdb
    DATABASE_USER=postgres
    DATABASE_PASSWORD=postgres
    DB_HOST=localhost
    DB_PORT=5431
    ```
6. Open the terminal again and type `sudo docker-compose up --build`
7. Open another terminal
8. Type `python manage.py migrate`
9. Run the `populate_database.py` (folder path: Backend/populate_database.py)
10. Type `python manage.py createsuperuser` and follow the steps.

