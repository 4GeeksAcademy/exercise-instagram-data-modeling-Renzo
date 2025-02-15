import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, ForeignKey
from eralchemy2 import render_er
from typing import List

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    firstname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable = False, unique = True)

    followers: Mapped[List["Follower"]] = relationship(foreign_keys = ["Follower.user_from_id"])
    following: Mapped[List["Follower"]] = relationship(foreign_keys = ["Follower.user_to_id"])

class Follower(Base):
    __tablename__ = 'follower'
    id: Mapped[int] = mapped_column(primary_key = True)

    user_from_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_to_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

class Post(Base):
    __tablename__ = 'post'

    id: Mapped[int] = mapped_column(primary_key = True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship()

class Media(Base):
    __tablename__ = 'media'
    id: Mapped[int] = mapped_column(primary_key = True)
    type: Mapped[str] = mapped_column(nullable = False)
    url: Mapped[str] = mapped_column(nullable = False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post: Mapped["Post"] = relationship()

class Comment(Base):
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(primary_key = True)
    comment_text: Mapped[str] = mapped_column(nullable = False)

    autor_id: Mapped[str] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship()

    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post: Mapped["Post"] = relationship()



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
