from app.ext.admin import admin as main_admin
from app.ext.auth.admin import UserAdmin
from app.ext.db import db
from app.ext.db.models import User


def init_app(app):
    """TODO: inicializar o flask simple login + JWT"""

    main_admin.add_view(UserAdmin(User, db.session))
