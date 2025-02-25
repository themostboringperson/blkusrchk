import requests
import json



def getinfo(username):
    ROBLOX_API_LINK = 'https://users.roblox.com/v1/usernames/users'
    ROBLOX_USERNAME = {"usernames":[f"{username}"]}
    HEADERS = {'Content-Type':'application/json'}

    roblox_response = requests.post(ROBLOX_API_LINK,json.dumps(ROBLOX_USERNAME),headers=HEADERS)
    print(roblox_response.json())
    return roblox_response.json()

def getotherinfo(userid):
    ROBLOX_API_LINK2 = f'https://friends.roblox.com/v1/users/{userid}/friends'
    HEADERS2 = {'Content-Type':'application/json'}

    roblox2_response = requests.get(ROBLOX_API_LINK2,headers=HEADERS2)
    print(roblox2_response.json())
    return roblox2_response.json()

if __name__ == '__main__':
    getotherinfo(userid=2042035259)