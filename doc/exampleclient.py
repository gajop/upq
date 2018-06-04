#!/usr/bin/env python

import requests

searchparams = {
	"category" : "engine_linux64",
	"limit": 1
}

r = requests.get('https://api.springfiles.com/json.php', params=searchparams)

print(r.json())
