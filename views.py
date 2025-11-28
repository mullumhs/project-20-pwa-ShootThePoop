from flask import render_template, request, redirect, url_for, flash, Flask
from models import db, Countries # Also import your database model here

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages


app = Flask(__name__)

app.secret_key = "your_secret_key_here"

def init_routes(app):

    @app.route('/', methods=['GET'])
    def index():
        # This route should retrieve all items from the database and display them on the page.
        countries = Countries.query.all()
        return render_template('index.html', message='Displaying all items', countries = countries)



    @app.route('/add', methods=['POST','GET'])
    def create_item():
        if request.method == 'POST':
            new_country = Countries(
                country = request.form['country'],
                continent = request.form['continent'],
                capital_city = request.form['capital_city'],
                population = request.form['population'],
                language = request.form['language'],
                currency = request.form['currency'],
                map = request.form['map'],
                flag = request.form['flag']
            )
            db.session.add(new_country)
            db.session.commit()
        # This route should handle adding a new item to the database.
            flash('Country added successfully!')
            return redirect(url_for('index'))
        return render_template('add.html')


    @app.route('/update', methods=['GET', 'POST'])
    def update_item():
        if request.method == 'POST':
            target_name = request.form['country'].strip().lower()
            target_continent = request.form['continent'].strip().lower()
            target_capital_city = request.form['capital_city'].strip().lower()
            country = Countries.query.filter(
                db.func.lower(Countries.country) == target_name
            ).first_or_404()

            country = Countries.query.filter(
                db.func.lower(Countries.continent) == target_continent
            ).first_or_404()

            country = Countries.query.filter(
                db.func.lower(Countries.capital_city) == target_capital_city
            ).first_or_404()



            for field in ['continent', 'capital_city', 'population', 'language', 'currency', 'map', 'flag']:
                val = request.form.get(field)
                if val:
                    setattr(country, field, val)

            db.session.commit()
            flash('Country updated successfully!')
            return redirect(url_for('index'))
        return render_template('update.html')



    @app.route('/delete', methods=['GET', 'POST'])
    def delete_item():
        if request.method == 'POST':
            target_name = request.form['country'].strip().lower()
            country = Countries.query.filter(
                db.func.lower(Countries.country) == target_name
            ).first_or_404()

            db.session.delete(country)
            db.session.commit()
            flash('Country deleted successfully!')
            return redirect(url_for('index'))
        return render_template('delete.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/register')
    def register():
        return render_template('signup.html')
    
    @app.route('/view/<id>')
    def view(id):
        country = Countries.query.filter(db.func.lower(Countries.id) == id).first_or_404()


        return render_template('view.html', id=id, country = country)
