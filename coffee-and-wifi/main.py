from flask import Flask, render_template
from flask.globals import request
from flask.helpers import url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField,SelectField
from wtforms.fields.html5 import URLField,TimeField
from wtforms.validators import InputRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '#'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name',validators=[InputRequired()])
    location = URLField('Cafe Location og Google Maps(URL)',validators=[InputRequired()])
    opening = TimeField('Opening Time(HH:MM)',validators=[InputRequired()])
    closing = TimeField('Closing Time(HH:MM)',validators=[InputRequired()])
    coffee_rating = SelectField('Coffee Rating',validators=[InputRequired()],choices=['☕','☕☕','☕☕☕','☕☕☕☕','☕☕☕☕☕'])
    wifi_rating  = SelectField("Wi-Fi Ratings",validators=[InputRequired()],choices=['❌','📶','📶📶','📶📶📶','📶📶📶📶','📶📶📶📶📶'])
    power_rating = SelectField('Power Ratings',validators=[InputRequired()],choices=['❌','🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["POST","GET"])
def add_cafe():
    my_form = CafeForm()
    if request.method == "POST" and my_form.validate_on_submit() :
        print("True")
        cafeName = my_form.cafe.data
        cafeUrl = my_form.location.data
        openTime = my_form.opening.data
        closeTime = my_form.closing.data
        cofRating = my_form.coffee_rating.data
        wifRating = my_form.wifi_rating.data
        powRating = my_form.power_rating.data  
        with open('cafe-data.csv','a',encoding='utf8') as csv_file:
            csv_file.write(f"\n{cafeName},"
                           f"{cafeUrl},"
                           f"{openTime},"
                           f"{closeTime},"
                           f"{cofRating},"
                           f"{wifRating},"
                           f"{powRating},")
        return redirect(url_for('cafes'))     
    return render_template('add.html', form=my_form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='',encoding='utf8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
