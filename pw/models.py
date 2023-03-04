from peewee import *


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase('anime.db')

class Anime(BaseModel):
    id = PrimaryKeyField(null=True, unique=True)
    title = CharField()
    poster = CharField()
    seasons = IntegerField()
    serias = IntegerField()
    janre = CharField()
    description = TextField()
    date = DateField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'anime'

class Episod(BaseModel):
    id = PrimaryKeyField(null=True)
    anime = ForeignKeyField(Anime)
    video_url = CharField()

    class Meta:
        db_table = 'episode'

if __name__ == '__main__':
    Episod.create_table()
    Anime.create_table()
