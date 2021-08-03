from wtforms import StringField, Form, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm


class InputForm(FlaskForm): #create form
    users = StringField('users',render_kw={"placeholder": "Utilisateur"})
    testUsers = StringField('testUsers',render_kw={"placeholder": "Utilisateur"})
    groups = SelectField('groups', choices=[])
    dateByYear = DateField('Choisir une année', format="%Y")
    dateByForkStart = DateField('Choisir la fin de la période', format="%d/%m/%Y")
    dateByForkEnd = DateField('Choisir le debut de la période', format="%d/%m/%Y")
    queue = SelectField('queue', choices=[])
    cluster = SelectField('cluster', choices=[])
    submit = SubmitField('Envoyer')
    reset = SubmitField('Réinitialiser')

class ConnexionForm(FlaskForm):
    submit = SubmitField('Connexion')