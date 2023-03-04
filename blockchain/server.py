from flask import Flask, render_template, request, url_for, redirect
from main import write_block, check_block

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        creditor = request.form['creditor']
        amount = request.form['amount']
        borrower = request.form['borrower']
        write_block(creditor, amount, borrower)
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/checking')
def check():
    return render_template('index.html', res=check_block())


if __name__ == '__main__':
    app.run(debug=True)