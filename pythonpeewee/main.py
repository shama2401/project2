
  word = input('Введите слово:')
    if not English.select().where(English.word==word):
        translate=input('Введите перевод слова:')
        English.create(word=word,translate=translate)
        return redirect(url_for('index'))
    return render_template('index.html')

    else:
        print(f'Слово {word} уже существует')
        print(' ')

def show_data():
    for i in English.select():
        print(i.id,i.word,i.translate)

def update_data():
    word = input('Введите слово:')
    word_upd=input('На что обновить?:')
    query=English.update(translate=word_upd).where(English.word==word)
    query.execute()


def delete_data():
    delete_data_query=input('Введите слово для удаления:')
    del_word=English.select().where(English.word==delete_data_query)
    English.delete_by_id(del_word)


def main(query='None'):
    while True:
        if query != '':
            query = input('''
                    Введите:
                    0-для выхода
                    1-для вставки слова
                    2-для просмотра слов
                    3-для обновления слов
                    4-для удаления слов

                    ''')
            if query == '0':
                print('До свидания')
                break
            if query == '1':
                insert_data()
            if query == '2':
                show_data()
            if query == '3':
                update_data()
            if query == '4':
                delete_data()
        else:
            print('Неизвестная операция!')


if __name__ == '__main__':
    main()