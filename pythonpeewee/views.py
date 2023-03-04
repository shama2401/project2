from models import *
from flask import *

app = Flask(__name__)
app.config['SECRET KEY'] = '123740981237401732904'

@app.route('/insert-data/', methods=['POST', 'GET'])
def insert_data():
    if request.method == 'POST':
        word = request.form['word']
        translate = request.form['translate']
        if not English.select().where(English.word == word):
            English.create(word=word, translate=translate)
        else:
            return flash(f'Слово {word} уже существует', 'Warning')
    return render_template('insert.html')

@app.route('/')
def show_data():
    words = English.select()
    # for i in English.select():
    #     print(i.id, i.word, i.translate)
    return render_template('index.html', words=words)


@app.route('/update/<int:id>', methods=['POST','GET'])
def update_data(id):
    datas = English.get_by_id(id)
    if request.method == 'POST':
        word = request.form['word']
        word_upd = request.form['word_upd']
        query = English.update(word=word, translate=word_upd).where(English.word==word)
        query.execute()
        return redirect('/')
    return render_template('update.html', datas=datas)


@app.route('/delete/<int:id>')
def delete_data(id):
    English.delete_by_id(id)
    return redirect('/')

def main(query='None'):
    app.run(debug=True)
    # while True:
    #     if query != '':
    #         query = input('''
    #         Введите:
    #         0 - для выхода
    #         1 - для вставки слова
    #         2 - для просмотра слов
    #         3 - для обновления слова
    #         4 - для удаления слова
    #         ''')
    #
    #         if query == '0':
    #             print('Программа остановлена')
    #             break
    #         if query == '1':
    #             insert_data()
    #         if query == '2':
    #             show_data()
    #         if query == '3':
    #             update_data()
    #         if query == '4':
    #             delete_data()
    #     else:
    #         print('Неизвестный запрос')

if __name__ == '__main__':
    main()