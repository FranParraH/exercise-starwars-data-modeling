import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, func, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    
class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

class Entry(Base):
    __tablename__ = 'entry'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    
class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    url = Column(String(500))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    entry_id = Column(Integer, ForeignKey('entry.id'), nullable=False)
    entry = relationship(Entry)

class Comment(Base):
    __tablename__ = 'coment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    entry_id = Column(Integer, ForeignKey('entry.id'), nullable=False)
    entry = relationship(Entry)

class Films(Base):
    __tablename__ = 'films'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(500))
    time_created = Column(DateTime(timezone=True), server_default=func.now())

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(500))
    diameter = Column(Integer)
    terrain = Column(String(500))
    population = Column(Integer)
    
class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    url = Column(String(500))
   
class Follow_planet(Base):
    __tablename__ = 'follow_planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    url = Column(String(500))
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    planet = relationship(Character)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

class Follow_character(Base):
    __tablename__ = 'follow_character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    url = Column(String(500))
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    character = relationship(Character)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

class Film_planet(Base):
    __tablename__ = 'film_planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    planet = relationship(Character)
    films_id = Column(Integer, ForeignKey('films.id'), nullable=False)
    films = relationship(Films)

class Film_character(Base):
    __tablename__ = 'film_character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    character = relationship(Character)
    films_id = Column(Integer, ForeignKey('films.id'), nullable=False)
    films = relationship(Films)   


# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     user = relationship(User)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
