from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class UrlYoutube(FlaskForm):
    url = StringField("URL do Video")
    botao = SubmitField("Enviar")
