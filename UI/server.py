from flask import Flask, render_template
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'freeCofee'
							#Some random key/something that allows us to configure
							# our Flask application
							#This is ESSENTIAL if you want form to be up and running

@app.route('/')
def home():
	return 'Hello World!'

@app.route('/about')
def about():
	return 'The about page'

@app.route('/blog')
def blog():
	posts = [{'title':'Technology in 2019', 'author': 'Steven Grady'},
			{'title': 'Expansion of oil in Russia', 'author': 'KSI'}]

	return render_template('blog.html', author= 'Steven Grady', sunny=False, posts= posts)

@app.route('/blog/<string:blog_id>') #this is a blog id variable that was passed into the URL
									 # You decide whether or not to define the <blog_id> variable with
									 # a data type i.e. i could've written <int:blog_id>
									 #or simply <blog_id>
							#what carrots <> do is specify a rule

def blogpost(blog_id):
	return 'This is blog post number ' + blog_id #printing out the blog id #

@app.route('/signup')
def signup():
	form = SignUpForm()
	return render_template('signup.html', form=form)


if __name__ == '__main__':
	app.run()