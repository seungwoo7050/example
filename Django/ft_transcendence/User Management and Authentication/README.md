# User Management and Authentication in Django

This module covers implementing user registration, login, and profile management in Django, with a focus on understanding how these features work and their purpose in a typical web application. You will explore how Django’s authentication system functions, learn about the different files used in setting up user management, and understand where user data is stored.

---

## Table of Contents

1. **Project Purpose**

2. **Requirements and Planning**

3. **Step-by-Step Code Walkthrough**

4. **Concepts**

5. **My Questions (placeholder)**

6. **Common Questions about This Project**

7. **Main Reference Links**

---

## 1. Project Purpose

In this project, you’ll learn:

- How to set up a user management system with Django’s built-in authentication features.

- The purpose of authentication and how it relates to user data security and access control.

- The process of creating user registration and profile forms that handle user data securely.

- How to link user data with a database, making it accessible through both backend and frontend interfaces.

### What is the Authentication System?

Django’s authentication system is a framework that handles essential user operations like registration, login, and password management. Its purpose is to enable secure management of user data and ensure that only authenticated users can access specific parts of the application.

- **User Management**: The system functions similarly to a membership system on typical websites, allowing users to create accounts, log in, and update their profile information.

- **Regular Users vs. Administrators**: By default, Django’s system supports both regular users and superusers (administrators). Regular users access the front end, while administrators manage the backend using Django’s admin interface.

- **Multiple User Registrations**: Django allows multiple users to register, enabling membership-like functionality similar to signing up on a regular website.

- **Front-End Integration**: The user registration and login views we create in this module are linked to the frontend templates (HTML forms), allowing users to interact with them directly.

---

## 2. Requirements and Planning

### Software Requirements

This module continues from the previous setup, so you’ll need:

- **macOS** (with Terminal)

- **Django** (from the virtual environment set up previously)

- **PostgreSQL database** (linked with your Django project via Docker as set up in the previous module)

### Key Setup Steps

1. Enable Django’s built-in authentication framework.

2. Configure and customize Django’s `User` model and registration forms.

3. Create views for registration, login, and profile management.

4. Use Django’s built-in authentication methods for handling sessions securely.

---

## 3. Step-by-Step Code Walkthrough

### Step 1: Enabling Django’s Authentication System

Django’s authentication system is an integral part of the framework and comes with features like session management, user models, and middleware for handling login status.

1. **Check Installed Apps**: In `settings.py`, ensure `django.contrib.auth` and `django.contrib.contenttypes` are included in `INSTALLED_APPS`. These modules provide essential user management and authentication features.

    ```python
    INSTALLED_APPS = [
        'django.contrib.auth',         # Handles authentication processes
        'django.contrib.contenttypes', # Manages database interactions for models
        'django.contrib.sessions',     # Tracks user sessions for secure login
        'django.contrib.messages',     # Manages notifications/messages
        'django.contrib.staticfiles',  # Manages static files (CSS, JavaScript)
        # Add the custom app we'll create next
        'user_management',
    ]
    ```

2. **Set Up Authentication URLs**: Django provides default views for login and logout that you can connect in your `urls.py` by including Django’s authentication URLs:

    ```python
    # main_project/urls.py
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('auth/', include('django.contrib.auth.urls')),  # Default login/logout views
    ]
    ```

### Step 2: Create a Custom User App

#### What is `startapp`?

When you run `python manage.py startapp user_management`, Django creates a basic app structure, which includes files like `models.py`, `views.py`, and `urls.py`. These files serve as placeholders or templates where you can define functionality, but they do not contain any built-in features. This structure is meant to organize code, allowing you to define specific logic and models for user management.

1. **Create a New App**:

    ```bash
    python manage.py startapp user_management
    ```

2. **Purpose of Each File in the App**:

    - **models.py**: Extending the `User` model can be done through a OneToOneField relationship to the existing `User` model, allowing additional customization.

    - **views.py**: Used to define the logic behind each view, such as registration and profile management.

    - **urls.py**: Used to map views to specific URL patterns, allowing users to navigate to different parts of the app.

3. **Adding the App to `INSTALLED_APPS`**: Add `user_management` to `INSTALLED_APPS` in `settings.py`, which registers the app and makes it accessible throughout your project.

    ```python
    INSTALLED_APPS = [
        # Other installed apps
        'user_management',
    ]
    ```

### Step 3: Create User Registration and Profile Forms

Forms in Django are essential for handling data input from users. Here, we’ll create forms to manage user registration and profile updates.

1. **Create a `forms.py` in `user_management`**: Define forms for registering a new user and updating an existing user profile.

    ```python
    # user_management/forms.py
    from django import forms
    from django.contrib.auth.models import User

    class UserRegistrationForm(forms.ModelForm):
        password = forms.CharField(label='Password', widget=forms.PasswordInput)
        password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

        class Meta:
            model = User
            fields = ('username', 'first_name', 'email')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don’t match.')
            return cd['password2']

    class UserEditForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ('first_name', 'last_name', 'email')
    ```
2. **Purpose of Each Form**:

    - **UserRegistrationForm**: Handles new user sign-ups. It verifies that the two entered passwords match and prepares data to be saved securely.
    
    - **UserEditForm**: Allows users to update their profile information, like first name and email address.

### Step 4: Create Views for Registration and Profile Management

In Django, views handle the logic behind each page and manage data interactions with the model and database.

1. **Define Views in `user_management/views.py`**: The registration view creates a new user account, while the profile view allows the user to update their information.

    ```python
    # user_management/views.py
    from django.shortcuts import render, redirect
    from django.contrib.auth import authenticate, login
    from .forms import UserRegistrationForm, UserEditForm

    def register(request):
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()
                login(request, new_user)
                return redirect('profile')
        else:
            form = UserRegistrationForm()
        return render(request, 'user_management/register.html', {'form': form})

    def profile(request):
        if request.method == 'POST':
            form = UserEditForm(instance=request.user, data=request.POST)
            if form.is_valid():
                form.save()
        else:
            form = UserEditForm(instance=request.user)
        return render(request, 'user_management/profile.html', {'form': form})
    ```

2. **Explanation of Each View**:

- **Register View**: Manages new user registrations. It validates form data, saves the user, and logs them in.

- **Profile View**: Manages existing user data, allowing them to update their profile details.

3. **URL Patterns in `user_management/urls.py`**: Add URL patterns to allow access to registration and profile views.

    ```python
    # user_management/urls.py
    from django.urls import path
    from . import views

    urlpatterns = [
        path('register/', views.register, name='register'),
        path('profile/', views.profile, name='profile'),
    ]
    ```

4. **Include User Management URLs in Project URLs**: Link the user management URLs with the main project’s URLs file.

    ```python
    # main_project/urls.py
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('auth/', include('django.contrib.auth.urls')),
        path('user/', include('user_management.urls')),  # Include user management routes
    ]
    ```

### Step 5: Creating and Using Templates for User Registration and Profile

Templates handle the frontend of Django’s application. They contain HTML forms for user input.

1. **Create a `register.html` Template**: The registration form template captures user input for account creation.

    ```html
    <!-- user_management/templates/user_management/register.html -->
    <h2>Register</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
    ```

2. **Create a `profile.html` Template**: The profile form template allows logged-in users to update their information.

    ```html
    <!-- user_management/templates/user_management/profile.html -->
    <h2>Profile</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
    ```

### Step 6: Verify User Management Setup

Once you’ve completed all the steps, here’s how to check if everything is working correctly:


1. **Start the Django Server**:

    ```bash
    python manage.py runserver
    ```

2. **Visit the Registration Page**:

    - Go to `http://127.0.0.1:8000/user/register/` to view the registration form.

    - Fill out the registration form to create a new user account.

3. **Check Database for New User**:

    - Open a new terminal window and run the following command to access PostgreSQL via Docker and check if the new user is stored:
        ```bash
        docker-compose exec db psql -U myuser -d mydatabase -c "SELECT * FROM auth_user;"
        ```
    
    - Verify that the new user appears in the auth_user database table.

4. **Log in and Verify Profile Update**:

- After creating the user, go to the login page (e.g., `http://127.0.0.1:8000/auth/login/`), log in, and visit the profile page at `http://127.0.0.1:8000/user/profile/`.

- Update some profile details and confirm that changes are saved in the database.

---

## 4. Concepts

### Key Concepts Covered

- Authentication and User Management: Django’s system handles secure user registration, login, and password management.

- Form Handling: Forms are used to manage data input securely, especially for sensitive information like passwords.

- Database Integration: User data is saved to PostgreSQL, allowing long-term storage and data retrieval.

---

## 5. My Questions

### 1. `urls.py` and `urlpatterns`

**Purpose of `urls.py`**: The `urls.py` file in Django manages URL routing for the project or specific app. It defines which views (webpage responses) should be rendered when a user visits a particular URL.

#### What is `urlpatterns`?

- `urlpatterns` is a Python list that maps URL patterns to their corresponding view functions. Each entry in `urlpatterns` is a route (URL) connected to a view. When a request is made to a URL, Django searches through `urlpatterns` to find a match and serves the associated view.

#### Example Structure: In `user_management/urls.py`:

```python
from django.urls import path
from . import views  # Imports the views defined in views.py

urlpatterns = [
    path('register/', views.register, name='register'),  # Maps URL /register/ to the register view
    path('profile/', views.profile, name='profile'),     # Maps URL /profile/ to the profile view
]
```

Using the `name` attribute allows easy reference to URLs without hardcoding paths, which improves code maintainability.

- `path()` takes three arguments:

1. The URL pattern (e.g., `'register/'`).

2. The view function to be called (e.g., `views.register`).

3. A unique name (e.g., `name='register'`) to refer to this URL path in templates or code.

#### Usage on the Server:

- When a user visits `http://127.0.0.1:8000/user/register/`, Django matches `register/` in `urlpatterns` to the `register` view function and executes it.

- URLs in `urlpatterns` allow you to access views consistently and dynamically link pages in templates.

### 2. `forms.py` and Form Creation

**Purpose of `forms.py`**: `forms.py` is not included by default in Django apps; you create it manually to handle form data. Forms are used to capture user input, validate it, and process it securely. Django’s forms.py can create forms from models or fields that aren’t in models.

#### Writing `forms.py`:

- You define a `Form` class for each form you want to create. For example, `UserRegistrationForm` allows users to enter and validate their registration data.

#### Example Structure:

```python
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']
```

#### Explanation of Key Parts:

- **`Meta` Class**: Sets form details, such as the model (e.g., `User`) and the fields to include (e.g., '`username`', '`first_name`', '`email`').

- **Field Definitions**: Define fields manually if they need special behavior, like hiding password characters using `PasswordInput`.

- **Validation (e.g., `clean_password2`)**: Custom methods to validate specific fields.

#### How Forms are Used:

1. In views, forms are created and filled with data from the user’s input.

2. Forms validate data automatically, checking types, required fields, and constraints.

### 3. `views.py` and View Functions

**Purpose of `views.py`**: In Django, `views.py` contains the view functions or classes that define the logic for handling requests and generating responses. Each view function takes a user request, processes it (e.g., retrieving or saving data), and then returns an HTML response.

#### Writing `views.py`:

- Each view function represents an endpoint that can serve dynamic content based on user interactions.

#### Example Structure:

```python
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm, UserEditForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_management/register.html', {'form': form})
```

#### Explanation of Key Parts:

- **Function Definition**: `def register(request):` defines the `register` view. It receives the `request` object, which contains data about the HTTP request.

- Conditionals for Request Methods:
    
    - `POST` method: Processes form data submitted by the user. The form is validated and saved if the data is valid.
    
    - `GET` method: Displays an empty form for the user to fill out.

- **Form Usage**:
    - The form is instantiated with `UserRegistrationForm()`.
    
    - `is_valid()` checks if the form data meets all criteria.
    
    - `save()` saves the form data as a new user in the database.

- Rendering Templates:
    
    - The view returns the template (e.g., `register.html`) with context data (e.g., `{'form': form}`).

#### How Views are Used:

    - Views process user requests, handle logic, and pass data to templates, where it’s displayed as a response.

### 4. Template Folder Structure

#### Should the Template Folder Exist as a Subfolder of the App?

- **Yes**: Django’s best practice is to create a `templates` folder inside each app to store templates related to that specific app.

- **Why**: Organizing templates within the app allows easy management and separation of app-specific templates from others.

#### Example Directory Structure:

```text
my_project/
├── user_management/
│   ├── templates/
│   │   └── user_management/
│   │       ├── register.html
│   │       └── profile.html
│   ├── __init__.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
```

- **Naming Convention**: Inside `templates`, the subfolder `user_management` matches the app’s name, which helps Django find templates correctly if multiple apps have templates with the same name.

---

## 6. Common Questions about This Project

**Q: Are registered users stored in the linked database?**

Yes, users are saved in the `auth_user` table in PostgreSQL. You can query this table directly to view user information.

**Q: Why are templates needed for user management?**

Templates like `register.html` and `profile.html` provide HTML forms that enable users to enter data and interact with the backend.

**Q: Can I add custom fields to the user model?**

You can create a custom user model if additional fields are needed, but this should be done at the project’s start to avoid migration issues.

---

## 7. Main Reference Links

- [Django User Authentication Documentation](https://docs.djangoproject.com/en/5.1/topics/auth/)

- [Django Forms Documentation](https://docs.djangoproject.com/en/5.1/topics/forms/)

- [Django Model and Form Validation](https://docs.djangoproject.com/en/5.1/ref/forms/validation/)