from flaskr import login_manager
from flaskr import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class Indirizzo(db.Model):
    __tablename__ = 'indirizzo'

    id_indirizzo = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('indirizzo_id_indirizzo_seq'::regclass)"))
    cap = db.Column(db.Integer, nullable=False)
    strada = db.Column(db.String(100), nullable=False)

    def __init__(self, id_indirizzo, cap, strada):
        self.id_indirizzo = id_indirizzo
        self.cap = cap
        self.strada = strada


class TipoDoc(db.Model):
    __tablename__ = 'tipo_doc'

    id_tipo = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('tipo_doc_id_tipo_seq'::regclass)"))
    tipo_documento = db.Column(db.String(50))

    def __init__(self, id_tipo, documento):
        self.id_tipo = id_tipo
        self.tipo_documento = tipo_documento

class Persona(UserMixin, db.Model):
    __tablename__ = 'persona'
    __table_args__ = (
        db.CheckConstraint("(cf)::text ~ '^[A-Z]{6}\\d{2}[A-Z]\\d{2}[A-Z]\\d{3}[A-Z]$'::text"),
    )

    id_persona = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('persona_id_persona_seq'::regclass)"))
    nome = db.Column(db.String(50), nullable=False)
    cognome = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    cf = db.Column(db.String(16), nullable=False, unique=True)
    id_indirizzo = db.Column(db.Integer, db.ForeignKey('indirizzo.id_indirizzo'), nullable=False, unique=True)
    id_email = db.Column(db.Integer, db.ForeignKey('email.id_email'), nullable=False, unique=True)
    id_documento = db.Column(db.Integer, db.ForeignKey('documento.id_documento'), nullable=False, unique=True)
    id_telefono = db.Column(db.Integer, db.ForeignKey('telefono.id_telefono'), nullable=False, unique=True)
    luogo_nascita = db.Column(db.String(50), nullable=False)
    data_nascita = db.Column(db.Date, nullable=False)

    indirizzo = db.relationship('Indirizzo', foreign_keys=[id_indirizzo], uselist=False)
    email = db.relationship('Email', foreign_keys=[id_email])
    documento = db.relationship('Documento', foreign_keys=[id_documento])
    telefono = db.relationship('Telefono', foreign_keys=[id_telefono])


    def get_id(self):
        return self.id_persona

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @login_manager.user_loader
    def load_user(id_persona):
        return Persona.query.get(int(id_persona))

class StudLeg(db.Model):
    __tablename__ = 'stud_leg'

    id_studio = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('stud_leg_id_studio_seq'::regclass)"))
    id_indirizzo = db.Column(db.Integer, db.ForeignKey('indirizzo.id_indirizzo'))
    orario_inizio = db.Column(db.Time, nullable=False)
    orario_fine = db.Column(db.Time, nullable=False)
    da_giorno = db.Column(db.String(20), nullable=False)
    a_giorno = db.Column(db.String(20), nullable=False)

    indirizzo = db.relationship('Indirizzo', foreign_keys=[id_indirizzo])

    def __init__(self, id_studio, id_indirizzo, orario_inizio, orario_fine, da_giorno, a_giorno):
        self.id_studio = id_studio;
        self.id_indirizzo = id_indirizzo
        self.orario_inizio = orario_inizio
        self.orario_fine = orario_fine
        self.da_giorno = da_giorno
        self.a_giorno = a_giorno


class Documento(db.Model):
    __tablename__ = 'documento'

    id_documento = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('documento_id_documento_seq'::regclass)"))
    codice = db.Column(db.String(50), unique=True, nullable=False)
    id_tipo = db.Column(db.Integer, db.ForeignKey('tipo_doc.id_tipo'))

    tipo_doc = db.relationship('TipoDoc', foreign_keys=[id_tipo])

    def __init__(self, id_documento, codice, id_tipo):
        self.id_documento = id_documento
        self.codice = codice
        self.id_tipo = id_tipo

class Email(db.Model):
    __tablename__ = 'email'

    id_email = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('email_id_email_seq'::regclass)"))
    indirizzo = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, id_email, indirizzo):
        self.id_email = id_email
        self.indirizzo = indirizzo

class Medico(db.Model):
    __tablename__ = 'medico'

    id_medico = db.Column(db.Integer, db.ForeignKey('persona.id_persona'), primary_key=True)
    id_studio = db.Column(db.Integer, db.ForeignKey('stud_leg.id_studio'), unique=True)

    persona = db.relationship('Persona', foreign_keys=[id_medico])
    stud_leg = db.relationship('StudLeg', foreign_keys=[id_studio])

    def __init__(self, id_medico, id_studio):
        self.id_medico = id_medico
        self.id_studio = id_studio

class Telefono(db.Model):
    __tablename__ = 'telefono'

    id_telefono = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('telefono_id_telefono_seq'::regclass)"))
    numero = db.Column(db.String(11), unique=True, nullable=False)

    def __init__(self, id_telefono, numero):
        self.id_telefono = id_telefono
        self.numero = numero

class Paziente(db.Model):
    __tablename__ = 'paziente'

    id_paziente = db.Column(db.Integer, db.ForeignKey('persona.id_persona'), primary_key=True)
    id_medico = db.Column(db.Integer, db.ForeignKey('medico.id_medico'), nullable=False)

    persona = db.relationship('Persona', foreign_keys=[id_paziente])
    medico = db.relationship('Medico', foreign_keys=[id_medico])

    def __init__(self, id_paziente, id_medico):
        self.id_paziente = id_paziente
        self.id_medico = id_medico

class Ricetta(db.Model):
    __tablename__ = 'ricetta'

    id_ricetta = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('ricetta_id_ricetta_seq'::regclass)"))
    id_paziente = db.Column(db.Integer, db.ForeignKey('paziente.id_paziente'))
    id_medico = db.Column(db.Integer, db.ForeignKey('medico.id_medico'))
    campo = db.Column(db.String(300), nullable=False)
    data_emissione = db.Column(db.Date, nullable=False)

    medico = db.relationship('Medico')
    paziente = db.relationship('Paziente')
