from flask import Flask, redirect, render_template, request, url_for
from flask.helpers import flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms.fields.core import SelectField, StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import InputRequired


class BookForm(FlaskForm):
    b_name = StringField("Book Name", validators=[InputRequired()])
    b_author = StringField("Book Author", validators=[InputRequired()])
    b_rating = SelectField("Ratings",validators=[InputRequired()],choices=['⭐','⭐⭐','⭐⭐⭐','⭐⭐⭐⭐','⭐⭐⭐⭐⭐'])
    submit = SubmitField('Add')
   

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=True, nullable=False)
    rating = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


    
db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html',book_data = all_books)


@app.route("/add",methods=["GET","POST"])
def add():
    my_form = BookForm()
    if  request.method == "POST" and my_form.validate_on_submit():
        new_book = Book(title=f"{my_form.b_name.data}", author=f"{my_form.b_author.data}", rating=f"{my_form.b_rating.data}")
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html',b_form = my_form)    


@app.route("/edit",methods=["POST","GET"])
def edit():
    book_id = request.args.get('id')
    desired_book = Book.query.get(book_id)
    if request.method == "POST":
        book_id = request.form["b_id"]
        update_book = Book.query.get(book_id)
        update_book.rating=request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',book= desired_book)

@app.route('/delete/<int:id>')
def delete(id):
    book_id = id
    delete_book = Book.query.get(book_id)
    db.session.delete(delete_book)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

