import requests




    
API_URL = 'https://osu.ppy.sh/api/v2'




def getUserBeatmapScore(access_token, beatmap, user, mode=None, mods=None):
    
    
    if mode is None:
        mode = "osu"
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
         
        
    }
    body = {
        
         "mode": f"{mode}",
         "mods": f"{mods}"
    }
    
    url = API_URL + f'/beatmaps/{beatmap}/scores/users/{user}'
    
    request = requests.get(url=url, headers=headers, params=body)
    
    data = request.json()
    
    return data

def getUserBeatmapScoreAll(access_token, beatmap, user, mode=None):
    
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
    
    url = API_URL + f'/beatmaps/{beatmap}/scores/users/{user}/all'
    
    request = requests.get(url=url, headers=headers, params=body)
    
    data = request.json()
    
    return data

def getBeatmapScores(access_token, beatmap, mode=None, mods=None, type=None):
    
    if mode is None:
        mode = "osu"
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
         
        
    }
    body = {
        
         "mode": f"{mode}",
         "mods": f"{mods}",
         "type": f"{type}",
         
    }
    
    url = API_URL + f'/beatmaps/{beatmap}/scores'
    
    request = requests.get(url=url, headers=headers, params=body)
    
    data = request.json()
    
    return data

def getBeatmap(access_token, beatmap):

    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
         
        
    }

    url = API_URL + f'/beatmaps/{beatmap}'
    
    request = requests.get(url=url, headers=headers)
    
    data = request.json()
    
    return data

def lookupBeatmap(access_token, id=None, filename=None, checksum=None):

    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
         
        
    }
    body = {
        
         "id":f'{id}',
         "filename":f'{filename}',
         "checksum":f'{checksum}',
         
    }
    
    url = API_URL + f'/beatmaps/lookup'
    
    request = requests.get(url=url, headers=headers, params=body)
    
    data = request.json()
    
    return data
    
    #Not implemented getBeatmaps()

   
  