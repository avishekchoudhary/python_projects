from enum import unique
from inspect import Parameter
from operator import index
from typing import ValuesView

from flask import Flask, render_template, redirect, url_for, request
from flask.wrappers import Response
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from requests.api import head
from wtforms import StringField, SubmitField
from wtforms.fields.core import DecimalField
from wtforms.validators import DataRequired, InputRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title  = db.Column(db.String(60),unique=True,nullable=False)
    year  = db.Column(db.Integer,nullable=False)
    description  = db.Column(db.String(120),unique=True,nullable=False)
    rating  = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(300),nullable=False)
    img_url = db.Column(db.String(300),unique=True,nullable=False)

    def __repr__(self):
        return f'<Movies {self.title}>'

db.create_all()
    

class UpdateForm(FlaskForm):
    change_1 = DecimalField('Your ratings out of 10',validators=[InputRequired()])
    change_2 = StringField("Your Review",validators=[InputRequired()])
    submit = SubmitField('Done')


class AddForm(FlaskForm):
    movie_name = StringField("Movie Title",validators=[InputRequired()])
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i    
    db.session.commit()
    return render_template("index.html",movies_data = all_movies)

@app.route("/edit/<int:id>",methods = ["POST","GET"])
def update(id):
    update_form = UpdateForm()
    movie_id = id
    if request.method == "POST" and update_form.validate_on_submit():
        u_movie = Movie.query.get(movie_id)
        u_movie.rating = update_form.change_1.data
        u_movie.review = update_form.change_2.data
        db.session.commit()
        return redirect(url_for('home'))
    desired_movie = Movie.query.get(movie_id)
    return render_template("edit.html",movie = desired_movie,U_form = update_form)
@app.route("/delete/<int:id>")
def delete(id):
    movie_id = id
    d_movie = Movie.query.get(movie_id)
    db.session.delete(d_movie)
    db.session.commit()
    return redirect(url_for('home')) 


@app.route("/add",methods=["POST","GET"])
def add():
    add_form = AddForm()
    if request.method == "POST" and add_form.validate_on_submit():
        movie = add_form.movie_name.data
        parameter={
            "api_key":'9ce920a9268394c054a98cad0b70abb6',
            "query":movie
        }
        response = requests.get(url="https://api.themoviedb.org/3/search/movie",params=parameter)
        response.raise_for_status()
        data = response.json()['results']
        return render_template('select.html',movies=data)
    return render_template('add.html',a_form = add_form)

@app.route("/select")
def select():
    movie_id = request.args.get("id")
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}",params={"api_key":'9ce920a9268394c054a98cad0b70abb6'})
    response.raise_for_status()
    data = response.json()
    new_movie = Movie(
    title=data["original_title"],
    year=data[ "release_date"].split("-")[0],
    description=data[ "overview"],
    rating=data["vote_average"],
    ranking=None,
    review="Not revieved yet",
    img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('home'))
  

if __name__ == '__main__':
    app.run(debug=True)
