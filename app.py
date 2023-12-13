1   from flask import Flask
  4 
  5 app = Flask(__name__)
 11 
 12 @app.route('/', methods=['GET'])
 13 def one():
 16     return "<h1>flask_app</h1>"
 17 
 18 if __name__  == '__main__':
 19     app.run(host="0.0.0.0", debug=True)

