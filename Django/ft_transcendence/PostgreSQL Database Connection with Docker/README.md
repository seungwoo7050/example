# PostgreSQL Connection Setup in Django with Docker

In this project, we will set up a PostgreSQL database for a Django project using Docker to create isolated, reproducible environments. The guide will cover dependency verification and installation, environment setup, database configuration, and instructions for starting and stopping the application.

---

## Table of Contents

1. **Project Purpose**

2. **Requirements and Planning**

3. **Step-by-Step Code Walkthrough**

4. **Concepts**

5. **My Questions**

6. **Common Questions about This Project**

7. **Main Reference Links**

---

## 1. Project Purpose

In this project, you’ll learn:

- How to set up and verify environment dependencies.

- How to configure Django to connect to a PostgreSQL database.

- Manage dependencies using Docker and a requirements.txt file.

- Manage and securely store environment variables.

--

## 2. Requirements and Planning

### Software Requirements

- **macOS** (using Terminal)

- **Homebrew** (for dependency management)

- **Python 3.x**

- **Docker** and **Docker Compose**

### Key Setup Steps

1. Verify and install dependencies.

2. Create a virtual environment and install Django.

3. Set up a `requirements.txt` file.

4. Set up Docker and Docker Compose to run Django and PostgreSQL.

5. Test, start, and stop the application properly.

---

## 3. Step-by-Step Code Walkthrough

### Step 1: Verify and Install Dependencies on macOS

1. **Install Homebrew (if not already installed)**: Check if Homebrew is installed by running:

	```bash
	brew --version

	# If not installed:
	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
	```

2. **Verify and Install Python 3.x**: Check if Python 3.x is installed:

	```bash
	python3 --version

	# If Python is not installed:
	brew install python3
	```

3. **Verify and Install Docker**: Check if Docker is installed and accessible by running:

	```bash
	docker --version

	# If Docker isn’t installed:
	brew install --cask docker
	```

	Note: Docker Desktop may need to be launched from your Applications folder.

### Step 2: Set Up a Virtual Environment

1. **Create a project directory and initialize a virtual environment**:

	```bash
	mkdir ft_transcendence_project && cd ft_transcendence_project
	python3 -m venv venv
	```

2. **Activate the virtual environment**:

	```bash
	source venv/bin/activate

	# To deactivate the virtual environment, run:
	deactivate
	```

3. **Install Django and Add Dependencies to `requirements.txt`**:

	1. **Install Django in your virtual environment**:

		```bash
		pip install django
		```

	2. **Generate a `requirements.txt` file**:

		```bash
		pip freeze > requirements.txt
		```

		This file will capture Django and other installed packages, ensuring consistent installation across environments.

	3. **Contents of `requirements.txt`**: Make sure your `requirements.txt` includes at least:

		```text
		django==<your installed version>
		psycopg2-binary
		```

4. **Install dependencies from `requirements.txt`**:

	Once your `requirements.txt` file is set up, you can install all listed dependencies with the following command. This step ensures that all required packages are installed consistently across different setups.

	```bash
	pip install -r requirements.txt
	```

### Step 3: Create and Verify a New Django Project

1. **Start a Django project**:

	```bash
	django-admin startproject myproject .
	```

2. **Verify the setup by running Django’s development server**:

	```bash
	python manage.py runserver
	```

	Check `http://127.0.0.1:8000` in your browser to ensure Django is running correctly.

	**To stop the server**: Press `Ctrl + C` in the Terminal.

### Step 4: Configure Docker and Docker Compose

1. **Create a `Dockerfile`**: In your project directory, create a Dockerfile to define the Docker image for your Django app.

	```Dockerfile
	# Dockerfile
	FROM python:3.9-slim
	ENV PYTHONUNBUFFERED=1
	WORKDIR /code
	COPY requirements.txt /code/
	RUN pip install -r requirements.txt
	COPY . /code/
	```

2. **Create a `docker-compose.yml` file**: This file defines services for Django and PostgreSQL.

	```yaml
	version: '3.9'

	services:
		db:
			image: postgres
			environment:
				POSTGRES_DB: mydatabase
				POSTGRES_USER: myuser
				POSTGRES_PASSWORD: mypassword
			volumes:
			- postgres_data:/var/lib/postgresql/data

		web:
			build: .
			command: python manage.py runserver 0.0.0.0:8000
			volumes:
				- .:/code
			ports:
				- "8000:8000"
			environment:
				- DJANGO_SETTINGS_MODULE=myproject.settings
			depends_on:
				- db

	volumes:
		postgres_data:
	```

### Step 5: Configure Django for PostgreSQL

1. **Add PostgreSQL connection information in Django settings**: In `myproject/settings.py`, update the `DATABASES` setting:

	```python
	DATABASES = {
		'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'mydatabase',
		'USER': 'myuser',
		'PASSWORD': 'mypassword',
		'HOST': 'db',
		'PORT': '5432',
		}
	}

### Step 6: Running Docker Compose

1. **Start the Docker containers**:

	```bash
	docker-compose up --build
	```
	- This command will build the images and start the containers. Access the application at `http://localhost:8000` to verify that it’s running.

	**To stop the Docker containers**: Press `Ctrl + C` in the terminal where Docker Compose is running, or run:

	```bash
	docker-compose down
	```

2. **Common Docker Commands**:

	- **Rebuild without cache**: If you need to rebuild the Docker containers (e.g., after changes in `Dockerfile`):
		```bash
		docker-compose up --build --no-cache
		```

	- **View logs**: To check logs for troubleshooting:
		```bash
		docker-compose logs
		```

	- **Stop all containers**: Clean up containers and remove networks:
		```bash
		docker-compose down
		```

---

## 4. Concepts

### Key Concepts Covered

- **Containerization (Docker)**: Docker helps maintain consistency in deployment across different environments.

- **PostgreSQL in Docker**: Running PostgreSQL in Docker allows you to keep database configurations isolated and easily portable.

- **Requirements Management**: The `requirements.txt` file lists dependencies, ensuring consistent installations across environments.

- **Environment Variables**: Environment variables store sensitive data securely, allowing configurations to change between development, testing, and production.

---

## 5. My Questions

### 1. Dockerfile Configuration Details

#### 1-1. PYTHONUNBUFFERED=1 in ENV

- **Purpose**: Setting `PYTHONUNBUFFERED=1` in the environment ensures that Python outputs (such as print statements) are sent directly to the terminal without being buffered.

- **Why it’s Useful**: Without buffering, you can see the logs in real time, which is essential for debugging within a Docker container.

#### 1-2. `/code/` Directory as the Working Directory

- **Purpose of `/code/`**: This directory is where we define our project’s working directory. It can be any directory name, but it's a good practice to use a standard directory like `/code/` or `/app/`.

- **Automatic Creation**: If `/code/` doesn't exist, Docker will create it automatically when it is set as the `WORKDIR` using `WORKDIR /code`.

- **Feature of COPY Command**: The `COPY . /code/` command copies all files from the current directory on the host machine into the `/code/` directory in the container. The `COPY` command doesn’t create directories; instead, the `WORKDIR` does.

### 2. Docker Components and Settings

#### 2-1. Differences Between build and image in Docker Compose

- **`build` Directive**:

	- When using `build`, Docker Compose will build the image based on the instructions in the Dockerfile within the project directory. This approach is useful for custom-built applications where you want to control the dependencies and configurations explicitly.

	- Example:
		```yaml
		web:
		build: .
		ports:
			- "8000:8000"
		```
- **`image` Directive**:
	- With `image`, you specify a pre-built Docker image that can be pulled from Docker Hub or another Docker registry. This method is ideal for standardized applications or services, like `postgres`, `redis`, or `nginx`, where you do not need to customize the image.

	- Example:
		```yaml
		db:
		image: postgres
		environment:
			POSTGRES_DB: mydatabase
		```

#### 2-2. `127.0.0.1` vs `0.0.0.0` in Docker Environments

- **`127.0.0.1` (Localhost)**: This IP restricts access to the application to the local machine only. It is useful in development or testing environments where you don’t want external access.

- `0.0.0.0`: This IP binds the application to all available network interfaces, making it accessible from outside the Docker container (e.g., from your local machine's browser). This is particularly important in Docker because the application is in a container isolated from the host system.

#### 2-3. Purpose of `POSTGRES_DB`, `POSTGRES_USER`, and `POSTGRES_PASSWORD`

- **Usage**: These environment variables are used by the PostgreSQL Docker image to create and initialize the database on first launch.

	- `POSTGRES_DB`: Sets the name of the initial database created in PostgreSQL.

	- `POSTGRES_USER`: Sets the username for accessing the database.

	- `POSTGRES_PASSWORD`: Sets the password for the specified user.

- **Customizable**: You can set these values to anything, but they must match the credentials in Django’s `DATABASES` configuration (in `settings.py`).

- **Where to Set Them**: In Docker Compose, these are set under `environment` for the `db` service, and the corresponding values should be reflected in Django’s `DATABASES` setting.

#### 2-4. Difference Between Dockerfile EXPOSE and Docker Compose Ports

- **Dockerfile `EXPOSE`**: The `EXPOSE` command in the Dockerfile indicates which port the application listens on inside the container. However, it doesn’t actually map this port to the host machine.

- **Docker Compose Ports**:
	- The `ports` setting in `docker-compose.yml` maps the container’s port to a port on the host machine, allowing external access.

	- For instance, `8000:8000` maps the container’s port `8000` to port `8000` on the host, making the app accessible from `localhost:8000`.

### 3. Setting Up DATABASES in settings.py

- **Purpose**: In `settings.py`, you define your database settings to tell Django which database to connect to.
- **Replacing Existing Settings**: Yes, you typically replace the default `sqlite3` configuration in `DATABASES` with your PostgreSQL configuration as follows:
	```python
	DATABASES = {
    	'default': {
        	'ENGINE': 'django.db.backends.postgresql',
        	'NAME': 'mydatabase',
			'USER': 'myuser',
			'PASSWORD': 'mypassword',
			'HOST': 'db',  # Refers to the service name in docker-compose.yml
			'PORT': '5432',
		}
	}
	```

### 4. Managing and Verifying Databases in Django and PostgreSQL

#### 4-1. Checking Existing Database Connections and Adding Additional Databases

1. **Checking Database Connections**:

	- **Directly in Django**: Run `python manage.py dbshell` to check if you can connect to the database. Alternatively, you can use Django ORM commands, like querying a model, to see if the connection is active.

	- **Directly in PostgreSQL**: Run `docker-compose exec db psql -U myuser -d mydatabase` to connect to PostgreSQL via the terminal.

2. **Connecting to Multiple Databases**:

- Django supports multiple databases. In `settings.py`, you can add additional entries in the `DATABASES` setting.

	```python
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql',
			'NAME': 'mydatabase',
			'USER': 'myuser',
			'PASSWORD': 'mypassword',
			'HOST': 'db',
			'PORT': '5432',
		},
		'second_db': {
			'ENGINE': 'django.db.backends.postgresql',
			'NAME': 'another_db',
			'USER': 'myuser2',
			'PASSWORD': 'mypassword2',
			'HOST': 'db',
			'PORT': '5432',
		}
	}
	```

- With multiple databases, specify which one to use when querying:
	```python
	from myapp.models import MyModel
	data = MyModel.objects.using('second_db').all()
	```

#### 4-2. General Database Management in Django and PostgreSQL

1. **Creating and Managing Databases**:

	- **In PostgreSQL**: Use `docker-compose exec db psql -U myuser` to access PostgreSQL. Commands like `CREATE DATABASE` and `DROP DATABASE` manage databases directly.

	- **In Django**: Django ORM provides tools to manage tables, relationships, and migrations rather than entire databases. Use `python manage.py migrate` to apply migrations and create tables within the database specified in `DATABASES`.

2. **General Database Control in Django**:

	- Django offers the `makemigrations` and `migrate` commands to control tables (models) within the specified database.

	- For example:
		```bash
		python manage.py makemigrations
		python manage.py migrate
		```

3. **When to Use Django vs PostgreSQL Directly**:

- **Use Django**: For managing models and migrations (e.g., creating/updating tables).

- **Use PostgreSQL**: For managing entire databases (e.g., creating/deleting databases, managing users).

**Example Scenario**
If you want to set up a new database for testing, you would:

1. **Create the database** in PostgreSQL manually via psql or Docker Compose environment variables.

2. **Add the database configuration** in Django’s DATABASES setting.

3. **Use Django ORM** to define and manage tables within that database.

---

## 6. Common Questions about This Project

**Q: What is the purpose of `requirements.txt`?**

- The `requirements.txt` file lists all Python packages required by your Django project, making it easy to reinstall the same versions of dependencies on a different machine or environment.

**Q: How can I ensure that Docker and Django servers stop running properly?**

- For Docker, you can stop containers using `docker-compose down`. For Django’s development server, `Ctrl + C` in the terminal stops it.

**Q: How do I restart Docker containers if I need to apply changes?**

- Use `docker-compose up --build` to restart and apply any changes in the Docker environment.

---

## 7. Main Reference Links

- [Django Documentation](https://docs.djangoproject.com/en/stable/)

- [Docker Documentation](https://docs.docker.com/)

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)