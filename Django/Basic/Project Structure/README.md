# Django Project Structure

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. One of its strengths is its well-organized project structure, which promotes modularity, reusability, and scalability. This guide will delve into the typical structure of a Django project, explaining the purpose of each key file and folder, and highlighting standard content. We'll also cover additional best practices and configurations to help you build robust Django applications.

---

## Table of Contents

1. **Root Directory**
 
2. **Project Package**
 
3. **Application Package**
 
4. **Templates Directory**
 
5. **Static Files**
 
6. **Media Files**
 
7. **Virtual Environment**
 
8. **Requirements File**
 
9. **Migrations**
 
10. **Advanced Project Structure and Cunstomizations**
 
11. **Testing Pratice**
 
---

## 1. Root Directory

At the level of your Django project, you'll typically find the following:

```bash
my_project/
├── manage.py
├── my_project/
├── app_name/
├── templates/
├── static/
├── media/
├── requirements.txt
└── venv/
```

### `manage.py`

- **Purpose**: A command-line utility that lets you interact with your Django project in various ways.

- **Common Commands**:
	
	- `python manage.py runserver` — Starts the development server.
	
	- `python manage.py migrate` — Applies database migrations.
	
	- `python manage.py createsuperuser` — Creates an admin user.

- **Note**: This file is auto-generated and usually doesn't require modification.

### `requirements.txt`

- **Purpose**: Lists all Python dependencies for your project.

- **Usage**:
	
	- Install dependencies with `pip install -r requirements.txt.`

- **Example**:
	```text
	Django>=3.2,<4.0
	djangorestframework
	psycopg2
	```

### `venv/` (Virtual Environment)

- **Purpose**: Isolates your project's Python dependencies from other projects.

- **Usage**:
	
	- Create with `python -m venv venv.`
	
	- Activate with `source venv/bin/activate` (Unix) or `venv\Scripts\activate `(Windows).

---

## 2. Project Package

This is your main project folder, sharing the same name as your project (e.g., `my_project/`).

```bash
my_project/
├── __init__.py
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py
```

### `__init__.py`

- **Purpose**: An empty file that tells Python this directory should be considered a Python package.

### `settings.py`

- **Purpose**: Contains all the configuration for your Django project.

- **Key Sections**:

	- **Installed Applications**

		```python
		INSTALLED_APPS = [
			# Default Django apps
			'django.contrib.admin',
			'django.contrib.auth',
			# ...
			# Third-party apps
			'rest_framework',
			# Custom apps
			'app_name',
		]
		```

	- **Middleware**
		```python
		MIDDLEWARE = [
			'django.middleware.security.SecurityMiddleware',
			'django.contrib.sessions.middleware.SessionMiddleware',
			# ...
		]
		```

	- **Templates**
		```python
		TEMPLATES = [
			{
				'BACKEND': 'django.template.backends.django.DjangoTemplates',
				'DIRS': [BASE_DIR / 'templates'],  # Global templates directory
				'APP_DIRS': True,
				'OPTIONS': {
					'context_processors': [
						# Default processors
						'django.template.context_processors.debug',
						'django.template.context_processors.request',
						# ...
					],
				},
			},
		]
		```

	- **Databases**
		```python
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.sqlite3',  # Or 'django.db.backends.postgresql'
				'NAME': BASE_DIR / 'db.sqlite3',
			}
		}
		```

	- **Static Files**
		```python
		STATIC_URL = '/static/'
		STATICFILES_DIRS = [BASE_DIR / 'static']
		STATIC_ROOT = BASE_DIR / 'staticfiles'  # For 'collectstatic' in production
		```

	- **Media Files**
		```python
		MEDIA_URL = '/media/'
		MEDIA_ROOT = BASE_DIR / 'media'
		```

	- **Security Settings**
		```python
		DEBUG = False  # Set to False in production
		ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'yourdomain.com']
		SECRET_KEY = 'your-secret-key'  # Keep this secret in production
		```
	
### `urls.py`

- **Purpose**: Defines URL patterns for the project.

- **Usage**:
	```python
	from django.contrib import admin
	from django.urls import path, include
	from django.conf import settings
	from django.conf.urls.static import static

	urlpatterns = [
		path('admin/', admin.site.urls),
		path('', include('app_name.urls')),
	]

	if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	```

### `asgi.py` and `wsgi.py`

- **Purpose**: Entry points for ASGI- and WSGI-compatible web servers.

- **Note**: Typically left unmodified unless deploying with specific settings.

---

## 3. Application Package

Applications are Django’s way to group related functionality. Each app has its own directory.

```bash
app_name/
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   └── test_views.py
├── urls.py
└── views.py
```

### `models.py`

- **Purpose**: Defines the data models (database schema) for the app.

- **Example**:
	```python
	from django.db import models

	class Post(models.Model):
		title = models.CharField(max_length=100)
		content = models.TextField()
		created_at = models.DateTimeField(auto_now_add=True)

		def __str__(self):
			return self.title
	```

### `views.py`

- **Purpose**: Contains view functions or classes that handle requests and return responses.

- **Example**:
	```python
	from django.shortcuts import render
	from .models import Post

	def post_list(request):
		posts = Post.objects.all()
		return render(request, 'app_name/post_list.html', {'posts': posts})
	```

### `urls.py` (App-Level)

- **Purpose**: Defines URL patterns specific to this app.

- **Example**:
	```python
	from django.urls import path
	from . import views

	urlpatterns = [
		path('', views.post_list, name='post_list'),
	]
	```

### `forms.py`

- **Purpose**: Contains form classes for handling user input and validation.

- **Example**:
	```python
	from django import forms
	from .models import Post

	class PostForm(forms.ModelForm):
		class Meta:
			model = Post
			fields = ['title', 'content']
	```

### `admin.py`

- **Purpose**: Registers models with the Django admin site.

- **Example**:
	```python
	from django.contrib import admin
	from .models import Post

	@admin.register(Post)
	class PostAdmin(admin.ModelAdmin):
		list_display = ('title', 'created_at')
	```

### `tests/` Directory

- **Purpose**: Contains unit tests for the app, organized by type.

- **Example**:
	```bash
	tests/
	├── __init__.py
	├── test_models.py
	└── test_views.py
	```

- `**test_models.py` Example**:
	```python
	from django.test import TestCase
	from .models import Post

	class PostModelTest(TestCase):
		def test_string_representation(self):
			post = Post(title="Sample Post")
			self.assertEqual(str(post), post.title)
	```

### apps.py

- **Purpose**: Configuration for the app.

- **Example**:
	```python
	from django.apps import AppConfig

	class AppNameConfig(AppConfig):
		default_auto_field = 'django.db.models.BigAutoField'
		name = 'app_name'
	```

---

## 4. Templates Directory

Templates are used to render HTML pages with dynamic content.

```bash
templates/
├── base.html
└── app_name/
    └── post_list.html
```

### `base.html`

- **Purpose**: A base template that other templates inherit from.

- **Example**:
	```html
	<!DOCTYPE html>
	<html>
	<head>
		<title>{% block title %}My Site{% endblock %}</title>
		<link rel="stylesheet" href="{% static 'app_name/css/style.css' %}">
	</head>
	<body>
		<header>
			<h1>My Site</h1>
		</header>
		<nav>
			<!-- Navigation links -->
		</nav>
		<main>
			{% block content %}{% endblock %}
		</main>
		<footer>
			&copy; 2023 My Site
		</footer>
	</body>
	</html>
	```

### `post_list.html`

- **Purpose**: A template that extends `base.html` and displays a list of posts.

- **Example**:
	```html
	{% extends 'base.html' %}

	{% block title %}Post List{% endblock %}

	{% block content %}
		<h2>Posts</h2>
		<ul>
			{% for post in posts %}
				<li>{{ post.title }} - {{ post.created_at }}</li>
			{% endfor %}
		</ul>
	{% endblock %}
	```

### Template Inheritance

- **Purpose**: Allows templates to reuse common structures, promoting DRY principles.

- **Usage**: Child templates use `{% extends 'base.html' %}` to inherit from the base template.

---

## 5. Static Files

Static files include CSS, JavaScript, and images that don't change often.

```bash
static/
└── app_name/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── images/
        └── logo.png
```

### style.css

- **Example**:
	```css
	body {
		font-family: Arial, sans-serif;
		background-color: #f8f9fa;
	}
	```

### Configuration

- **In `settings.py`**:
	```python
	STATIC_URL = '/static/'
	STATICFILES_DIRS = [BASE_DIR / 'static']
	```

### Collecting Static Files for Production

- **Command**: `python manage.py collectstatic`

- **Purpose**: Collects all static files into `STATIC_ROOT` for deployment.

---

## 6. Media Files

Media files are user-uploaded content, such as images or documents.

```bash
media/
└── uploads/
    └── user_1/
        └── profile.jpg
```

### Configuration

- **In `settings.py`**:
	```python
	MEDIA_URL = '/media/'
	MEDIA_ROOT = BASE_DIR / 'media'
	```

- **In `urls.py`**:
	```python
	from django.conf import settings
	from django.conf.urls.static import static

	urlpatterns = [
		# ... your url patterns
	]

	if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	```

---

## 7. Virtual Environment

While not part of the Django structure per se, using a virtual environment is best practice.

### Advantages

- **Isolation**: Keeps project dependencies separate.

- **Consistency**: Ensures that all developers use the same package versions.

### Common Tools

- **venv**: Built-in to Python 3.

- **virtualenv**: An alternative with additional features.

- **pipenv**: Combines virtual environment and package management.

---

## 8. Requirements File

The `requirements.txt` file specifies your project's dependencies.

### Creating `requirements.txt`

- **Command**: `pip freeze > requirements.txt`

### Installing Dependencies

- **Command**: `pip install -r requirements.txt`

---

## 9. Migrations

Migrations track changes to your models and propagate them to the database schema.

```bash
app_name/
└── migrations/
    ├── __init__.py
    ├── 0001_initial.py
    └── 0002_auto_20230315_1234.py
```

### Applying Migrations

- **Commands**:

	- `python manage.py makemigrations` — Creates new migration files.
	
	- `python manage.py migrate` — Applies migrations to the database.

### Migration Files

- **Example**:
	```python
	from django.db import migrations, models

	class Migration(migrations.Migration):

		initial = True

		dependencies = [
			# Specify any dependencies
		]

		operations = [
			migrations.CreateModel(
				name='Post',
				fields=[
					('id', models.BigAutoField(primary_key=True, serialize=False)),
					('title', models.CharField(max_length=100)),
					('content', models.TextField()),
					('created_at', models.DateTimeField(auto_now_add=True)),
				],
			),
		]
	```

---

## 10. Advanced Project Structure and Cunstomizations

### Multiple Apps

- **Purpose**: Break down large projects into smaller, manageable components.

- **Organization**:
	```bash
	my_project/
	├── app_name/
	├── blog/
	├── accounts/
	└── shop/
	```

- **Configuration**:
	- Add each app to `INSTALLED_APPS` in `settings.py`.

### Custom User Model

- **Purpose**: Extend or customize the default Django `User` model.

- Steps:

	- Create a new app (e.g., `accounts`).
	
	- Define a custom user model in `models.py`.
	
	- Update `settings.py`:
		```python
		AUTH_USER_MODEL = 'accounts.CustomUser'
		```

---

## 11. Testing Practices

Organizing tests is crucial for maintaining code quality.

### Structured Tests Directory

```bash
tests/
├── __init__.py
├── test_models.py
├── test_views.py
├── test_forms.py
└── test_urls.py
```

### Example Test Case

```python
from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostViewsTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Test Post", content="Just a test.")

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
```

### Running Tests

- **Command**: `python manage.py test`