import click
from app.ext.db import db
from app.ext.db import models


def init_app(app):

    @app.cli.command()
    def create_db():
        """Este comando inicializa o db"""
        db.create_all()

    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--password", "-p")
    def add_user(email, password):
        """Este comando adiciona novos usuarios através do shell"""
        user = models.User(
            email=email,
            password=password
        )

        db.session.add(user)
        db.session.commit()
