# src/chapter20.py

"""
Chapter 20 – Database Access & ORMs
Author: Luca Bocaletto
Description:
    Demonstrate raw sqlite3 usage, SQLAlchemy Core, and SQLAlchemy ORM.
"""

import os
import sqlite3

from sqlalchemy import (
    create_engine, MetaData, Table, Column, Integer, String, select
)
from sqlalchemy.orm import declarative_base, sessionmaker

DB_FILE = "app.db"


def demo_sqlite3():
    print("== sqlite3 Demo ==")
    # remove existing database for a clean start
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE users (
            id    INTEGER PRIMARY KEY,
            name  TEXT NOT NULL,
            email TEXT UNIQUE
        )
    ''')
    conn.commit()

    # insert rows
    cur.execute("INSERT INTO users (name, email) VALUES (?, ?)",
                ("Alice", "alice@example.com"))
    cur.execute("INSERT INTO users (name, email) VALUES (?, ?)",
                ("Bob",   "bob@example.com"))
    conn.commit()

    # query and print
    cur.execute("SELECT id, name, email FROM users")
    for row in cur.fetchall():
        print("  ", row)

    cur.close()
    conn.close()
    print()


def demo_sqlalchemy_core():
    print("== SQLAlchemy Core Demo ==")
    engine = create_engine(f"sqlite:///{DB_FILE}", echo=False)
    metadata = MetaData()

    users = Table(
        "users", metadata,
        Column("id",    Integer, primary_key=True),
        Column("name",  String, nullable=False),
        Column("email", String, unique=True),
    )
    metadata.create_all(engine)

    # insert a new record
    with engine.connect() as conn:
        conn.execute(
            users.insert(),
            [{"name": "Carol", "email": "carol@example.com"}]
        )
        conn.commit()

        # select and display
        rows = conn.execute(select(users)).fetchall()
        for r in rows:
            print("  ", dict(r))
    print()


def demo_sqlalchemy_orm():
    print("== SQLAlchemy ORM Demo ==")
    Base = declarative_base()
    engine = create_engine(f"sqlite:///{DB_FILE}", echo=False)
    Session = sessionmaker(bind=engine)

    class User(Base):
        __tablename__ = "users"
        id    = Column(Integer, primary_key=True)
        name  = Column(String, nullable=False)
        email = Column(String, unique=True)

        def __repr__(self):
            return f"<User(id={self.id}, name={self.name!r}, email={self.email!r})>"

    Base.metadata.create_all(engine)

    session = Session()
    # add another user
    session.add(User(name="Dave", email="dave@example.com"))
    session.commit()

    # query by filter
    q = session.query(User).filter(User.name.in_(["Alice", "Dave"]))
    for user in q:
        print("  ", user)
    session.close()
    print()


def main():
    print("\n=== Chapter 20: Database Access & ORMs Demo ===\n")
    demo_sqlite3()
    demo_sqlalchemy_core()
    demo_sqlalchemy_orm()
    print("=== End of Chapter 20 ===\n")


if __name__ == "__main__":
    main()
