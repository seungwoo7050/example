# Django Fundamentals

This guide offers an in-depth look at Django's foundational elements, enriched with detailed explanations and extensive code samples to foster understanding. You'll find thorough coverage of Django's essential components, making it easier to build and manage powerful web applications.
		
---

## Table of Contents

1. **Introduction to Django**

2. **Setting up Django**

3. **Django Project Structure**

4. **Apps in Django**

5. **URLs and Views**

6. **Templates and Static Files**

7. **Models and Databases**

8. **Advanced Database Management**

9. **Migrations**

10. **Django Admin Panel**

11. **Forms and User Input**

12. **Django QuerySet API**

13. **Class-Based Views (CBVs)**

14. **Middleware**

15. **Authentication and Authorization**

16. **OAuth2.0 Implementation**

17. **Two-Factor Authentication (2FA) Implementation**

18. **Signals**

19. **Testing in Django**

20. **Django REST Framework (DRF) Introduction**

21. **Best Practices in Django**

22. **Common Questions**

23. **Main Reference Links**

---

## 1. Introduction to Django

Django is a full-featured web framework designed for **rapid development** and **clean, pragmatic design**. It's built on the principle of **"Don't Repeat Yourself (DRY)"**, allowing you to focus on your application's functionality by providing reusable components.

### Key Features

- **MVT Architecture**: Django follows the Model-View-Template (MVT) structure, separating data management, business logic, and presentation:
	
	- **Model**: Manages the data and defines the database schema.
	
	- **View**: Retrieves data from models and sends it to templates.
	
	- **Template**: Handles the presentation layer, rendering dynamic HTML pages.

- **ORM (Object-Relational Mapper)**: Converts Python classes into database tables, letting you interact with the database seamlessly.

- **Built-in Admin Interface**: Offers a ready-to-use interface for managing data, making it easy for non-developers to handle the backend.

> Understanding database terminology is essential because Django's ORM translates database concepts into Python code, letting developers work with databases more intuitively.

### Database terms

Here is a breakdown of commonly used database terms in Django and web development:

#### Schema

- **Definition**: A schema in database terminology defines the structure of the database. It outlines how data is organized, including tables, fields, relationships, and constraints.

- **In Django**: Each Django model corresponds to a database table. For instance, creating a `User` model in Django will automatically create a `User` table in the database with columns matching the fields defined in the model.

#### Column (or Field)

- **Definition**: A column represents a specific attribute or property within a table. Each column has a data type and stores one aspect of data about the entity.

- **In Django**: Fields in Django models correspond to columns in the database table. For example, defining a `CharField` for a username in a model would create a `username` column in the associated table.

#### Row (or Record)

- **Definition**: A row, also known as a record, is a single entry in a table, representing one instance of the entity. Each row contains data in columns defined by the table's schema.

- **In Django**: When a new object instance is created in Django (like creating a new user), Django ORM inserts a new row in the table corresponding to that model, filling columns based on the instance's attributes.

#### Primary Key

- **Definition**: A primary key is a unique identifier for each row in a table. No two rows can have the same primary key value.

- **In Django**: Django automatically adds a primary key field called `id` to each model. You can specify a different primary key field if you want by setting `primary_key=True` on any field.

#### Foreign Key

- **Definition**: A foreign key is a reference to a primary key in another table, establishing a relationship between two tables.

- **In Django**: Foreign keys are used in Django models to link two models. For instance, if you have an `Order` model that needs to relate to a `User` model, you'd use a foreign key to point from `Order` to `User`.

#### Index

- **Definition**: An index is a data structure that improves the speed of data retrieval. An index is built on one or more columns and allows quick searching.

- **In Django**: You can specify indexed fields in Django models to optimize queries on frequently searched columns. Django automatically indexes primary keys, but additional indexes can be added if needed.

#### Constraints

- **Definition**: Constraints enforce rules at the database level to ensure data integrity, such as unique constraints, not null constraints, and foreign key constraints.

- **In Django**: Constraints can be added in Django models to ensure that certain fields are unique (`unique=True`), required (by setting `null=False` and `blank=False`), or match specific criteria (using model Meta options like `unique_together`).

#### Query

- **Definition**: A query is a request for data from the database. It can be a request to retrieve, update, insert, or delete data.

- **In Django**: Queries are made through Django's ORM. For example, `User.objects.all()` retrieves all users, while `User.objects.filter(name="John")` retrieves only users with the name "John".

---

## 2. Setting up Django

### Step-by-Step Installation

1. **Install Python** (if not already installed): macOS usually comes with Python 2 pre-installed. To use Python 3, install it using Homebrew (if Homebrew isn't installed, see below).

	```bash
	# Install Homebrew (if necessary)
	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

	# Use Homebrew to install Python 3
	brew install python
	```

2. **Create a Virtual Environment**: Using virtual environments isolates project dependencies. To create one, run:

	```bash
	python3 -m venv myenv
	```

3. **Activate the Virtual Environment**: Activate the virtual environment with the following command:

	```bash
	source myenv/bin/activate
	```

4. **Install Django**: Once the environment is active, install Django using `pip`:
	```bash
	pip install django
	```

5. **Start a Django Project**: With Django installed, create a new project using the `startproject` command:

	```bash
	django-admin startproject myproject
	cd myproject
	```

6. **Run the Development Server**: Start the server to verify that everything is set up correctly:

	```bash
	python3 manage.py runserver
	```

Open a browser and visit `http://127.0.0.1:8000` to see Django's welcome page.

---

## 3. Django Project Structure

Django's default project structure is organized for efficient project management.

- **manage.py**: The command-line utility for managing Django commands.

- **settings.py**: Contains configuration settings (database setup, installed apps, middleware).

- **urls.py**: Manages URL routing to direct requests to views.

- **wsgi.py** and **asgi.py**: Web server interfaces for deployment compatibility.

#### Example Configuration

- **Database Configurations**: By default, Django uses SQLite. However, for more robust databases like PostgreSQL, update the `DATABASES` configuration in `settings.py`

### PostgreSQL Example (optional)

Install PostgreSQL using Homebrew and configure `settings.py`:

```bash
brew install postgresql
```

Update `settings.py` to configure PostgreSQL:

```python
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'mydatabase',
		'USER': 'myuser',
		'PASSWORD': 'mypassword',
		'HOST': 'localhost',
		'PORT': '5432'
	}
}
```

Replace `'myuser'` and `'mypassword'` with your PostgreSQL credentials.

---

## 4. Apps in Django

Django projects are organized into **apps**, each responsible for specific functionality. This modular approach improves maintainability and scalability.

### Creating an App

To create a new app, use the following command:

```bash
python3 manage.py startapp myapp
```

This command creates a directory structure within `myapp`:

- **models.py**: Defines the data models for the app.

- **views.py**: Contains logic to process requests and responses.

- **urls.py** (optional): Defines URL routing specific to this app.

- **templates/**: Holds HTML templates for the app.

- **static/**: Stores static assets like CSS and JavaScript files.

### Registering an App

To enable the app in your project, add it to `INSTALLED_APPS` in `settings.py`:

```python
# settings.py
INSTALLED_APPS = [
	# Default apps
	'myapp',	# Add your new app here
]
```

By organizing each function into an app, Django encourages reusability and clean architecture.

---

## 5. URLs and Views

In Django, **URLs** and **views** work together to handle incoming requests and generate responses. URLs serve as entry points to different parts of your application, while views process those requests, retrieve necessary data, and pass it to templates for rendering into HTML or JSON responses.

### URL Routing in Django

Django has a powerful URL routing system, where each URL pattern corresponds to a specific view. The URL dispatcher matches incoming URLs to a predefined list of patterns defined in `urls.py` files across your project and individual apps.

#### Defining URL Patterns in `urls.py`

Every Django app typically has its own `urls.py` file, where you define specific routes for that app. The project’s main `urls.py` file, located in the root directory, consolidates app-specific URLs to create a central routing system.

Here’s an example of defining a URL pattern in an app-specific `urls.py` file:

```python
# myapp/urls.py
from django.urls import path	# Import path for defining URLs
from . import views			 # Import views to link functions to URLs

# Define URL patterns for the app
urlpatterns = [
	path('hello/', views.hello_world, name='hello_world'),  # Maps /hello/ to hello_world view
]
```

In this example:

- `path('hello/', views.hello_world, name='hello_world')`: This line connects the URL `hello/` to the `hello_world` view.

- The `name` **parameter** assigns a name to the URL pattern (`hello_world`). Named URLs are useful for reverse URL resolution, which allows you to refer to URLs by name rather than hard-coding paths throughout your code.

#### Including App URLs in the Main `urls.py` File

To organize routing better, Django’s `urls.py` files in apps are often included in the project’s main `urls.py` file. This way, all routes are centralized and easier to manage:

```python
# project_root/urls.py
from django.contrib import admin
from django.urls import path, include  # Include to add app URLs

urlpatterns = [
	path('admin/', admin.site.urls),  # Route for Django’s built-in admin panel
	path('myapp/', include('myapp.urls')),  # Includes all URLs defined in myapp/urls.py
]
```

Here, include(`'myapp.urls'`) tells Django to look inside the `myapp/urls.py` file for additional URL patterns. Requests that start with `myapp/` will be routed based on the definitions in `myapp/urls.py`.

### Views in Django

Views are functions or classes that process incoming requests, interact with the database (using models), and return responses, usually HTML or JSON. Django supports two main types of views:

1. **Function-Based Views (FBVs)**

2. **Class-Based Views (CBVs)**

Both are commonly used, and each has advantages depending on the complexity and reuse needs of the view.

#### Function-Based Views (FBVs)

FBVs are simple Python functions that receive an HTTP request object and return an HTTP response. FBVs are straightforward and ideal for simpler views with minimal logic.

Example of a Function-Based View:

```python
# myapp/views.py
from django.http import HttpResponse  # Import HttpResponse to return text-based responses

def hello_world(request):
	return HttpResponse("Hello, world!")  # Response text is returned directly
```

Here:
- `hello_world` is a function that takes `request` as a parameter.

- It returns an `HttpResponse` with the text `"Hello, world!"`, which will be displayed when someone visits the `/hello/` URL.

#### Class-Based Views (CBVs)

CBVs are Python classes that provide greater flexibility, reusability, and organization, especially for complex views. Django includes several built-in CBVs, such as `TemplateView`, `ListView`, and `DetailView`, that handle common web application patterns.

Example of a Class-Based View:

```python
# myapp/views.py
from django.views import View  # Import View for creating class-based views
from django.http import HttpResponse

class HelloWorldView(View):
	def get(self, request):
		return HttpResponse("Hello, world!")  # Handles GET requests with a simple response
```

In this example:
- `HelloWorldView` is a class inheriting from Django’s base `View` class.

- The `get` **method** defines what happens when the view receives a GET request. It returns an `HttpResponse` with the text `"Hello, world!"`.

- This CBV can be expanded to handle other HTTP methods, like POST or PUT, by adding corresponding methods (e.g., `post`, `put`).

#### Linking URLs to Class-Based Views

To connect a CBV to a URL, you must call `.as_view()` on the view class in `urls.py`. This tells Django to handle the view class as a function, which is compatible with URL routing.

```python
# myapp/urls.py
from django.urls import path
from .views import HelloWorldView

urlpatterns = [
	path('hello/', HelloWorldView.as_view(), name='hello_world'),  # CBV mapped to URL
]
```

### Differences Between FBVs and CBVs

- **FBVs**: Simpler to write and ideal for views with minimal logic. Each HTTP method requires separate views if different logic is needed.

- **CBVs**: More structured and reusable, especially for views that require similar logic for different HTTP methods. You can create custom views by extending Django’s generic CBVs, making them powerful for complex applications.

---

## 6. Templates and Static Files

Django templates enable dynamic HTML rendering, while static files manage assets such as CSS, JavaScript, and images.

### Template Example

Django templates support loops, conditionals, and variable substitution:

```html
<!-- myapp/templates/greet.html -->
 <!DOCTYPE html>
 <html>
	<head>
		<title>Greeting</title>
	</head>
	<body>
		<h1>Hello, {{ name }}!</h1>
	</body>
</html>
```

### Configuring Static Files

In `settings.py`, define the paths for static files:

```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

Place static assets in each app's **static/** directory to keep them organized and easily accessible.

---

## 7. Models and Databases

In Django, **models** represent the core data structure of your application. They define what data is stored, how it's organized, and the relationships between different entities. Django's ORM (Object-Relational Mapper) translates these models into **database tables**, allowing you to interact with your database using Python instead of SQL.


### Defining a Model

Each Django model is represented as a class in Python, inheriting from models.Model. Each attribute of the model class corresponds to a **column** in the database table. When you define a model, Django's ORM automatically creates a table in the database with the appropriate fields and relationships.

Example of a simple model definition in Django:

```python
# myapp/models.py
from django.db import models	# Import the models module

class Person(models.Model):
	name = models.CharField(max_length=100)	# Defines a CharField for names
	age = models.IntegerField()				# Defines an IntegerField for ages
	email = models.EmailField(unique=True)	# Defines an EmailField with a uniqueness constraint
```

In this example:

- `Person` is a model that represents a table in the database. Each instance of `Person` corresponds to a row in that table.

- **Fields**: `name`, `age`, and `email` are fields in the `Person` model, representing columns in the `Person` table. Each field is defined using a specific **field type** (e.g., `CharField`, `IntegerField`, `EmailField`), which determines the data type of the column.

### How Django Uses Models to Create Database Tables

When you run the command `python manage.py migrate`, Django checks the models and creates corresponding tables in the database if they don't already exist. It also applies any changes made to models through migrations, keeping the database schema synchronized with your models.

### Common Field Types in Django Models

Django provides a wide range of field types to represent different types of data. Here are some of the most commonly used fields:

1. **CharField**: Used for short text, such as names or titles.
	
	- Example: `name = models.CharField(max_length=100)`
	
	- The `max_length` argument specifies the maximum number of characters allowed.

2. **IntegerField**: Stores integer data.
	
	- Example: `age = models.IntegerField()`
	
	- Useful for storing numeric values, like age, quantity, or other counts.

3. **DateTimeField**: Stores date and time information.
	
	- Example: `create_at = models.DateTimeField(auto_now_add=True)`
	
	- `auto_now_add=True` option automatically sets this field to the current date and time when the object is first created.

4. **EmailField**: Stores email addresses, with optional validation for email format.
	
	- Example: `email = models.EmailField(unique=True)`
	
	- The `unique=True` argument enforces a uniqueness constraint on the field, ensuring no two `Person` objects can have the same email address.

5. **TextField**: Used for longer text entries.
	
	- Example: `bio = models.TextField()`
	
	- Useful for descriptions, comments, or other text that doesn't have a strict character limit.

6. **BooleanField**: Stores True/False values.
	
	- Example: `is_active = models.BooleanField(default=True)`
	
	- Used for numerical data that may contain decimal points, like prices or ratings.

7. **FloatField**: Stores floating-point numbers.
	
	- Example: `price = models.FloatField()`
	
	- Used for numerical data that may contain decimal points, like prices or ratings.

### Defining Model Relationships

In addition to fields, models can define **relationship** between different tables. Django supports three primary types of relationships:


#### 1. One-to-Many Relationship (ForeignKey)

- A one-to-many relationship means each row in one table can relate to multiple rows in another table. For example, if each `Book` is written by a single `Author`, but each `Author` can write multiple `Books`, this would be a one-to-many relationship.

- **ForeignKey** is used to represent one-to-many relationship.

Example:

```python
class Author(models.Model):
	name = models.CharField(max_length=100)

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

- Here, each `Book` is related to an `Author` through the `author` field, which is a `ForeignKey`.

- `on_delete=models.CASCADE` specifies that if an `Author` is deleted, all their `Books` should be deleted as well. Other options include `SET_NULL` (set the field to null) and `PROTECT` (prevent deletion of the related object).

#### 2. Many-to-Many Relationship (ManyToManyField)

- A many-to-many relationship allows each row in one table to relate to multiple rows in another, and vice versa. For example, if `Students` can enroll in multiple `Courses` and each `Course` can have multiple `Students`, this is a many-to-many relationship.
- **ManyToManyField** is used to represent many-to-many relationships.

Example:

```python
class Student(models.Model):
	name = models.CharField(max_length=100)
	courses = models.ManyToManyField('Course')

class Course(models.Model):
	title = models.CharField(max_length=100)
```

- Here, each `Student` can enroll in multiple `Courses`, and each `Course` can have multiple `Students`.

- Django creates an **intermediate table** to manage this relationship automatically, which is invisible to the user.

#### 3. One-to-One Relationship (OneToOneField)

- A one-to-one relationship links a single row in one table to a single row in another. This can be useful for extending the data of a model without modifying the original table. For example, a `UserProfile` could be linked to a single `User`.

- **OneToOneField** is used to represent one-to-one relationships.

Example:

```python
class User(models.Model):
	username = models.CharField(max_length=100)

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField()
```

- Here, each `UserProfile` is uniquely associated with a single `User`.

### Adding Constraints in Models

Django allows you to set constraints on fields to enforce data integrity and uniqueness. Some common constraints include:

1. **Unique Constraint**: Ensures no duplicate values in a field. This is specified by setting `unique=True` on a field, as in `email = models.EmailField(unique=True)`.

2. **Not Null Constraint**: Ensures that a field cannot be empty by setting `null=False` (default behavior in Django). For instance, `name = models.CharField(max_length=100, null=False)` ensures `name` cannot be left blank in the database.

3. **Default Value**: Sets a default value if no value is provided. For example, `is_active = models.BooleanField(default=True)`.

4. **Custom Constraints**: Django supports advanced constraints using model `Meta` options or by defining `unique_together` or `constraints` within the model.
	```python
	class Person(models.Model):
		name = models.CharField(max_length=100)
		email = models.EmailField()

		class Meta:
			unique_together = ('name', 'email')	 # Enforces unique name-email pair
	```

### Advanced Model Features

#### Custom Model Managers

Model managers allow you to customize how objects are retrieved from the database. By default, Django provides an `objects` manager for every model.

#### Creating a Custom Manager

```python
# myapp/models.py
from django.db import models

class PublishedManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(is_published=True)

class Article(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	is_published = models.BooleanField(default=False)

	objects = models.Manager()       # The default manager
	published = PublishedManager()   # Our custom manager
```

#### Usage:

```python
# Retrieve all articles
all_articles = Article.objects.all()

# Retrieve only published articles
published_articles = Article.published.all()
```

#### Model Inheritance

Django supports model inheritance to reuse common fields and behaviors.

- **Abstract Base Classes**: Define common fields and methods for other models to inherit.

	```python
	class CommonInfo(models.Model):
		name = models.CharField(max_length=100)
		created_at = models.DateTimeField(auto_now_add=True)

		class Meta:
			abstract = True

	class Student(CommonInfo):
		student_id = models.CharField(max_length=10)

	class Teacher(CommonInfo):
		employee_id = models.CharField(max_length=10)
	```

- **Multi-table Inheritance**: Each model corresponds to its own database table.

	```python
	class Place(models.Model):
		name = models.CharField(max_length=50)
		address = models.CharField(max_length=80)

	class Restaurant(Place):
		serves_pizza = models.BooleanField(default=False)
		serves_pasta = models.BooleanField(default=False)
	```

- **Proxy Models**: Modify the Python-level behavior without changing the model's fields.

	```python
	class Order(models.Model):
		order_date = models.DateField()

	class LatestOrder(Order):
		class Meta:
			proxy = True
			ordering = ['-order_date']
	```

#### Advanced Field Options

- **Validators**: Add custom validation logic to fields.

	```python
	from django.core.validators import MinValueValidator

	class Product(models.Model):
		name = models.CharField(max_length=100)
		price = models.DecimalField(
			max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)]
		)
	```

- **Field Options**: Use additional options like `unique`, `db_index`, `choices`, and `default`.

	```python
	class Employee(models.Model):
		EMPLOYEE_TYPES = [
			('FT', 'Full-Time'),
			('PT', 'Part-Time'),
			('CT', 'Contract'),
		]

		name = models.CharField(max_length=100)
		employee_type = models.CharField(
			max_length=2, choices=EMPLOYEE_TYPES, default='FT'
		)
		email = models.EmailField(unique=True)
		hired_date = models.DateField(auto_now_add=True, db_index=True)
	```

---

## 8. Advanced Database Management

In addition to basic database interactions, Django provides features for advanced database management, such as connection pooling, multiple database configurations, database routing, and transaction management. These capabilities are essential for building scalable and robust applications.

### Database Connection Pooling

Connection pooling reuses database connections rather than opening a new one for each request, improving performance and resource utilization.

- **Using `django-db-geventpool`**: This package enables database connection pooling with support for gevent.
	
	```bash
	pip install django-db-geventpool
	```

	Update your `DATABASES` setting in `settings.py`:

	```python
	DATABASES = {
		'default': {
			'ENGINE': 'django_db_geventpool.backends.postgresql_psycopg2',
			'NAME': 'mydatabase',
			'USER': 'myuser',
			'PASSWORD': 'mypassword',
			'HOST': 'localhost',
			'PORT': '5432',
			'CONN_MAX_AGE': 0,  # Use 0 to utilize connection pooling
			'OPTIONS': {
				'MAX_CONNS': 20,  # Maximum number of connections in the pool
			},
		}
	}
	```

### Multiple Database Configuration

Django allows you to define and interact with multiple databases within a single project. This is useful for load balancing, separating reads and writes, or integrating legacy databases.

#### Defining Multiple Databases

In `settings.py`, define additional databases:

```python
DATABASES = {
	'default': {  # Primary database
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'primary_db',
		# Other connection parameters
	},
	'replica': {  # Secondary database
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'replica_db',
		# Other connection parameters
	},
}
```

#### Database Routers

Create a database router to control database operations:

```python
# myapp/db_routers.py
class DatabaseRouter:
	def db_for_read(self, model, **hints):
		return 'replica'  # Route all read operations to the replica database

	def db_for_write(self, model, **hints):
		return 'default'  # Route all write operations to the default database

	def allow_migrate(self, db, app_label, model_name=None, **hints):
		return True  # Allow migrations on all databases
```

Register the router in `settings.py`:

```python
DATABASE_ROUTERS = ['myapp.db_routers.DatabaseRouter']
```

### Transaction Management

Django provides tools for managing database transactions to ensure data integrity.

#### Using Transactions

Wrap database operations within an atomic transaction:

```python
from django.db import transaction

def some_view(request):
	with transaction.atomic():
		# All operations inside this block are executed in a single transaction
		# If an error occurs, the transaction is rolled back
		account.withdraw(100)
		account.save()
```

#### Setting Isolation Levels

Adjust the transaction isolation level in the database settings:

```python
DATABASES = {
	'default': {
		# ...
		'OPTIONS': {
			'isolation_level': 'serializable',
		},
	},
}
```

### Connection Handling
Manage database connections effectively:


- **Closing Connections**: Django automatically closes database connections at the end of each request. For long-running processes, manually close connections using:

	```python
	from django.db import close_old_connections

	def long_running_task():
		# ... your code ...
		close_old_connections()
	```

- **Connection Lifetime**: Adjust `CONN_MAX_AGE` in `DATABASES` to control the lifetime of persistent connections.

---

## 9. Migrations

In Django, **migrations** are a way of managing and tracking changes in your database schema as your models evolve. As you modify model definitions—such as adding fields, creating new models, or altering existing relationships—Django uses migrations to automatically translate these changes into database commands that update the underlying database structure.

Migrations are essential for keeping your database in sync with your model definitions and ensuring that changes are applied consistently across different environments (like development, testing, and production).

### Understanding Django’s Migration System

Django’s migration system operates in two main steps:

1. **Creating Migration Files**: These files describe the changes made to your models and are stored in your Django app’s migrations directory.

2. **Applying Migrations**: This step executes the changes defined in the migration files, altering the actual database schema.

#### Step 1: Creating Migration Files

Whenever you make changes to your models (for example, adding a new field, modifying a field type, or creating a new model), you need to create a migration file. This file contains the instructions Django will use to apply the model changes to your database.

To create a migration file, use the following command:

```bash
python3 manage.py makemigrations
```

This command:

- Scans all of your models for any changes.

- Generates a migration file in each app’s `migrations` folder for any models that have been modified.

- Names the file with a sequential number and a description (e.g., `0001_initial.py` for the first migration or `0002_add_email_field.py` if you added an email field).

Each migration file includes a **list of operations** that Django will execute when you apply the migration. Here’s an example of what a simple migration file might look like:

```python
# Generated migration file in myapp/migrations/0002_add_email_field.py

from django.db import migrations, models

class Migration(migrations.Migration):

	dependencies = [
		('myapp', '0001_initial'),
	]

	operations = [
		migrations.AddField(
			model_name='person',
			name='email',
			field=models.EmailField(max_length=254, unique=True),
		),
	]
```

In this example:

- `dependencies` specify the migration(s) that must be applied before this one. Here, it depends on `0001_initial`, meaning it needs the initial schema setup.

- `operations` define what changes are made in this migration. In this case, it adds an `email` field to the `Person` model.

#### Step 2: Applying Migrations

Once migration files are created, you apply them to the database with the following command:

```bash
python3 manage.py migrate
```

The `migrate` command:

- Reads the migration files in each app’s `migrations` folder.

- Checks the database to see which migrations have already been applied (tracking this in a special `django_migrations` table).

- Applies any migrations that haven’t yet been applied to update the database schema.

Applying migrations is crucial because it ensures the database matches your current models, preventing runtime errors and data integrity issues.

### How Migrations Work Internally

Django’s migration system keeps track of each migration in a special database table called `django_migrations`. This table stores the names of applied migrations, so Django knows which migrations are pending. When you run `migrate`, Django only applies migrations that haven’t been applied yet, which keeps everything in sync without re-running previous migrations.

### Example of Creating and Applying Migrations

Let’s say you start with a simple `Person` model:

```python
# myapp/models.py
from django.db import models

class Person(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
```

1. **Initial Migration**: After creating this model, you generate an initial migration file.

	```bash
	python3 manage.py makemigrations
	```
	Django will create a migration file `0001_initial.py` that defines the creation of the `Person` table with `name` and `age` fields.

2. **Applying Initial Migration**: Apply the migration to create the initial schema in the database.

	```bash
	python3 manage.py migrate
	```
	Now, the `Person` table is created in the database with columns for `name` and `age`.

3. **Adding a Field**: Suppose you add an email field to the Person model:

	```python
	# myapp/models.py
	class Person(models.Model):
		name = models.CharField(max_length=100)
		age = models.IntegerField()
		email = models.EmailField(unique=True)
	```

4. **Creating a New Migration**: Run `makemigrations` again to create a new migration that adds the `email` field to the `Person` model.

	```bash
	python3 manage.py makemigrations
	```
	This generates `0002_add_email_field.py` with instructions to add the `email` column.

5. **Applying the New Migration**: Finally, run `migrate` to apply this new migration to the database.

	```bash
	python3 manage.py migrate
	```
	Now, the `email` field has been added to the Person table in the database.

### Migration Dependencies

Each migration file specifies **dependencies** to ensure migrations are applied in the correct order. For example, if you create a migration to add a new field, it will depend on the initial migration that created the table. Django will only apply a migration after its dependencies have been applied.

### Rollbacks and Managing Migration States

Django migrations also support rolling back changes using the migrate command:

```bash
python3 manage.py migrate myapp 0001
```

This command reverts the `myapp` app to migration `0001`, effectively rolling back any changes made by subsequent migrations. This is useful during development if you need to backtrack after making unwanted changes.

### Types of Migration Operations

Django provides various **migration operations** to handle different types of schema changes. Some of the most common operations include:

- **AddField**: Adds a new field to an existing model/table.

- **RemoveField**: Removes a field from a model/table.

- **AlterField**: Changes the properties of an existing field (e.g., max length or nullability).

- **RenameField**: Renames a field within a model/table.

- **CreateModel**: Creates a new table in the database.

- **DeleteModel**: Deletes an entire table from the database.

These operations are automatically generated by makemigrations based on changes in the model definitions.

### Benefits of Django Migrations

1. **Version Control for Database Schema**: Migrations provide a clear history of database schema changes, making it easy to track, review, and apply changes across different environments.

2. **Collaboration**: Migrations are tracked in version control (e.g., Git), so developers working on the same project can share schema changes.

3. **Automated Schema Management**: Migrations handle complex schema updates, such as adding fields or altering relationships, automatically. This reduces manual SQL writing and helps prevent human errors.

---

## 10. Django Admin Panel

Django’s **admin panel** is a built-in interface for managing your application's data, providing a simple GUI to view, add, update, and delete records from the database. It’s ideal for internal use, allowing non-technical users to interact with the data without requiring SQL knowledge or custom views.

### Enabling the Admin Panel

To activate the admin panel, register your models in `admin.py` for each app. Django automatically generates CRUD (Create, Read, Update, Delete) operations for all registered models.

1. **Registering Models in the Admin Interface**

	To make a model accessible in the admin, import it in `admin.py` and register it with Django’s `admin.site.register()` function.

	```python
	# myapp/admin.py
	from django.contrib import admin
	from .models import Person
		
	admin.site.register(Person)
	```

	In this example, `Person` will now be visible in the admin panel.

2. **Accessing the Admin Interface**

	The admin interface is available at `http://127.0.0.1:8000/admin`. Before accessing it, create a superuser (admin account) to log in:

	```bash
	python3 manage.py createsuperuser
	```

	You’ll be prompted to set a username, email, and password for the superuser.

### Customizing the Admin Panel

The Django admin panel can be customized to control how models and data are displayed:

1. **Displaying Specific Fields in List View**

	Use `list_display` in a custom `ModelAdmin` class to specify fields shown in the list view.

	```python
	# myapp/admin.py
	class PersonAdmin(admin.ModelAdmin):
		list_display = ('name', 'age', 'email')
		
	admin.site.register(Person, PersonAdmin)
	```

2. **Adding Filters and Search Fields**

	- `list_filter`: Adds filters in the admin panel sidebar.
	- `search_fields`: Allows search functionality across specified fields.

	```python
	class PersonAdmin(admin.ModelAdmin):
		list_display = ('name', 'age', 'email')
		list_filter = ('age',)			  # Adds a filter for 'age'
		search_fields = ('name', 'email')   # Enables search by 'name' and 'email'

	admin.site.register(Person, PersonAdmin)
	```

3. **Fieldsets and Inline Models**

	You can organize fields into sections using `fieldsets`, and display related models within a parent model using `InlineModelAdmin`.
	```python
	class PersonAdmin(admin.ModelAdmin):
		fieldsets = (
			('Personal Info', {'fields': ('name', 'email')}),
			('Additional Info', {'fields': ('age',)}),
		)
	```
Django’s admin panel can be a powerful tool for managing data, enabling robust customization without much additional code.

---

## 11. Forms and User Input

Forms in Django simplify data collection and validation by offering built-in tools to handle both user-generated and internal data entry. Django forms can be created manually or generated directly from models.

### Creating Forms Manually

Manual forms provide flexibility and can be created by defining fields and validation logic.

```python
# myapp/forms.py
from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea)
```

### ModelForm: Generating Forms from Models

ModelForm is a form created directly from a Django model, which makes it easy to handle model instances in forms.

```python
from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
	class Meta:
		model = Person
		fields = ['name', 'age', 'email']
```

### Handling Form Submission

To process form data, views in Django typically:

1. Instantiate the form with request data (`POST`).

2. Validate the data (`form.is_valid()`).

3. Save the form data if valid.

```python
# myapp/views.py
from django.shortcuts import render, redirect
from .forms import PersonForm

def add_person(request):
	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('person_list')  # Redirect after saving
	else:
		form = PersonForm()
	return render(request, 'add_person.html', {'form': form})
```

In this example:

- A form instance is created with `request.POST` data.

- Upon validation, `form.save()` inserts the data into the database.

- `redirect` sends the user to another page upon successful submission.

Django forms provide a simple, yet powerful, way to collect and process user input, with the advantage of automatic validation.

---

## 12. Django QuerySet API

The QuerySet API is Django’s powerful tool for querying databases. It abstracts SQL operations, enabling complex data retrieval and manipulation through Python code. Each QuerySet represents a collection of database rows, allowing developers to chain filters, perform aggregations, and retrieve specific data.

### Basic QuerySet Methods

1. **Retrieving All Records**

	```python
	people = Person.objects.all()
	```

2. **Filtering Records**
		
	Filters retrieve records that meet specified conditions, supporting lookups such as `exact`, `iexact` (case-insensitive), and `contains`.

	```python
	adults = Person.objects.filter(age__gte=18)  # People aged 18 or older
	```

3. **Excluding Records**

	Exclude specific records based on conditions.

	```python
	non_adults = Person.objects.exclude(age__gte=18)
	```

4. **Ordering Results**

	Order records by one or more fields. Prefix the field with a hyphen (`-`) for descending order.

	```python
	ordered_people = Person.objects.order_by('name')  # Ascending by name
	```

5. **Limiting Results**

	QuerySets are lazy, meaning they don’t retrieve data until explicitly requested. Use slicing to limit records, like with lists.

	```python
	first_five_people = Person.objects.all()[:5]  # Retrieves the first 5 records
	```

### Aggregation and Annotation

Aggregations compute summary values across records, like `Count`, `Sum`, and `Average`.

```python
from django.db.models import Avg

average_age = Person.objects.aggregate(Avg('age'))  # Average age of all people
```

### Common QuerySet Lookups

Django offers a wide range of lookups for flexibility:

- `__gte` and `__lte`: Greater than or equal to, less than or equal to.

- `__icontains`: Case-insensitive substring match.

- `__in`: Checks if a value is within a specified list.

For instance, to get all `Person` records where the name contains “John” (case-insensitive):

```python
johns = Person.objects.filter(name__icontains='john')
```

The QuerySet API in Django is versatile and provides the power to query data efficiently without writing raw SQL, supporting a wide range of applications from simple CRUD to complex analytics.

---

## 13. Class-Based Views (CBVs)

Class-Based Views (CBVs) in Django provide a structured, reusable way to create views that require similar logic across multiple parts of an application. Django offers built-in CBVs, such as `ListView`, `DetailView`, `CreateView`, `UpdateView`, and `DeleteView`, simplifying CRUD operations.

### Built-in Class-Based Views

Django’s generic CBVs handle many common tasks out of the box:

1. **ListView**: Displays a list of objects.

2. **DetailView**: Shows details of a single object.

3. **CreateView**: Provides a form to create a new object.

4. **UpdateView**: Renders a form to update an existing object.

5. **DeleteView**: Confirms and deletes an object.

### Example of a ListView

To display a list of `Person` objects:

```python
# myapp/views.py
from django.views.generic import ListView
from .models import Person

class PersonListView(ListView):
	model = Person
	template_name = 'person_list.html'
	context_object_name = 'people'
```

### Example of a CreateView

To create a new Person record using a form:

```python
# myapp/views.py
from django.views.generic.edit import CreateView
from .models import Person

class PersonCreateView(CreateView):
	model = Person
	fields = ['name', 'age', 'email']
	template_name = 'person_form.html'
	success_url = '/people/'  # Redirect URL after successful submission
```

### Using CBVs in URL Configuration

To connect a CBV to a URL, use `.as_view()` in `urls.py`:

```python
# myapp/urls.py
from django.urls import path
from .views import PersonListView, PersonCreateView

urlpatterns = [
	path('people/', PersonListView.as_view(), name='person_list'),
	path('people/add/', PersonCreateView.as_view(), name='person_add'),
]
```

### CBV Advantages Over FBVs

- **Reusability**: CBVs allow inheritance and can be extended to share common logic.

- **Cleaner Code**: CBVs often reduce boilerplate, especially for CRUD operations.

- **Modularity**: Easily handles different HTTP methods within the same class (e.g., GET, POST).

CBVs provide a powerful way to manage views, particularly for CRUD operations, by encapsulating functionality into reusable classes.

---

## 14. Middleware

Middleware in Django provides a way to process requests and responses globally before they reach views or are sent back to the client. Middleware can be used for cross-cutting concerns like authentication, logging, request throttling, or handling custom headers. Middleware functions execute in a sequence, allowing different levels of access and modification throughout the request-response lifecycle.

### Purpose and Usage of Middleware

Middleware components in Django operate at various stages of the request-response cycle:

1. **Pre-processing**: Middleware can modify requests before they reach the view, often used to enforce security checks or user authentication.

2. **Post-processing**: Middleware can modify responses before they are sent back to the client, useful for adding headers or handling response formats.

Django provides built-in middleware options for common use cases, such as managing sessions and handling CSRF protection, and also supports custom middleware for more specific needs.

### Commonly Used Built-in Middleware

Here are some of the most frequently used middleware classes in Django, which can be enabled in the `MIDDLEWARE` section of `settings.py`:

```python
# settings.py
MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
### Overview of Key Middleware

- **SecurityMiddleware**: Enforces security settings, such as HTTPS redirection and secure cookies.

- **SessionMiddleware**: Manages user sessions by storing data on the server side.

- **AuthenticationMiddleware**: Associates requests with logged-in users, enabling access control.

- **CSRF Middleware**: Protects against cross-site request forgery by ensuring that forms include a unique token for secure form submissions.

### Creating Custom Middleware

To create custom middleware, define a class with methods for request and response processing. Place the middleware class in an appropriate file, like `middleware.py` within your app.

Here’s an example of custom middleware that adds a custom header to all responses:

```python
# myapp/middleware.py
class CustomHeaderMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)
		response['X-Custom-Header'] = 'Custom Value'
		return response
```

To register it, add the middleware class to the `MIDDLEWARE` list in `settings.py`:

```python
# settings.py
MIDDLEWARE.append('myapp.middleware.CustomHeaderMiddleware')
```

### Types of Middleware and Their Use Cases

1. **Request Handling**: Modifying requests before they reach views, such as checking authentication or logging requests.

2. **Response Handling**: Modifying responses before they are returned, like adding headers or altering formats.

3. **Exception Handling**: Catching and handling exceptions that occur in views, which can be used for custom error handling.

4. **Process View Middleware**: Called just before a view is executed, allowing custom behavior like conditional view access.

5. **Process Template Response Middleware**: Operates on the response template before rendering, useful for altering or adding context data.

### Key Advantages of Middleware

Middleware provides a global layer of functionality, allowing you to enforce certain behaviors and add reusable logic across your Django application. It's particularly powerful for scenarios where multiple views or requests need to share common processing without duplicating code.

Django's middleware framework simplifies cross-cutting concerns in web applications, making it a valuable tool for implementing security, session management, and request handling across views.

---

## 15. Authentication and Authorization

Django provides a robust, built-in **authentication and authorization** system for managing users, permissions, and access control. This system includes models, views, and forms for handling user registration, login, logout, and permission-based access control.

### Core Components of Authentication in Django

1. **User Model**: Django's default `User` model represents individual users, storing attributes like `username`, `email`, `password`, `is_active`, and `is_superuser`.

	```python
	from django.contrib.auth.models import User
	```

	- **Customizing the User Model**: For more flexibility, you may need to customize the default `User` model. Django provides two options:

		- **Extending `AbstractUser`**: Inherit from `AbstractUser` to add additional fields to the default user model.

			```python
			# myapp/models.py
			from django.contrib.auth.models import AbstractUser

			class CustomUser(AbstractUser):
				phone_number = models.CharField(max_length=15, blank=True)
			```

		- **Using `AbstractBaseUser`**: Inherit from `AbstractBaseUser` to create a completely new user model with full control over fields and authentication behavior.

			```python
			# myapp/models.py
			from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
			from django.db import models

			class CustomUser(AbstractBaseUser, PermissionsMixin):
				email = models.EmailField(unique=True)
				first_name = models.CharField(max_length=30)
				last_name = models.CharField(max_length=30)

				USERNAME_FIELD = 'email'
				REQUIRED_FIELDS = ['first_name', 'last_name']

				def __str__(self):
					return self.email
			```
		
		- **Updating Settings**: When customizing the user model, update `AUTH_USER_MODEL` in `settings.py`:
			```python
			# settings.py
			AUTH_USER_MODEL = 'myapp.CustomUser'
			```

		- **Creating a Custom User Manager**: If you're using `AbstractBaseUser`, you need to define a custom user manager.

			```python
			# myapp/managers.py
			from django.contrib.auth.base_user import BaseUserManager

			class CustomUserManager(BaseUserManager):
				def create_user(self, email, password, **extra_fields):
					if not email:
						raise ValueError('The Email field must be set')
					email = self.normalize_email(email)
					user = self.model(email=email, **extra_fields)
					user.set_password(password)
					user.save()
					return user

				def create_superuser(self, email, password, **extra_fields):
					extra_fields.setdefault('is_staff', True)
					extra_fields.setdefault('is_superuser', True)

					if extra_fields.get('is_staff') is not True:
						raise ValueError('Superuser must have is_staff=True.')
					if extra_fields.get('is_superuser') is not True:
						raise ValueError('Superuser must have is_superuser=True.')

					return self.create_user(email, password, **extra_fields)
			```

			And link it to your custom user model:
			
			```python
			# myapp/models.py
			class CustomUser(AbstractBaseUser, PermissionsMixin):
				# ... fields ...
				objects = CustomUserManager()
				# ... rest of the model ...
			```

2. **Authentication Views**: Django includes built-in views for login, logout, and password management. These views can be used out of the box or customized as needed.

	- **LoginView**: Handles user login.

		```python
		# myapp/urls.py
		from django.urls import path
		from django.contrib.auth import views as auth_views

		urlpatterns = [
			path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
			path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
		]
		```

	- **LogoutView**: Logs out the user and redirects to the specified page.

3. **User Registration**:

	Implement user registration using a custom view and form:

	```python
	# myapp/forms.py
	from django import forms
	from django.contrib.auth import get_user_model

	User = get_user_model()

	class SignUpForm(forms.ModelForm):
		password = forms.CharField(widget=forms.PasswordInput)
		confirm_password = forms.CharField(widget=forms.PasswordInput)

		class Meta:
			model = User
			fields = ['email', 'first_name', 'last_name', 'password']

		def clean(self):
			cleaned_data = super().clean()
			password = cleaned_data.get('password')
			confirm_password = cleaned_data.get('confirm_password')

			if password and confirm_password and password != confirm_password:
				self.add_error('confirm_password', 'Passwords do not match.')
	```
	```python
	# myapp/views.py
	from django.shortcuts import render, redirect
	from .forms import SignUpForm

	def signup(request):
		if request.method == 'POST':
			form = SignUpForm(request.POST)
			if form.is_valid():
				user = form.save(commit=False)
				user.set_password(form.cleaned_data['password'])
				user.save()
				return redirect('login')
		else:
			form = SignUpForm()
		return render(request, 'signup.html', {'form': form})
	```

	- **URLs Configuration**:

		```python
		# myapp/urls.py
		urlpatterns += [
			path('signup/', signup, name='signup'),
		]
		```

4. **Password Reset and Email Verification**:

	- **Password Reset**: Django provides built-in views and forms for password reset via email.
		```python
		# myapp/urls.py
		from django.urls import path
		from django.contrib.auth import views as auth_views

		urlpatterns += [
			path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
			path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
			path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
			path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
		]
		```

		- **Email Backend Configuration**: Ensure email settings are configured in settings.py:
			```python
			# settings.py
			EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
			EMAIL_HOST = 'smtp.gmail.com'
			EMAIL_PORT = 587
			EMAIL_USE_TLS = True
			EMAIL_HOST_USER = 'your_email@example.com'
			EMAIL_HOST_PASSWORD = 'your_email_password'
			```
	
	- **Email Verification**: Implement email verification during user registration to confirm user emails.

		- **Using Third-Party Packages**: Packages like `django-allauth` can simplify email verification.

			```bash
			pip install django-allauth
			```
			
			- **Configure Installed Apps**:

				```python
				# settings.py
				INSTALLED_APPS += [
					'django.contrib.sites',
					'allauth',
					'allauth.account',
					'allauth.socialaccount',
				]
				SITE_ID = 1
				```
			
			- **Include URLs**:

				```python
				# project_root/urls.py
				urlpatterns += [
					path('accounts/', include('allauth.urls')),
				]
				```

		- **Custom Implementation**: Manually send verification emails with tokens.

			- **Generate Token and Send Email**:

				```python
				# myapp/views.py
				from django.contrib.auth.tokens import default_token_generator
				from django.template.loader import render_to_string
				from django.utils.http import urlsafe_base64_encode
				from django.utils.encoding import force_bytes
				from django.urls import reverse

				def send_verification_email(request, user):
					token = default_token_generator.make_token(user)
					uid = urlsafe_base64_encode(force_bytes(user.pk))
					verification_link = request.build_absolute_uri(
						reverse('email_verification_confirm', kwargs={'uidb64': uid, 'token': token})
					)
					subject = 'Email Verification'
					message = render_to_string('email_verification_email.html', {'verification_link': verification_link})
					user.email_user(subject, message)
				```
			
			- **Verification View**:

				```python
				# myapp/views.py
				from django.contrib.auth import get_user_model
				from django.contrib.auth.tokens import default_token_generator
				from django.utils.http import urlsafe_base64_decode

				User = get_user_model()

				def email_verification_confirm(request, uidb64, token):
					uid = urlsafe_base64_decode(uidb64).decode()
					user = User.objects.get(pk=uid)

					if default_token_generator.check_token(user, token):
						user.is_active = True
						user.save()
						return redirect('login')
					else:
						# Invalid token
						return render(request, 'email_verification_invalid.html')
				```

			- **URL Configuration**:

				```python
				# myapp/urls.py
				urlpatterns += [
					path('email-verification/<uidb64>/<token>/', email_verification_confirm, name='email_verification_confirm'),
				]
				```

5. **Restricting Access to Views**:

	- **Using `@login_required` Decorator**: Restrict access to authenticated users.

		```python
		from django.contrib.auth.decorators import login_required

		@login_required
		def dashboard(request):
			return render(request, 'dashboard.html')
		```

		- **Redirecting Unauthenticated Users**: By default, users are redirected to the URL specified in `LOGIN_URL` (default is `/accounts/login/`).

			```python
			# settings.py
			LOGIN_URL = '/login/'
			```
	
	- **Class-Based Views**: Use `LoginRequiredMixin`.
	
		```python
		from django.contrib.auth.mixins import LoginRequiredMixin
		from django.views.generic import TemplateView

		class DashboardView(LoginRequiredMixin, TemplateView):
			template_name = 'dashboard.html'
			login_url = '/login/'  # Optional: override LOGIN_URL setting
		```

6. **Permissions and Authorization**:

	Django's permission framework allows you to define fine-grained access control.

	- **Model-Level Permissions**: Control access to entire models.

		- **Default Permissions**: Django automatically creates `add`, `change`, `delete`, and `view` permissions for each model.

		- **Custom Permissions**: Define additional permissions in the model's `Meta` class.

			```python
			# myapp/models.py
			class Document(models.Model):
				title = models.CharField(max_length=100)
				content = models.TextField()

				class Meta:
					permissions = [
						('can_publish', 'Can Publish Documents'),
					]
			```

	- **Checking Permissions in Views**:

		- **Using Decorators**:

			```python
			from django.contrib.auth.decorators import permission_required

			@permission_required('myapp.can_publish', raise_exception=True)
			def publish_document(request):
				# View logic
				pass
			```

		- **Class-Based Views**:

			```python
			from django.contrib.auth.mixins import PermissionRequiredMixin
			from django.views.generic import View

			class PublishDocumentView(PermissionRequiredMixin, View):
				permission_required = 'myapp.can_publish'
				raise_exception = True

				def get(self, request):
					# View logic
					pass
			```
	
	- **Object-Level Permissions**:

		For per-object permissions, use third-party packages like django-guardian.

		- **Installation**:
			
			```bash
			pip install django-guardian
			```

		- **Configuration**:
			
			```python
			# settings.py
			INSTALLED_APPS += ['guardian']
			AUTHENTICATION_BACKENDS = [
				'django.contrib.auth.backends.ModelBackend',  # Default
				'guardian.backends.ObjectPermissionBackend',
			]
			ANONYMOUS_USER_ID = -1
			```

		- **Assigning Permissions**:
			
			```python
			from guardian.shortcuts import assign_perm

			# Assign 'change_document' permission to a user for a specific document
			assign_perm('myapp.change_document', user, document)
			```

		- **Checking Object Permissions**:

			```python
			from guardian.mixins import PermissionRequiredMixin

			class EditDocumentView(PermissionRequiredMixin, View):
				permission_required = 'myapp.change_document'
				accept_global_perms = False  # Only object-level perms

				def get_object(self):
					return Document.objects.get(pk=self.kwargs['pk'])

				def has_permission(self):
					obj = self.get_object()
					return self.request.user.has_perm('myapp.change_document', obj)
			```

7. **Anonymous and Authenticated Users**

	- **AnonymousUser**: Represents users who are not logged in. Behaves like a `User` object but with limited permissions.

		```python
		if request.user.is_anonymous:
			# Handle anonymous user
			pass
		```
	
	- **Authenticated Users**: Accessed via `request.user`, representing the logged-in user.

8. **Groups and Permissions**:

	- **Groups**: Collections of users to which permissions can be assigned, simplifying permission management.

		```python
		from django.contrib.auth.models import Group

		# Create a group
		editors = Group.objects.create(name='Editors')

		# Assign permissions to the group
		from django.contrib.auth.models import Permission
		can_edit = Permission.objects.get(codename='change_article')
		editors.permissions.add(can_edit)

		# Add users to the group
		user.groups.add(editors)
		```

9. **Backends and Custom Authentication**:

	- **Authentication Backends**: Control how users are authenticated. Django uses ModelBackend by default.

	- **Custom Authentication Backend**: Implement custom logic for authentication.

		```python
		# myapp/auth_backends.py
		from django.contrib.auth.backends import BaseBackend
		from django.contrib.auth import get_user_model

		User = get_user_model()

		class EmailBackend(BaseBackend):
			def authenticate(self, request, email=None, password=None, **kwargs):
				try:
					user = User.objects.get(email=email)
				except User.DoesNotExist:
					return None
				if user.check_password(password):
					return user
				return None

			def get_user(self, user_id):
				try:
					return User.objects.get(pk=user_id)
				except User.DoesNotExist:
					return None
		```

		- **Update Settings**:

			```python
			# settings.py
			AUTHENTICATION_BACKENDS = ['myapp.auth_backends.EmailBackend']
			```

10. **Middleware for Authentication**:

	- **AuthenticationMiddleware**: Associates users with requests using sessions.

		- Ensure `AuthenticationMiddleware` is included in `MIDDLEWARE`:

			```python
			# settings.py
			MIDDLEWARE = [
				# ... other middleware ...
				'django.contrib.auth.middleware.AuthenticationMiddleware',
				# ... other middleware ...
			]
			```

11. **Login and Logout Redirection**:

	- `LOGIN_REDIRECT_URL`: The URL to redirect to after a successful login.

		```python
		# settings.py
		LOGIN_REDIRECT_URL = '/dashboard/'
		```
	
	- `LOGOUT_REDIRECT_URL`: The URL to redirect to after a logout.

		```python
		# settings.py
		LOGOUT_REDIRECT_URL = '/login/'
		```

12. **Session Security**:

	- **Session Expiry**: Control how long a session remains active.

		```python
		# settings.py
		SESSION_COOKIE_AGE = 1209600  # Two weeks, in seconds
		SESSION_EXPIRE_AT_BROWSER_CLOSE = False
		```
	
	- **Secure Cookies**: Enhance security by ensuring cookies are only sent over HTTPS.

		```python
		# settings.py
		SESSION_COOKIE_SECURE = True
		CSRF_COOKIE_SECURE = True
		```

---

## 16. OAuth2.0 Implementation

OAuth2.0 is an open standard for access delegation, commonly used to grant websites or applications access to user information on other websites without giving them the passwords. Implementing OAuth2.0 enhances security and allows your Django application to interact with third-party services.

### Installing `django-oauth-toolkit`

The `django-oauth-toolkit` package provides OAuth2.0 support for Django applications.

#### Installation

```bash
pip install django-oauth-toolkit
```

#### Configuration

1. **Add to Installed Apps**

	```python
	# settings.py
	INSTALLED_APPS += [
		'oauth2_provider',
	]
	```

2. **Include URLs**

	```python
	# project_root/urls.py
	from django.urls import include, path

	urlpatterns = [
		# ... existing url patterns
		path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
	]
	```

3. **Apply Migrations**

	```bash
	python manage.py migrate
	```

#### Setting Up an OAuth2 Provider

Create an application to generate client credentials:

1. **Access the Admin Panel**

	Navigate to `http://127.0.0.1:8000/admin/` and log in with your superuser account.

2. **Register a New Application**

- Go to **"Applications"** under **"OAuth2 Provider"**.

- Click **"ADD APPLICATION"**.

- Fill out the form with the necessary details (e.g., client type, authorization grant type).

#### Protecting API Endpoints

Use the provided decorators or authentication classes to protect your views:

```python
# myapp/views.py
from oauth2_provider.decorators import protected_resource
from django.http import JsonResponse

@protected_resource()
def api_resource(request):
	data = {'message': 'This is a protected resource'}
	return JsonResponse(data)
```

#### Configuring Grant Types and Tokens

Customize OAuth2.0 settings:

```python
# settings.py
OAUTH2_PROVIDER = {
	'ACCESS_TOKEN_EXPIRE_SECONDS': 3600,
	'REFRESH_TOKEN_EXPIRE_SECONDS': 86400,
	'AUTHORIZATION_CODE_EXPIRE_SECONDS': 300,
	'ALLOWED_GRANT_TYPES': [
		'authorization-code',
		'password',
		'client-credentials',
		'implicit',
		'refresh-token',
	],
	'SCOPES': {'read': 'Read scope', 'write': 'Write scope'},
}
```

#### Integrating with DRF

If you're using Django REST Framework, integrate OAuth2.0 authentication:

```python
# settings.py
REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
	),
	'DEFAULT_PERMISSION_CLASSES': (
		'rest_framework.permissions.IsAuthenticated',
	),
}
```

---

## 17. Two-Factor Authentication (2FA) Implementation

Two-Factor Authentication (2FA) adds an extra layer of security by requiring users to provide two forms of identification before accessing their accounts. Implementing 2FA in your Django application enhances security and protects against unauthorized access.

### Installing `django-two-factor-auth`

The `django-two-factor-auth` package provides comprehensive 2FA support.

#### Installation

```bash
pip install django-two-factor-auth
```

#### Configuration

1. **Add to Installed Apps**

	```python
	# settings.py
	INSTALLED_APPS += [
		'django_otp',
		'django_otp.plugins.otp_static',
		'django_otp.plugins.otp_totp',
		'two_factor',
	]
	```

2. **Add Middleware**

	```python
	# settings.py
	MIDDLEWARE += [
		'django_otp.middleware.OTPMiddleware',
	]
	```

3. **Include URLs**

	```python
	# project_root/urls.py
	from django.urls import include, path

	urlpatterns = [
		# ... existing url patterns
		path('', include('two_factor.urls', 'two_factor')),
	]
	```

4. **Update Authentication Backends**

	Ensure that the authentication backends support 2FA:

	```python
	# settings.py
	AUTHENTICATION_BACKENDS = [
		'django.contrib.auth.backends.ModelBackend',
	]
	```

#### Setting Up 2FA Methods

- **Time-Based One-Time Password (TOTP)**: Users can scan a QR code with an authenticator app (e.g., Google Authenticator) to set up TOTP.

- **Backup Tokens**: Users can generate backup codes in case they lose access to their primary device.

#### Enforcing 2FA for Users

Apply mixins or decorators to views that require 2FA:

```python
from django.views.generic import TemplateView
from two_factor.views import OTPRequiredMixin

class ProtectedView(OTPRequiredMixin, TemplateView):
	template_name = 'protected.html'
```

For function-based views:

```python
from two_factor.decorators import otp_required

@otp_required
def protected_view(request):
	# Your view logic
	pass
```

#### Configuring SMS or Call Gateways (Optional)

If you want to support SMS or phone call verification:

- **Choose a Backend**: Use third-party services like Twilio.

- **Configure the Backend**:

	```python
	# settings.py
	TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.twilio.gateway.Twilio'
	TWILIO_ACCOUNT_SID = 'your_account_sid'
	TWILIO_AUTH_TOKEN = 'your_auth_token'
	TWILIO_CALLER_ID = '+1234567890'
	```

---

## 18. Signals

Django signals provide a way for components to get notified when certain events occur elsewhere in the framework. They allow decoupled components to “listen” for events and trigger specific actions without requiring direct calls.

### Commonly Used Signals

1. `post_save` and `pre_save`: Triggered before or after saving an object.

2. `post_delete` and `pre_delete`: Triggered before or after deleting an object.

3. `m2m_changed`: Triggered when a many-to-many relationship is modified.

### Example: Using `post_save` Signal to Send a Notification

Let’s create a `post_save` signal that sends an email notification each time a new `Person` instance is saved.

```python
# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Person

@receiver(post_save, sender=Person)
def send_notification(sender, instance, created, **kwargs):
	if created:
		send_mail(
			'New Person Added',
			f'A new person, {instance.name}, has been added.',
			'admin@example.com',
			['admin@example.com'],
			fail_silently=False,
		)
```

### Registering Signals in `apps.py`

To ensure signals are registered, import the `signals.py` file in your app’s `apps.py`:

```python
# myapp/apps.py
from django.apps import AppConfig

class MyAppConfig(AppConfig):
	name = 'myapp'

	def ready(self):
		import myapp.signals  # Import signals when the app is ready
```

And then set `default_app_config` in `__init__.py`:

```python
# myapp/__init__.py
default_app_config = 'myapp.apps.MyAppConfig'
```

Django signals are an efficient way to handle loosely coupled event-based logic, enabling you to extend your app’s functionality in response to database actions without modifying core code.

---

## 19. Testing in Django

Django’s testing framework provides tools for writing and running tests to ensure your code works as expected. It includes test cases for views, models, and forms, making it easier to validate and maintain code quality.

### Writing Unit Tests with `TestCase`

Django’s `TestCase` class provides a clean setup for testing models and views.

1. **Testing Models**

	You can test model behaviors, such as default values or field constraints, by creating objects and asserting expected results.

	```python
	# myapp/tests.py
	from django.test import TestCase
	from .models import Person

	class PersonModelTest(TestCase):
		def setUp(self):
			self.person = Person.objects.create(name="Alice", age=30)

		def test_person_creation(self):
			self.assertEqual(self.person.name, "Alice")
			self.assertEqual(self.person.age, 30)
	```

2. **Testing Views**

	Test views by simulating requests and asserting the correct templates or responses.

	```python
	from django.urls import reverse

	class PersonListViewTest(TestCase):
		def test_view_url_exists_at_desired_location(self):
			response = self.client.get('/people/')
			self.assertEqual(response.status_code, 200)
			self.assertTemplateUsed(response, 'person_list.html')
	```

3. **Testing Forms**

	Test form validation and data handling using Django’s `Form` class.

	```python
	from .forms import PersonForm

	class PersonFormTest(TestCase):
		def test_form_valid_data(self):
			form = PersonForm(data={'name': 'Alice', 'age': 30})
			self.assertTrue(form.is_valid())
	```			

4. **Running Tests**

	Run all tests using:

	```bash
	python3 manage.py test
	```

Testing helps ensure that changes do not introduce new issues and maintains a high-quality codebase over time.

---

## 20. Django REST Framework (DRF) Introduction

The Django REST Framework (DRF) is a toolkit for building APIs with Django. It simplifies API development with tools for serialization, authentication, and view organization.

### Key Components in DRF

1. **Serializers**: Convert complex data (like model instances) into JSON format and vice versa.

2. **ViewSets**: Encapsulate logic for handling different HTTP methods (GET, POST, PUT, DELETE) in a single class.

3. **Routers**: Automatically generate URL patterns for ViewSets, providing RESTful routing for your API.

4. **Authentication and Permissions**: DRF provides flexible authentication options and permission classes to control access to API endpoints.

5. **Throttling**: DRF supports request throttling to limit the rate of requests a client can make.

### Example: Creating a Simple API with DRF

1. **Creating a Serializer**

	Serializers are used to convert model instances to JSON format.

	```python
	# myapp/serializers.py
	from rest_framework import serializers
	from .models import Person

	class PersonSerializer(serializers.ModelSerializer):
		class Meta:
			model = Person
			fields = ['id', 'name', 'age', 'email']
	```				

2. **Defining a ViewSet**

	ViewSets define the behavior of the API endpoint, handling CRUD operations automatically.

	```python
	# myapp/views.py
	from rest_framework import viewsets
	from .models import Person
	from .serializers import PersonSerializer

	class PersonViewSet(viewsets.ModelViewSet):
		queryset = Person.objects.all()
		serializer_class = PersonSerializer
	```

3. **Configuring URLs with a Router**

	Routers automatically create URLs for your ViewSet, simplifying routing setup.

	```python
	# myapp/urls.py
	from rest_framework.routers import DefaultRouter
	from .views import PersonViewSet

	router = DefaultRouter()
	router.register(r'people', PersonViewSet)

	urlpatterns = router.urls
	```

### API Authentication and Permissions

DRF supports multiple authentication methods and provides permission classes to restrict access.

#### Authentication Methods

Configure the authentication classes in `settings.py`:

```python
# settings.py
REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': [
		'rest_framework.authentication.SessionAuthentication',  # Uses Django's session framework
		'rest_framework.authentication.BasicAuthentication',
	],
	'DEFAULT_PERMISSION_CLASSES': [
		'rest_framework.permissions.IsAuthenticated',  # Requires users to be authenticated
	],
}
```

- **SessionAuthentication**: Uses Django's session framework. Suitable for web clients that have session cookies.

- **BasicAuthentication**: Uses HTTP Basic authentication. Suitable for testing or internal APIs.

#### Permissions

Control access at the view level using permission classes.

- **IsAuthenticated**: Only authenticated users can access the view.

- **IsAdminUser**: Only admin users can access the view.

- **AllowAny**: All users can access the view.

#### Example of setting permissions in a ViewSet:

```python
from rest_framework.permissions import IsAuthenticated

class PersonViewSet(viewsets.ModelViewSet):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer
	permission_classes = [IsAuthenticated]
```

#### Custom Permissions

Create custom permission classes by subclassing `rest_framework.permissions.BasePermission`.

```python
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.owner == request.user
```

Apply the custom permission to a view:

```python
class DocumentViewSet(viewsets.ModelViewSet):
	queryset = Document.objects.all()
	serializer_class = DocumentSerializer
	permission_classes = [IsOwner]
```

### Throttling and Rate Limiting

Throttling limits the number of requests a client can make in a given time period.

#### Enabling Throttling

Configure default throttling classes in `settings.py`:

```python
# settings.py
REST_FRAMEWORK = {
	'DEFAULT_THROTTLE_CLASSES': [
		'rest_framework.throttling.UserRateThrottle',
		'rest_framework.throttling.AnonRateThrottle',
	],
	'DEFAULT_THROTTLE_RATES': {
		'user': '1000/day',      # Authenticated users can make 1000 requests per day
		'anon': '100/day',       # Unauthenticated users can make 100 requests per day
	},
}
```

#### Custom Throttling

Create custom throttle classes by subclassing `rest_framework.throttling.BaseThrottle`.

```python
from rest_framework.throttling import UserRateThrottle

class BurstRateThrottle(UserRateThrottle):
	scope = 'burst'

# settings.py
REST_FRAMEWORK['DEFAULT_THROTTLE_CLASSES'].append('myapp.throttles.BurstRateThrottle')
REST_FRAMEWORK['DEFAULT_THROTTLE_RATES']['burst'] = '10/minute'
```

### Testing the API

DRF includes an interactive web API browser that supports authentication and allows you to test your endpoints.

- Navigate to your API endpoint in a browser to access the API interface.

---

## 21. Best Practices in Django

Following best practices can help you maintain clean, efficient, and secure Django applications. Here are key guidelines:

### 1. Organize Project Structure

Django's default project layout promotes organization. Use separate apps for distinct features, keep templates and static files organized, and adhere to Django’s recommended file structure. Each app should serve a single purpose to enhance maintainability.

### 2. Use Virtual Environments

Use a virtual environment (e.g., `venv`) to isolate dependencies and avoid conflicts across projects. This also simplifies deployment and dependency management.

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Apply the DRY Principle

The **Don't Repeat Yourself (DRY)** principle helps minimize redundant code. Reuse functionality by creating reusable apps, using template inheritance, and utilizing Django’s built-in tools like `forms.ModelForm` and generic views.

### 4. Optimize Database Queries

Efficient database queries are critical to performance. Use Django’s **select_related** and **prefetch_related** methods to reduce query counts for related objects. Also, utilize indexes for frequently searched fields and monitor query efficiency using Django’s debug toolbar during development.

```python
# Example of select_related for efficient querying
books = Book.objects.select_related('author').all()
```

### 5. Write Tests

Django’s built-in testing framework allows you to write and run tests for models, views, and forms, ensuring code reliability. Start with simple tests, like checking that views load correctly, and progressively add tests for specific functionality.

```python
# Sample test
from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
	def test_string_representation(self):
		book = Book(title="Sample Book")
		self.assertEqual(str(book), book.title)
```

### 6. Manage Sensitive Information Securely

Store sensitive data, like secret keys and database credentials, in environment variables rather than in `settings.py`. Libraries like `django-environ` can help manage environment variables conveniently.

```python
# Example using django-environ
import environ
env = environ.Env()
SECRET_KEY = env("SECRET_KEY")
```

### 7. Implement Basic Security Practices

Django includes several built-in security features, but additional steps can further protect your application:

- **CSRF Protection**: Django provides CSRF protection by default.

- **HTTPS**: Use SSL/TLS in production to secure data transmission.

- **Secure Cookies**: Enable secure cookies for session and CSRF tokens.

```python
# Example settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

### 8. Use Django’s Caching Features

Caching can significantly improve performance by storing frequently accessed data temporarily. Django supports several caching backends, including in-memory, file-based, and external services like Redis or Memcached.

```python
# Example cache settings
CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION': '127.0.0.1:11211',
	}
}
```

### 9. Document Your Code

Clear documentation makes it easier for others (and future you) to understand the codebase. Use Django’s docstrings and comments effectively and provide clear README or API documentation.

### 10. Regularly Update Dependencies

Regularly check for updates to Django and any dependencies you use, as updates often include security patches and performance improvements. Use tools like `pip list --outdated` to check for updates.

---

## 22. Common Questions

### Q1: How does Django handle authentication and permissions in REST APIs?

- Django REST Framework (DRF) includes built-in classes for authentication (e.g., `BasicAuthentication`, `TokenAuthentication`) and permissions (e.g., `IsAuthenticated`, `IsAdminUser`) to control API access.

### Q2: What are the key performance optimization strategies for Django applications?

- Use caching, optimize database queries, enable database indexing, Use asynchronous requests where possible, and compress media assets.

### Q3: How do I deploy a Django application in production?

- Use a WSGI server like **Gunicorn**, a web server like **Nginx**, and a database server (PostgreSQL or MySQL). Django provides deployment guidelines for setting up your application in a secure, performant environment.

### Q4: How does Django support multi-language applications?

- Django includes **internationalization (i18n)** and **localization (l10n)** features to translate strings and adapt content to different languages. Use `gettext` for string translation and configure available languages in `settings.py`.

### Q5: How do I integrate Django with front-end frameworks like React or Vue?

- Use Django’s API capabilities through Django REST Framework (DRF) to serve data to a front-end JavaScript framework. DRF provides RESTful endpoints that front-end applications can consume.

## 23. Main Reference Links

1. [**Django Official Documentation: Django Docs**](https://docs.djangoproject.com/en/)

2. [**Django REST Framework: DRF Docs**](https://www.django-rest-framework.org/)

3. [**Real Python Django Guide: Real Python**](https://realpython.com/)