from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
   return 'Witamy na stronie polskich lig krajowych utworzonej z uzyciem microframeworka Flask'
if __name__ == '__main__':
      app.run(debug=True)
