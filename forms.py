from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange

class FormularioCadastro(FlaskForm):
    nome = StringField(
        'Nome',
        validators = [DataRequired(), Length(min=3, max=100)],
        render_kw = {
            "class": "btn btn-dark form-control"
        }
    )

    sobrenome = StringField(
        'Sobrenome',
        validators = [DataRequired(), Length(min=3, max=100)],
        render_kw = {
            "class": "btn btn-dark form-control"
        }
    )

    idade = IntegerField(
        'Idade',
        validators = [DataRequired()],
        render_kw = {
            "class": "btn btn-dark form-control text-center",
            "inputmode": "numeric"
        }
    )
    
    whatsapp = StringField(
        'WhatsApp',
        validators = [DataRequired()],
        render_kw = {
            "class": "btn btn-dark form-control text-center telefone-input",
            "inputmode": "numeric",
            "placeholder": "(xx) x xxxx-xxxx"
        }
    )

    semestre_atual = IntegerField(
        'Semestre Atual',
        validators = [DataRequired(), NumberRange(min=1, max=10)],
        render_kw = {
            "class": "btn btn-dark form-control text-center",
            "inputmode": "numeric"
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
            "class": "form-check d-none"
        }
    )

    sobre = TextAreaField(
        'Nos conte um pouco sobre você!',
        validators = [DataRequired(), Length(min=50)],
        render_kw = {
            "class": "btn btn-dark form-control",
            "placeholder": "Esta informação é para ajudar o seu calouro/veterano a te conhecer um pouco melhor. Conte um pouco sobre suas experiências pessoais e acadêmicas, hobbies e interessees.",
            "rows": 8
        }
    )