from models import *
from flask import *
app = Flask(__name__)
app.config['SECRET KEY'] = '123740981237401732904'


def add_anime():
    while True:
        id = input('Введите ID: ')
        title = input('Введите название: ')
        poster = input('Введите ссылку на постер(картинку аниме: ')
        seasons = input('Введите количество сезонов: ')
        serias = input('Введите количество серий: ')
        janre = input('Введите жанр: ')
        description = input('Введите описание: ')
        date = input('Введите дату: ')
        if not Anime.select().where(Anime.title==title):
            Anime.create(id=id, title=title, poster=poster, seasons=seasons, serias=serias, janre=janre, description=description, date=date)
            break
        else:
            print(f'{title} это аниме уже есть')

def add_episodes():
    while True:
        title = input('Введите название аниме: ')
        id = input('Введите ID: ')
        anime = int(input('Введите ID anime: '))
        video_url = input('Введите ссылку на видео: ')
        # if not Episod.select().where(Episod.anime.title==title):
        Episod.create(id=id, anime=anime, video_url=video_url)
        break
        # else:
        #     print(f'{title} такого аниме нет')


@app.route('/')
def list_anime():
    list_anime = Anime.select()
    return render_template('list.html', list_anime=list_anime)

@app.route('/list-episodes/<int:id>')
def episodes(id):
    anime = Anime.get_by_id(id)
    print(anime)
    list_episodes = Episod.select().where(Episod.anime==anime)
    # for le in list_episodes:
    #     print(le.id, le.anime, le.video_url)
    return render_template('episodes_list.html', list_episodes=list_episodes)

@app.route('/episode_view/<int:id>')
def episode_detail(id):
    video = Episod.get_by_id(id)
    return render_template('episode_detail.html', video=video.video_url)


if __name__ == '__main__':
    add_anime()
    # app.run(debug=True)
    # add_episodes()
    # app.run(debug=True)