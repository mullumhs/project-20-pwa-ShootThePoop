from flask import render_template, request, redirect, url_for, flash
from models import db, Countries # Also import your database model here

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

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
            return redirect(url_for('index'))
        # This route should handle adding a new item to the database.
        return render_template('index.html', message='Country added successfully')



    @app.route('/update', methods=['POST'])
    def update_item():
        # This route should handle updating an existing item identified by the given ID.
        return render_template('index.html', message=f'Item updated successfully')



    @app.route('/delete', methods=['POST'])
    def delete_item():
        # This route should handle deleting an existing item identified by the given ID.
        return render_template('index.html', message=f'Item deleted successfully')