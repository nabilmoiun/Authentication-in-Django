# Authentication in Django

***This project is part of a series on YouTube that teaches how to implement full authentication in Django.***

[Watch on Youtube](https://www.youtube.com/watch?v=nYcWtM-fU0M&list=PLoomN1iY7V9m3o1prTA-z6sxUFf9jLf8l)

Project Summary and Features
================

  + Custom user model
  + User registration
  + User authentication through username or email
  + Change user password
  + Reset password through email
  + Custom authentication backend
  + Custom mixins
  + Send email using multhreading
  + Overriding custom django auth views

Usage
=================

First clone this repo and go to the project root.

    $ git clone https://github.com/nabilmoiun/Authentication-in-Django.git
    $ cd Authentication-in-Django

I would recommend to work on a virtual environment. I have used ***virtualenv*** package to create a virtual environment you may wanna use other package. So install this as well if you already haven't.

    $ pip install virtualenv
    
Now create you own virtual environment here and install the project required packages written in requirements.txt file by running the following commands.

    $ virtualenv venv_name

Activate the virtual environment by the following command:


***On Linux***

    $ source venv_name/bin/activate
    
***On Windows***

If you are using git bash

    $ source venv_name/Scripts/activate
    
If you are using CMD

    $ cd venv_name/Scripts
    $ activate
    $ cd ../../
    
    
Now install the package requirements by:

    $ pip install -r requirements.txt
    
Well your environment is ready now.

Finally, you have to make migrations to get the app started and create a new superuser to interact with the admin dashboard.
So run the following commands as follows:

    $ python manage.py migrate
    $ python manage.py createsuperuser

So after successful completion of these you are ready to run the application by the following command:

    $ python manage.py runserver
    
Now open the browser go to ***localhost/8000/*** and you will see the home/login page of the application.


***NB: you have to change the following configurations in settings.py to send email for password reset***


    $ EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    $ EMAIL_USE_TLS = True
    $ EMAIL_HOST = "smtp.gmail.com"
    $ EMAIL_HOST_USER = "example@gmail.com"
    $ EMAIL_HOST_PASSWORD = "yourapppassword"
    $ EMAIL_PORT = 587


