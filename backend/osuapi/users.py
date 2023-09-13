import requests
from .temp_get_token import getToken

API_URL = 'https://osu.ppy.sh/api/v2'

def getOwnData(access_token, mode=None):
    
    
    if mode is None:
        mode = "osu"
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
         
        
    }
    body = {
        
         "mode": f"{mode}",
        
    }
    
    url = API_URL + f'/me/{mode}'
    
    request = requests.get(url=url, headers=headers, params=body)
    
    data = request.json()
    
    return data

def getUserKudosu(access_token, user):
    
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
         
        
    }
    body = {
        
         "id": f"{user}",
        
    }
    
    url = API_URL + f'/users/{user}/kudosu'
    
    request = requests.get(url=url, headers=headers, params=body)
    
    data = request.json()
    
    return data

def getUserScores(access_token, user, type, include_fails=None, mode=None, limit=None, offset=None):
    
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
         
        
    }
    body = {
        
        # "include_fails": f"{include_fails}",
        # "mode": f"{mode}",
        # "limit": f"{limit}",
        # "offset": f"{offset}",
         
        # TODO cuz fucking hell
        
    }
    
    url = API_URL + f'/users/{user}/scores/{type}'
    
    request = requests.get(url=url, headers=headers, params=body)
    
    data = request.json()
    
    return data

def getUserBeatmaps(access_token, user, type, limit=None, offset=None):
    
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
         
        
    }
    body = {
        
        
         "limit": f"{limit}",
         "offset": f"{offset}",
         
        
        
    }
    
    url = API_URL + f'/users/{user}/beatmapsets/{type}'
    
    request = requests.get(url=url, headers=headers, params=body)
    
    data = request.json()
    
    return data

def getUserRecentActivity(access_token, user, limit=None, offset=None):
    
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
         
        
    }
    body = {
        
        
         "limit": f"{limit}",
         "offset": f"{offset}",
         
        
        
    }
    
    url = API_URL + f'/users/{user}/recent_activity'
    
    request = requests.get(url=url, headers=headers, params=body)
    
    data = request.json()
    
    return data

def getUser(access_token, user, mode=None, key=None):
    
    if mode is None:
        mode = "osu"
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
         
        
    }
    body = {
        
        
         "mode": f"{mode}",
         "key": f"{key}",
         
        
        
    }
    
    url = API_URL + f'/users/{user}/{mode}'
    
    request = requests.get(url=url, headers=headers, params=body)
    
    data = request.json()
    
    return data




#Not implemented getUsers()