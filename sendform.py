import requests
site = requests.get("https://lambdaschool.com/contact")
data = { "name" : "Tiago" , "lastname" : "Lucas" , "email" : "tiago.slucas@gmail.com" , "message" : "SENT WITH PYTHON!" }
r = requests.post('https://lambdaschool.com/contact-form',json=data)
print(r.text)