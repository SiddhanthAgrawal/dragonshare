import mongoengine as mg

mg.connect(host="mongodb+srv://admin:@sitedata.fe9yi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

class User(mg.Document):
    email = mg.StringField()
    password = mg.StringField()
