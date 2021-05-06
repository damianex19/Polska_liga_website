from flask import Flask,render_template,url_for
app = Flask(__name__)

clubs = [
	{  
		'club': 'Ruch Chorzów',
		'voivedship': "Silesian",
		'level': '4',
		'updatedata': '07.05.2021'
	},
	{
		'club': 'RKS Radomsko',
		'voivedship': "Łódź",
		'level': '4',
		'updatedata': '07.05.2021'
	}
]

@app.route('/')
def home():
   return render_template('home.html',clubs=clubs)
@app.route('/about')
def about():
   return render_template('about.html',title='About')
if __name__ == '__main__':
      app.run(debug=True)
      
      
