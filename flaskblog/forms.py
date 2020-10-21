from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('İstifadəçi Adı',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Şifrə', validators=[DataRequired()])
    confirm_password = PasswordField('Təsdiq Şifrəsi',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Qeydiyyatdan Keç')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('Daxil etdiyiniz istifadəçi adı artıq istifadə olunub. Zəhmət olmasa, fərqli ad daxil edin. ')

    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Daxil etdiyiniz Email artıq istifadə olunub. Zəhmət olmasa, fərqli Email daxil edin.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Şifrə', validators=[DataRequired()])
    remember = BooleanField('Hesabımı Yadda Saxla')
    submit = SubmitField('Daxil Ol')


class UpdateAccountForm(FlaskForm):
    username = StringField('İstifadəçi Adı',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Profil şəklini yenilə', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Yenilə')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()

            if user:
                raise ValidationError('Daxil etdiyiniz istifadəçi adı artıq istifadə olunub. Zəhmət olmasa, fərqli ad daxil edin.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()

            if user:
                raise ValidationError('Daxil etdiyiniz Email artıq istifadə olunub. Zəhmət olmasa, fərqli Email daxil edin.')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
