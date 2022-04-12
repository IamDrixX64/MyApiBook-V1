import yaml
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()

database = 'library'
passw = os.getenv('db_pass')

db_path = "mysql+pymysql://drixx:IamDrixX64@localhost:5000/mydblivres"

db = SQLAlchemy()


def setup_db(app, path=db_path):

    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)
    db.create_all()


class Category(db.Model):

    __tablename__ = 'categories'

    id_cat = db.Column(db.Integer, primary_key=True)
    libelle_categorie = db.Column(db.String(50))
    books = db.relationship('Book', backref='categories', lazy=True)

    def __init__(self, libelle_categorie):
        self.libelle_categorie = libelle_categorie

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id_cat,
            'categorie': self.libelle_categorie
        }


class Book(db.Model):

    __tablename__ = 'books'

    id_book = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(12), nullable=False)
    titre = db.Column(db.String(200), nullable=False)
    date_publication = db.Column(db.String(10), nullable=False)
    auteur = db.Column(db.String(200), nullable=False)
    editeur = db.Column(db.String(150), nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id_cat'), nullable=False)

    def __init__(self, isbn, titre, date_publication, auteur, editeur, categorie_id):
        self.isbn = isbn
        self.titre = titre
        self.date_publication = date_publication
        self.auteur = auteur
        self.editeur = editeur
        self.categorie_id = categorie_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id_book,
            'code_ISBN': self.isbn,
            'titre': self.titre,
            'auteur': self.auteur,
            'editeur': self.editeur,
            'date_publication': self.date_publication
        }

    

    
class User(db.Model):

    __tablename__ = 'users'
    
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

    def __repr__(self):
        return '<User %r>' % self.username
    
    def create(self, data):
        username=data['username'],
        password=data['password'],
        email=data['email']
        
        db.session.add(user)
        db.session.commit()
        return user

    def update(self, data):
        user.username = data['username']
        user.email = data['email']

        db.session.add(user)
        db.session.commit()
        return user

    def delete(self):
        db.session.delete(user)
        db.session.commit()
        return True

    def get_all(self):
        return users


class SiteModel(db.Model):
    __tablename__="sites"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ville = db.Column(db.String(255), nullable=False)
    pays = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    url_photo = db.Column(db.String(255))
    note = db.Column(db.Integer)

    def __repr__(self):
        return '<Site %r>' % self.name
        
    def jsonify(self, site):
        return {
            "name" : site.name,
            "ville" : site.ville,
            "pays" : site.pays,
            "description" : site.description,
            "url_photo" : site.url_photo,
            "note" : site.note
        }

    def create(self, data):
        name=data['name'],
        ville=data['ville'],
        pays=data['pays'],
        description=data['description'],
        url_photo=data['url_photo'],
        note=data['note'],
        
        db.session.add(site)
        db.session.commit()
        return self.jsonify(site)

    def update(self, data):
        site.name = data['name']
        site.ville = data['ville']
        site.pays = data['pays']
        site.description = data['description']
        site.url_photo = data['url_photo']
        site.note = data['note']

        db.session.add(site)
        db.session.commit()
        return self.jsonify(site)

    def delete(self):
        db.session.delete(site)
        db.session.commit()
        return True

    def get_all(self):
        return [self.jsonify(site) for site in sites]

    def get(self):
        return self.jsonify(site)
