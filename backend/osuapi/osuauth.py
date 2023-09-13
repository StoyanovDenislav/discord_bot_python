import os
import requests
from flask import Blueprint, request, redirect
from dotenv import load_dotenv
from .temp_get_token import getToken, getRefreshToken
from .users import getUser
from flask_cors import CORS
from flask.json import jsonify




load_dotenv()

auth = Blueprint('authapi', __name__)


# Your application's client ID and client secret
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# OAuth endpoints
AUTHORIZATION_URL = 'https://osu.ppy.sh/oauth/authorize'
TOKEN_URL = 'https://osu.ppy.sh/oauth/token'


# Redirect URI that you've registered in your Osu! application settings
REDIRECT_URI = os.getenv("REDIRECT_URI")



@auth.route('/authapi')
def InitialCheck():
    
    token = getToken()
    
    if token is None:
        return redirect('/authapi/promptauth')
    
    if token and len(token) > 0:
        
        data = getUser(token, 2)
        
        if len(data) < 1:
            
            return redirect('/authapi/reauthorize')
  
    return redirect('/authapi/promptauth')
        
@auth.route('/authapi/promptauth')
def promptauth():
    
    
    
    auth_params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'scope': 'public',
    }
    auth_url = f'{AUTHORIZATION_URL}?{"&".join([f"{k}={v}" for k, v in auth_params.items()])}'

    return redirect(auth_url)

   

@auth.route('/authapi/callback') 
def callback():
    authorization_code = request.args.get('code')
    token_params = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': authorization_code,
        'grant_type': 'authorization_code',
        'redirect_uri': REDIRECT_URI,
    }
    token_response = requests.post(TOKEN_URL, data=token_params)
    token_data = token_response.json()
    ACCESS_TOKEN = token_data['access_token']
    REFRESH_TOKEN = token_data['refresh_token']
    
    with open('token.txt', 'w') as f:
        f.write(ACCESS_TOKEN)
    with open('refresh_token.txt', 'w') as f:
        f.write(REFRESH_TOKEN)
        
    print(token_data)
    # Now you have the access token to make authorized API requests
    # You can store the access token for future use or retrieve user data

    return redirect('')





    
    
@auth.route('/authapi/reauthorize')
def reauthorize():
    
    refresh_token = getRefreshToken()
    
    
    auth_params = {
        
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'scope': 'public',
    }
    
    token_response = requests.post(TOKEN_URL, data=auth_params)
    token_data = token_response.json()
    ACCESS_TOKEN = token_data['access_token']
    
    
    with open('token.txt', 'w') as f:
        f.write(ACCESS_TOKEN)
        
    print(token_data['expires_in'])
 
        
   
    # Now you have the access token to make authorized API requests
    # You can store the access token for future use or retrieve user data

    return "Reauthorization successful"




