from flask import Flask, request , render_template 
app=Flask(__name__)

@app.route1('/')

def loadpage():
    return ("i am Samannita")


@app.route('/admin')

def helloadmin():
    return ("i am Loria")
app.run()
