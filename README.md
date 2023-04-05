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
- Docker *(Not implemented yet)*
- Pandas *(Not implemented yet)*

## How to setup the project
1. Do `git clone thisrepositoryhttpurl.com`
2. Open the terminal
3. Type `python -m venv venv` and then `source venv/bin/activate`(Linux users) or `venv/Scripts/activate`(Windows users)
4. Enter(`cd ./Backend`) in the "Backend" folder and type `pip install -r requirements.txt`
5. Create a `.env` file in the "Backend/setup" path
6. Add the following enviroment variables:
    ```
    SECRET_KEY=yoursecretkey

    EMAIL_HOST_USER=youremail@email.com
    EMAIL_HOST_PASSWORD=yourpassword
    EMAIL_USE_TLS=True
    EMAIL_PORT=yoursmtpport
    EMAIL_HOST=your.smtp.server
    ```
7. Open the terminal again
8. Type `python manage.py migrate`
9. Type `python manage.py createsuperuser` and follow the steps.


## Implemented features:
- [x] Authentication
- [ ] Client registering
- [ ] Payments list
