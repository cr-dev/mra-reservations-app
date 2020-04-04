Steps to Create a Django Application using pipenv and python 3.8

1. Run the following command to create a virtual environment:
    pipenv --python 3.8
2. Activate pipenv with:
    pipenv shell
3. Install Django Framework with pip:
    pip install Django
4. Verify Django version:
    python -m django --version
5. Start Django project:
    django-admin startproject <project_name>
6. Go into the <project_name> folder:
    cd <project_name>
7. Run the django app in the server:
    python manage.py runserver
8. Run the migrations with:
    python manage.py migrate

Adding an App to the Django Project:

1. Execute the following command to create your django app module inside the current <project_name>
    # Note: Make sure you are in the correct folder and with the correct python virtual environment (pipenv shell)
    python manage.py startapp <app_name>
2. Configure urls and the rest of the stuff. Look for it in the django documentation.

Adding the Django Rest Framework (DRF):
1. Check version requirements for django and python in DRF docs and then execute the following commands when versioning is figured out:
    pip install djangorestframework
    pip install markdown
    pip install django-filter
2. Add DRF to the INSRTALLED_APPS variable (see DRF docs)
3. Run any pending migrations
4. Create a super user:
    python manage.py createsuperuser
    ** user admin:django2020
5. Setup Serializers (see DRF docs)
    Create serializers.py within the app in the project

Adding DRF Serializers:

1. Create classes for all serializers needed in serializers.py
2. Configure views correctly in views.py
    - Import viewsets and permissions
3. Create view templates and load static files
    class HomeView(TemplateView):
        template_name = 'reservations/home.html'
        <script src="{% static 'js/index.js' %}" charset="utf-8"></script>