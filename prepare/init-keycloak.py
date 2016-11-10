import requests
import json

serverUrl = 'http://localhost:8181/auth'
realm = 'master'
username = 'admin'
password = 'H16obbit'
clientId = 'test'
clientSecret = 'dbcf14d3-a161-4954-b2e3-d3295de63959'

def authenticate():
  # Fetch access token
  payload = {'client_id': [clientId], 'client_secret': [clientSecret], 'grant_type': ['password'], 'username': [username], 'password': [password]}
  response = requests.post('%s/realms/%s/protocol/openid-connect/token' % (serverUrl, realm), data=payload)
  if response.status_code != 200:
    raise Exception("%d %s" % (response.status_code, response.text))
  access_token = response.json()['access_token']
  return access_token

def loadJsonFile(jsonFile):
  with open(jsonFile, 'r') as myfile:
    data = myfile.read()
  return data

def post(uri, jsonFile, access_token, isArray=False):
  content = loadJsonFile(jsonFile)
  headers = {'Authorization': 'Bearer %s' % (access_token), 'Content-Type': 'application/json'}
  url = '%s/%s' % (serverUrl, uri)
  if not isArray:
    response = requests.post(url, headers=headers, data=content)
    print("%d %s" % (response.status_code, response.text))
  else:
    array = json.loads(content)
    for item in array:
      txt = json.dumps(item)    
      response = requests.post(url, headers=headers, data=txt)
      print("%d %s" % (response.status_code, response.text))

def put(uri, access_token, data=''):
  headers = {'Authorization': 'Bearer %s' % (access_token), 'Content-Type': 'application/json'}
  url = '%s/%s' % (serverUrl, uri)
  response = requests.put(url, headers=headers, data=data)
  print("%d %s" % (response.status_code, response.text))

def get(uri, access_token):
  headers = {'Authorization': 'Bearer %s' % (access_token), 'Content-Type': 'application/json'}
  url = '%s/%s' % (serverUrl, uri)
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    return response.json()
  else:
    print("%d %s" % (response.status_code, response.text))
    return []

def setUserPassword(jsonFile, access_token):
  print("set passwords...")
  data = '{"type": "password", "value": "hobbit", "temporary": false}'
  content = loadJsonFile(jsonFile)
  array = json.loads(content)
  users = get('admin/realms/Hobbit/users', access_token)
  for item in array:
    for user in users:
      if user['username'] == item['username']:
        id = user['id']
        print('set password for %s ...' % (item['username'])) 
        put('admin/realms/Hobbit/users/%s/reset-password' % (id), access_token, data)

def addDefaultGroup(groups, access_token):
  for g in groups:
    if g['name'] == 'Hobbit-user':
      id = g['id']
      print("set default group...")
      put('admin/realms/Hobbit/default-groups/%s' % id, access_token)

access_token = authenticate()
post('admin/realms', 'hobbit-realm.json', access_token)
post('admin/realms/Hobbit/clients', 'hobbit-client-gui.json', access_token)
post('admin/realms/Hobbit/clients', 'hobbit-client-rest.json', access_token)
post('admin/realms/Hobbit/roles', 'hobbit-roles.json', access_token, isArray=True)
groups = get('admin/realms/Hobbit/groups', access_token)
if len(groups) == 0:
  post('admin/realms/Hobbit/groups', 'hobbit-groups.json', access_token, isArray=True)
groups = get('admin/realms/Hobbit/groups', access_token)
addDefaultGroup(groups, access_token)
post('admin/realms/Hobbit/users', 'hobbit-users.json', access_token, isArray=True)
setUserPassword('hobbit-users.json', access_token)

