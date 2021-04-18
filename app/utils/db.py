import mongoengine as mg

mg.connect(host="mongodb+srv://admin:afnan921@sitedata.fe9yi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

class User(mg.Document):
    email = mg.StringField()
    password = mg.StringField()

class Post(mg.Document):
    name = mg.StringField()
    start = mg.StringField()
    to = mg.StringField()
    contact = mg.StringField()
    gender = mg.StringField()
    no = mg.StringField()
    child = mg.StringField()