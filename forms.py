from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField(
        "Usuario",
        validators=[
            DataRequired(message="El usuario es obligatorio."),
            Length(min=3, max=50, message="El usuario debe tener entre 3 y 50 caracteres.")
        ]
    )

    password = PasswordField(
        "Contraseña",
        validators=[
            DataRequired(message="La contraseña es obligatoria.")
        ]
    )

    submit = SubmitField("Ingresar")


class RegisterForm(FlaskForm):
    username = StringField(
        "Usuario",
        validators=[
            DataRequired(message="El usuario es obligatorio."),
            Length(min=3, max=50, message="El usuario debe tener entre 3 y 50 caracteres.")
        ]
    )

    password = PasswordField(
        "Contraseña",
        validators=[
            DataRequired(message="La contraseña es obligatoria."),
            Length(min=6, max=100, message="La contraseña debe tener mínimo 6 caracteres.")
        ]
    )

    confirm_password = PasswordField(
        "Confirmar contraseña",
        validators=[
            DataRequired(message="Debe confirmar la contraseña."),
            EqualTo("password", message="Las contraseñas no coinciden.")
        ]
    )

    submit = SubmitField("Registrar")