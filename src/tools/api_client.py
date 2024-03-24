from urllib import request
import json

def getFromApi(url, auth_token):
  req = request.Request(url)
  req.add_header("Authorization", auth_token)

  response = request.urlopen(req)
  text = response.read()

  return json.loads(text.decode('utf-8'))

def getFromUrl(url, auth_token):
  req = request.Request(url)
  req.add_header("Authorization", auth_token)

  response = request.urlopen(req)
  text = response.read()

  return json.loads(text.decode('utf-8'))