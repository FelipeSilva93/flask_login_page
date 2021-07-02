from flask import Blueprint, render_template, request, flash
from app.ext.auth.controller import create_user, check_user_existance


bp = Blueprint("site", __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/register', methods=["GET", "POST"])
def register():
    msg = None
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        check_user = check_user_existance(email)
       
        if check_user:
            msg = "Email já cadastrado"
        else:
            create_user(email, password)
            msg = 'Usuário cadastrado com sucesso'

            
    return render_template('register.html', msg=msg)
