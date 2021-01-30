from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == '__main__':
	app.run()