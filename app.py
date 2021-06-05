import os
from flask import Flask 
if os.path.exists("env.py"):
    import env 


app = Flask(_name_)

@app.route("/") 
def hello():
    return "Hello World... again!"


    if _name_=="_main_":
        app.run(host=os.environ.get("IP"),
         port=int(os.environ.get("PORT")),
         debug=True)
         