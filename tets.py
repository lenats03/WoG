import requests
name='Lena'
score=5
import requests
import json


#r = requests.delete("http://localhost:5001/scores" ,data={})
#print (r,r.text)
r = requests.post("http://localhost:5001/scores",
    data={ "acct": name,
    "score": score},
)
print (r,r.text)



