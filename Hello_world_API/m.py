from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route('/hello', methods=['GET'])
def hello_world():
     username = request.args.get('language')
     if(username=='French' or username=='french'):
      return 'Bonjour le monde'
     elif(username=='English' or username=='english'):
      return 'Hello world'
     elif(username=='Hindi' or username=='hindi'):
      return 'Namastey sansar'
     else:
      return 'The requested language is not supported'
     
     

if __name__ == '__main__':
    app.run()
