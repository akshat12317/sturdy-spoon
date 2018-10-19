from flask import Flask
from flask import render_template
from flask import request
import contactus as ct
ct.create_table()
app=Flask(__name__)


def counting(text):
    counter = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for v in counter:
        vowel_count = text.count(v)
        counter[v] = vowel_count
    return counter


@app.route('/', methods=['GET', 'POST'])
def index():
    counter=None
    if request.method=='POST':
        print('form submitted')
        Input1 = request.form.get('Input1')
        counter = counting(Input1)
        print(counter)
    return render_template('index.html', data=counter)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method=='POST':
        print('form submitted')
        name = request.form.get('name')
        mobile_no = request.form.get('Mobile')
        email = request.form.get('Email-id')
        ct.insert_data(name, mobile_no, email)
    return render_template('contact.html')


@app.route('/info')
def info():
    contact=ct.Show()
    return render_template('info.html', contact=contact)


if __name__ == "__main__":
    app.run(debug=True)
