# Custom OAuth 2.0 Authentication

In this module, we’ll implement a custom OAuth 2.0 authentication flow with Django, enabling users to log in via the 42 API. We’ll build the OAuth logic from scratch for flexibility, configure Redis to store tokens securely, and ensure custom data retrieval. This guide covers OAuth basics, Redis integration, and the end-to-end process for a comprehensive learning experience.

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

- How to build a custom OAuth 2.0 authentication flow for a specific provider.

- How to integrate the 42 API with Django to provide single sign-on (SSO) functionality.

- Storing and managing OAuth tokens securely using Redis.

- Customizing user data retrieval to match your application’s needs.

### What is OAuth 2.0 Authentication?

OAuth 2.0 is an authorization protocol that allows applications to access user data from a third-party provider without storing user credentials. In this setup:

- **Access Control**: OAuth tokens replace sensitive user data, providing controlled access.

- **Flexible User Data**: Custom OAuth lets you specify data (like user profile info) for retrieval, making it highly adaptable.
- **Redis Integration for Security**: Redis stores tokens securely, with automatic expiration to improve security and simplify token management.

This project builds on standard OAuth by customizing the process for 42 API and integrating Redis for secure storage.

---

## 2. Requirements and Planning

### Software Requirements

- **macOS** (using Terminal)

- **Django** (from the virtual environment set up previously)

- **Redis** for token storage

- **redis-py** for Python Redis integration

- **requests** for making HTTP requests to the 42 API

### Key Setup Steps

1. **Redis Configuration**:

	- Set up Redis for secure, fast token storage with built-in expiration handling.

	- Confirm Redis connectivity with Django to enable seamless integration for token caching.

2. **OAuth 2.0 Credentials and Flow**:

	- Register your application with the 42 API and obtain `CLIENT_ID` and `CLIENT_SECRET`.

	- Define the custom OAuth authorization and token exchange flow in Django views.

3. **Secure Token Storage**:

	- Use Redis to securely store tokens, with automatic expiration and retrieval mechanisms.

	- Implement optional token refresh logic to handle access token expiration and maintain session continuity.

4. **Customized Data Retrieval**:

	- Configure user data retrieval to match application requirements, such as fetching profile info, email, or campus details from the 42 API.

5. **Debugging and Validation**:

	- Integrate logging to capture OAuth flow events, errors, and user data retrieval.
	
	- Test OAuth login, token storage, and Redis expiration to confirm end-to-end functionality.

---

## 3. Step-by-Step Code Walkthrough

### Step 1: Install Required Packages

1. **Activate your virtual environment**:

	```bash
	source venv/bin/activate
	```

2. **Install Redis and Requests Libraries**: Install `redis-py` and `requests` for Redis integration and HTTP requests:

	```bash
	pip3 install redis requests
	```
	
3. **Update `requirements.txt`**:
	
	```bash
	pip3 freeze > requirements.txt
	```

### Step 2: Configure Redis in Django Settings

Redis will be used for secure token storage, and Django will connect to it as a token cache.

1. **Add Redis Configuration to `settings.py`**:
	
	```python
	# settings.py
	REDIS_HOST = 'localhost'
	REDIS_PORT = 6379
	REDIS_DB = 0
	```

2. **Installing and Starting Redis**:

	```bash
	# Install
	brew install redis

	# Start the Redis server
	redis-server

	# Verify Redis is running by entering
	# You should see PONG, confirming that Redis is ready to use.
	redis-cli ping
	```

3. **Testing Django’s Connection to Redis**:

	After setting up Redis, run your Django project to confirm Redis is accessible and connected without errors.

### Step 3: Set Up OAuth Credentials

You need a `CLIENT_ID` and `CLIENT_SECRET` from the 42 API to authorize users.

1. **Register Application with 42 API**:

	- Go to the 42 API portal and register a new application.

	- Set the callback URI to match the following:

		```text
		http://127.0.0.1:8000/oauth/callback/
		```

	- Retrieve your `CLIENT_ID` and `CLIENT_SECRET`.

2. **Store Credentials Securely in Environment Variables**:

	Add the following to your environment variables (e.g., in `.env`):

	```text
	FT_CLIENT_ID=<your_client_id>
	FT_CLIENT_SECRET=<your_client_secret>
	```


3. **Access Environment Variables in `settings.py`**:

	```python
	CLIENT_ID = os.getenv('FT_CLIENT_ID')
	CLIENT_SECRET = os.getenv('FT_CLIENT_SECRET')
	REDIRECT_URI = 'http://127.0.0.1:8000/oauth/callback/'
	```

### Step 4: Define OAuth URLs in Django

Add URL patterns to handle the custom OAuth login and callback routes.

1. **Define OAuth URLs in `urls.py`**:
	
	```python
	# project/urls.py
	from django.urls import path
	from user_management import views

	urlpatterns = [
		path('oauth/login/', views.oauth_login, name='oauth_login'),
		path('oauth/callback/', views.oauth_callback, name='oauth_callback'),
	]
	```

### Step 5: Implement OAuth Login View

This view redirects the user to the 42 API authorization page, requesting access with specific scopes.

1. **Create `oauth_login` View in `views.py`**:

	```python
	# user_management/views.py
	from django.shortcuts import redirect
	from django.conf import settings

	def oauth_login(request):
		authorization_url = (
			f"https://api.intra.42.fr/oauth/authorize"
			f"?client_id={settings.CLIENT_ID}&redirect_uri={settings.REDIRECT_URI}"
			f"&response_type=code&scope=public"
		)
		return redirect(authorization_url)
	```

2. **Explanation**:

	- **OAuth Scopes**: Scopes determine the data your application can access. For example, `public profile email campus` scopes allow you to access basic profile information, email, and campus details from the user. Adjusting scopes can help retrieve specific data needed by your application.

	- **Redirect Flow**: Users are redirected to the 42 authorization URL where they can approve access.

### Step 6: Implement OAuth Callback View

The callback view handles the response from 42, exchanges the code for tokens, retrieves user data, and saves tokens to Redis.

1. **Define `oauth_callback` in `views.py`**:

	```python
	import requests
	import redis
	from django.shortcuts import redirect
	from django.conf import settings
	from django.contrib.auth import login
	from django.contrib.auth.models import User

	# Connect to Redis
	redis_instance = redis.StrictRedis(
		host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB
	)

	def oauth_callback(request):
		# Retrieve authorization code
		code = request.GET.get('code')
		token_url = "https://api.intra.42.fr/oauth/token"
		
		# Token request data
		token_data = {
			'grant_type': 'authorization_code',
			'client_id': settings.CLIENT_ID,
			'client_secret': settings.CLIENT_SECRET,
			'code': code,
			'redirect_uri': settings.REDIRECT_URI,
		}
		response = requests.post(token_url, data=token_data)
		tokens = response.json()
		
		# Extract tokens
		access_token = tokens.get('access_token')
		refresh_token = tokens.get('refresh_token')
		expires_in = tokens.get('expires_in')

		# Store tokens in Redis with expiration
		redis_instance.set(f'42_token:{access_token}', refresh_token, ex=expires_in)

		# Retrieve user info
		headers = {'Authorization': f'Bearer {access_token}'}
		user_info = requests.get("https://api.intra.42.fr/v2/me", headers=headers).json()
		
		# Create or update user in Django
		username = user_info['login']
		email = user_info.get('email', f'{username}@42.fr')
		user, created = User.objects.get_or_create(username=username, defaults={'email': email})
		
		# Update or add additional profile fields (optional)
		if created:
			# Example of adding profile data from 42 API
			user.profile.image_url = user_info.get('image_url')
			user.profile.campus_info = user_info.get('campus')
			user.profile.save()
		
		# Log in the user
		login(request, user)
		
		return redirect('profile')
	```

2. **Explanation**:

	- **Code Exchange**: Exchanges the authorization code for access and refresh tokens.
	
	- **Token Storage in Redis**: The access token is stored in Redis with an expiration time to automatically handle token lifecycles.
	
	- **Custom User Data**: Additional profile fields can be saved if your application requires more user information.
	
	- **Session Management**: After retrieving the user data, the view logs in the user and redirects them to their profile page.

#### Token Expiration Handling

When storing tokens in Redis, we can rely on Redis's built-in expiration mechanism to automatically discard expired access tokens. However, for a more seamless user experience, we can use the `refresh_token` to get a new access token without requiring the user to log in again. Here’s an example of how to handle token expiration and refreshing:

```python
# Check token expiration and refresh if needed
if 'refresh_token' in tokens:
    refresh_token = tokens['refresh_token']
    # Use refresh token to get a new access token when the current one expires
    refresh_data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET,
    }
    refreshed_response = requests.post(token_url, data=refresh_data)
    new_tokens = refreshed_response.json()
    access_token = new_tokens.get('access_token')
    expires_in = new_tokens.get('expires_in')
    redis_instance.set(f'42_token:{access_token}', access_token, ex=expires_in)
else:
    # Handle case where refresh token is missing or expired
    # Prompt user to log in again, or take other action
    return redirect('oauth_login')
```

### Step 7: Verify OAuth Integration

1. **Start Django Server**:

	```bash
	python manage.py runserver
	```

2. **Testing OAuth Flow**:

	- Visit `http://127.0.0.1:8000/oauth/login/` to initiate the login.

	- Complete authentication on the 42 API page. You should be redirected to your callback view, where the user is logged in.

3. **Verify Redis Storage**:
	
	After authenticating, use the Redis CLI to verify that the tokens were stored securely:

	```bash
	redis-cli
	KEYS *  # Lists all stored keys
	```

	To check the expiration time of a specific token, use:

	```bash
	TTL 42_token:<access_token>
	```

	This command returns the remaining time (in seconds) until expiration, confirming that Redis handles token expiration.

---

## 4. Concepts

### Key Concepts Covered

- **OAuth 2.0 Flow**: Redirects user to provider’s login page, exchanges code for tokens, retrieves user data, and stores tokens.

- **Token Storage in Redis**: Redis stores tokens with expiration, providing secure and efficient token handling.

- **Customized Data Handling**: The 42 API provides custom user data (e.g., campus info, profile image) retrieved through scopes.

---

## 5. My Questions (placeholder)

---

## 6. Common Questions about This Project

Q: How can I add more customization in Redis storage (e.g., expiration handling, namespaces)?

Q: Is it possible to refresh the access token automatically when it expires?

Q: Why store tokens in Redis instead of Django’s database?

Redis is ideal for temporary, fast-access storage, making it a secure option for tokens that expire frequently.
Q: Can I customize the OAuth scopes to retrieve more data?

Yes, you can add scopes to the authorization URL to request specific data from the 42 API.
Q: What happens if a token expires?

Redis will automatically discard expired tokens. If the provider supports refresh tokens, the system can request a new access token using the refresh token.

---

## 7. Main Reference Links

- [OAuth 2.0](https://oauth.net/2/)

- [Django Redis Integration Documentation](https://github.com/jazzband/django-redis)

- [42 API Documentation](https://api.intra.42.fr/)