from peewee import *

class BaseModel(Model):
    class Meta:
        database=SqliteDatabase('demo_OD.db')


class Contact(BaseModel):
    id=PrimaryKeyField(null=True)
    word=CharField(max_length=100)
    translate=CharField(max_length=100)



    class Meta:
        db_table='contact'


if __name__ == '__main__':
    Contact.create_table()
