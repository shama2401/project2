from flask import Flask, render_template, url_for, request, flash
from models import *

app = Flask(__name__)

menu = [
    {'name': 'Home', 'url': '/'},
    {'name': 'About', 'url': '/about'},
    {'name': 'blog', 'url': '/blog'},
    {'name': 'doctor', 'url': '/doctor'},
    {'name': 'contact', 'url': '/contact'},
    {'name': 'depatments', 'url': '/depatments'},
]

@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu,)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html')


@app.route('/blog')
def blog():
    print(url_for('blog'))
    return render_template('blog.html', menu=menu, blog_link='blog')


@app.route('/doctor')
def doctor():
    print(url_for('doctor'))
    return render_template('doctor.html', menu=menu, doctor_link='doctor')


@app.route('/contact', methods=['GET', 'POST'])
def Contact():
    if request.method == 'POST':
        datas = dict(request.form)
        print(datas['email'].split('@')[1])
        email_list = ['gmail.com', 'mail.ru', 'yandex.ru']
        if len(datas['username']) < 2:
            # len(datas['phone_number']) <= 10 and \
            # datas['phone_number'].isdigit()\
            flash('Validate error', category='error')
        if datas['email'].split('@')[1] not in email_list:
            flash('Validate error', category='error')
        else:
            flash('Welcome', category='success')
    return render_template('contact.html', menu=menu)



@app.route('/depatments')
def depatments():
    print(url_for('depatments'))
    return render_template('depatments.html', menu=menu ,depatments_link='/depatments')






if __name__ == '__main__':
    app.run(debug=True)



