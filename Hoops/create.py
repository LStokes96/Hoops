from application import db
from application.models import Comments, Users, Players

db.drop_all()
db.create_all()


