from flask import Flask,render_template,url_for, flash,redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'PUT YOUR KEY HERE'

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

@app.route('/register',methods =["GET","POST"])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template('register.html', title = 'Register', form = form)	
@app.route('/login', methods =["GET","POST"])
def login():
	form = LoginForm()
	return render_template('login.html', title = 'Login', form = form)
	

if __name__ == '__main__':
      app.run(debug=True)
      
      
