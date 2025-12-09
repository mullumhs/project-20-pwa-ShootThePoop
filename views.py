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
                country_code = request.form['country_code'],
            )
            db.session.add(new_country)
            db.session.commit()
            flash('Country added successfully!')
        # This route should handle adding a new item to the database.
            return redirect(url_for('index'))
        return render_template('add.html')


    @app.route('/update/<int:id>', methods=['GET', 'POST'])
    def update_item(id):
        # get country by ID
        country = Countries.query.get_or_404(id)

        if request.method == 'POST':
            # update fields
            country.country = request.form['country']
            country.continent = request.form['continent']
            country.capital_city = request.form['capital_city']
            country.population = request.form['population']
            country.language = request.form['language']
            country.currency = request.form['currency']
            country.country_code = request.form['country_code']
    
            db.session.commit()
            flash('Country updated successfully!')

            return redirect(url_for('view', id=country.id))

        # 5. On GET, show the edit form with the existing country data
        return render_template('update.html', country=country)





    @app.route('/delete/<int:id>', methods=['POST'])
    def delete_item(id):

        country = Countries.query.get_or_404(id)

        db.session.delete(country)
        db.session.commit()

        flash('Country deleted successfully!')
        return redirect(url_for('index'))




    
    @app.route('/search', methods=['GET', 'POST'])
    def search_query():
        if request.method == 'POST':
            target_name = request.form['country'].strip().lower()
            country = Countries.query.filter(
                db.func.lower(Countries.country) == target_name
            ).first()


            return redirect(url_for('search_query'))


        return render_template('search.html')
    
    @app.route('/view/<int:id>')
    def view(id):
        # find country by ID
        country = Countries.query.get_or_404(id)
        return render_template('view.html', country=country)
