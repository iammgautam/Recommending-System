from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm, contentQueryForm, collaborativeQueryForm
from popularityModel import popularMovies
from contentModel import get_recommendations
from collaborativeModel import recommender

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'



@app.route("/home")
def home():
    return render_template('home.html', popularMovies=popularMovies)


@app.route("/contentSearch",methods=['GET','POST'])
def contentSearch():
    form = contentQueryForm()
    if form.validate_on_submit():

        query = form.conQuery.data


        rec = get_recommendations(query)


        # query = form.conQuery
        # rec = get_recommendations(title=query)
        return render_template('contentSearch.html', title='Recommendations of your choice', form = form, rec = rec, header_rec = "Top 10 Recommendations for you")
    return render_template('contentSearch.html', title='Recommendations of your choice', form = form)

@app.route("/collaborativeSearch",methods=['GET','POST'])
def collaborativeSearch():
    form = collaborativeQueryForm()
    if form.validate_on_submit():

        query = form.collQuery.data


        rec = recommender(query)


        return render_template('collaborativeSearch.html', title='Recommendations of your choice', form = form, rec = rec, header_rec = "Top 10 Recommendations for you")
    return render_template('collaborativeSearch.html', title='Recommendations of your choice', form = form)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/", methods=['GET','POST'])
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
        if form.email.data == 'admin@admin.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)