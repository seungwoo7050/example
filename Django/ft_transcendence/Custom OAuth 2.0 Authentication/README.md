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

Access Control: OAuth tokens replace sensitive user data, providing controlled access.
Flexible User Data: Custom OAuth lets you specify data (like user profile info) for retrieval, making it highly adaptable.
Redis Integration for Security: Redis stores tokens securely, with automatic expiration to improve security and simplify token management.
This project builds on standard OAuth by customizing the process for 42 API and integrating Redis for secure storage.

2. Requirements and Planning
Software Requirements
macOS (using Terminal)
Django (from the virtual environment set up previously)
Redis for token storage
redis-py for Python Redis integration
requests for making HTTP requests to the 42 API
Key Setup Steps
Set up and configure Redis for secure token storage.
Register your application with the 42 API to retrieve client credentials.
Define the custom OAuth authorization and token exchange flow with Django views.
Customize user data retrieval and handling to fit your app’s requirements.
3. Step-by-Step Code Walkthrough
Step 1: Install Required Packages
Activate your virtual environment:

bash
코드 복사
source venv/bin/activate
Install Redis and Requests Libraries: Install redis-py and requests for Redis integration and HTTP requests:

bash
코드 복사
pip install redis requests
Update requirements.txt:

bash
코드 복사
pip freeze > requirements.txt
Step 2: Configure Redis in Django Settings
Redis will be used for secure token storage, and Django will connect to it as a token cache.

Add Redis Configuration to settings.py:
python
코드 복사
# settings.py
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
Step 3: Set Up OAuth Credentials
You need a CLIENT_ID and CLIENT_SECRET from the 42 API to authorize users.

Register Application with 42 API:

Go to the 42 API portal and register a new application.
Set the callback URI to match the following:
text
코드 복사
http://127.0.0.1:8000/oauth/callback/
Retrieve your CLIENT_ID and CLIENT_SECRET.
Store Credentials in Environment Variables or Settings:

python
코드 복사
CLIENT_ID = os.getenv('FT_CLIENT_ID')
CLIENT_SECRET = os.getenv('FT_CLIENT_SECRET')
REDIRECT_URI = 'http://127.0.0.1:8000/oauth/callback/'
Step 4: Define OAuth URLs in Django
Add URL patterns to handle the custom OAuth login and callback routes.

Define OAuth URLs in urls.py:
python
코드 복사
# project/urls.py
from django.urls import path
from user_management import views

urlpatterns = [
    path('oauth/login/', views.oauth_login, name='oauth_login'),
    path('oauth/callback/', views.oauth_callback, name='oauth_callback'),
]
Step 5: Implement OAuth Login View
This view redirects the user to the 42 API authorization page, requesting access with specific scopes.

Create oauth_login View in views.py:

python
코드 복사
# user_management/views.py
from django.shortcuts import redirect
from django.conf import settings

def oauth_login(request):
    authorization_url = (
        f"https://api.intra.42.fr/oauth/authorize"
        f"?client_id={settings.CLIENT_ID}&redirect_uri={settings.REDIRECT_URI}&response_type=code"
    )
    return redirect(authorization_url)
Explanation:

OAuth Scopes: You can specify additional scopes here to request specific data.
Redirect Flow: Users are redirected to the 42 authorization URL where they can approve access.
Step 6: Implement OAuth Callback View
The callback view handles the response from 42, exchanges the code for tokens, retrieves user data, and saves tokens to Redis.

Define oauth_callback in views.py:

python
코드 복사
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
    login(request, user)
    
    return redirect('profile')
Explanation:

Code Exchange: Exchanges the authorization code for access and refresh tokens.
Token Storage in Redis: The access token is stored in Redis with expiration for security.
User Data Handling: Custom user data (username and email) is saved in Django’s User model.
Step 7: Verify OAuth Integration
Start Django Server:

bash
코드 복사
python manage.py runserver
Testing OAuth Flow:

Visit http://127.0.0.1:8000/oauth/login/ to initiate the login.
After authentication on the 42 API page, the callback view should log in the user.
Verify Redis Storage:

Open Redis CLI and check token storage:
bash
코드 복사
redis-cli
KEYS *  # Lists all stored keys
GET 42_token:<access_token>  # Replace <access_token> to retrieve the stored token
4. Concepts
Key Concepts Covered
OAuth 2.0 Flow: Redirects user to provider’s login page, exchanges code for tokens, retrieves user data, and stores tokens.
Token Storage in Redis: Redis stores tokens with expiration, providing secure and efficient token handling.
Customized Data Handling: The 42 API provides custom user data (e.g., campus info, profile image) retrieved through scopes.
5. My Questions (placeholder)
How can I add more customization in Redis storage (e.g., expiration handling, namespaces)?
Is it possible to refresh the access token automatically when it expires?
6. Common Questions about This Project
Q: Why store tokens in Redis instead of Django’s database?

Redis is ideal for temporary, fast-access storage, making it a secure option for tokens that expire frequently.
Q: Can I customize the OAuth scopes to retrieve more data?

Yes, you can add scopes to the authorization URL to request specific data from the 42 API.
Q: What happens if a token expires?

Redis will automatically discard expired tokens. If the provider supports refresh tokens, the system can request a new access token using the refresh token.
7. Main Reference Links
OAuth 2.0 Specification
Django Redis Integration Documentation
42 API Documentation