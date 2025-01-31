from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField
from wtforms.validators import DataRequired, Length, Regexp

class FormularioCadastro(FlaskForm):
    nome = StringField(
        'Nome',
        validators = [DataRequired(), Length(min=3, max=100)],
        render_kw = {
            "class": "form-control"
        }
    )

    sobrenome = StringField(
        'Sobrenome',
        validators = [DataRequired(), Length(min=3, max=100)],
        render_kw = {
            "class": "form-control"
        }
    )

    idade = IntegerField(
        'Idade',
        validators = [DataRequired()],
        render_kw = {
            "class": "form-control"
        }
    )

    curso = RadioField(
        'Curso',
        choices = [
            (1, 'Análise e Desenvolvimento de Sistemas (MANHÃ)'),
            (2, 'Análise e Desenvolvimento de Sistemas (TARDE)'),
            (3, 'Gestão da Tecnologia da Informação (NOITE)'),
            (4, 'Gestão de Energia e Eficiência Energética (NOITE)'),
            (5, 'Gestão Empresarial (MANHÃ)'),
            (6, 'Logística (NOITE)'),
            (7, 'Processos Químicos (MANHÃ)'),
            (8, 'Processos Químicos (NOITE)')
        ],
        validators = [DataRequired(), Length(min=3, max=100)],
        render_kw = {
            "class": "form-check"
        }
    )

    whatsapp = StringField(
        'WhatsApp',
        validators = [DataRequired()],
        render_kw = {
            "class": "form-control telefone-input",
            "placeholder": "(xx) x xxxx-xxxx"
        }
    )

    semestre_atual = IntegerField(
        'Semestre Atual',
        validators = [DataRequired()],
        render_kw = {
            "class": "form-control"
        }
    )
