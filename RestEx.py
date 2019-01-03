from flask import Flask, render_template, jsonify, request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    return "HELLO WORLD"

if __name__=='__main__':
    app.run(debug=True)


## REST API

