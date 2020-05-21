"""
from flask import Flask
from flask import render_template,url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__) #variable setting to the instance of the class 
       #__name__ is the special variable in the python that is the name of the module

app.config['SECRET_KEY']='2a0afb16c3059b390ca2f52b12349f068527'

posts=[
       {
              'author':'Aditya Talluru',
              'title':'Blog post 1',
              'content':'First post content',
              'date_posted':'May 20, 2020'
       },
       {
              'author':'ding',
              'title':'Blog post 2',
              'content':'Second post content',
              'date_posted':'May 21, 2020'
       }
]


@app.route("/") # This is a decorator
#For additional information ::  https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
def hello():
    return "<h1>Hello World! I am Aditya</h1>"
#''' we can insert all the html code but this would make the
# code a bit confusing so we use the concept called templates
# for which we would create an external .html file in the same directory'''

#If we want to have multiple pages we just need to add another decorator
@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/register")
def register():
       form = RegistrationForm()
       return render_template('register.html',title='Register', form=form)


@app.route("/login")
def login():
       form = LoginForm()
       return render_template('login.html',title='Login', form=form)

if __name__=='__main__':
       app.run(debug=True)

"""
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)