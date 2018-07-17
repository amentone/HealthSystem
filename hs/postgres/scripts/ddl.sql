DROP TABLE RICETTA CASCADE;
DROP TABLE PAZIENTE CASCADE;
DROP TABLE MEDICO CASCADE;
DROP TABLE STUD_LEG CASCADE;
DROP TABLE PERSONA CASCADE;
DROP TABLE EMAIL CASCADE;
DROP TABLE TELEFONO CASCADE;
DROP TABLE DOCUMENTO CASCADE;
DROP TABLE INDIRIZZO CASCADE;
DROP TABLE TIPO_DOC CASCADE;

CREATE TABLE TIPO_DOC
(
	ID_TIPO serial primary key,
	TIPO_DOCUMENTO varchar(50)
);

CREATE TABLE INDIRIZZO
(
	ID_INDIRIZZO serial primary key,
	CAP int not null,
	STRADA varchar(100) not null
);

CREATE TABLE DOCUMENTO
(
	ID_DOCUMENTO serial primary key,
    CODICE varchar(50) not null unique,
	ID_TIPO integer references TIPO_DOC(ID_TIPO)
);

CREATE TABLE TELEFONO
(
	ID_TELEFONO serial primary key,
	NUMERO varchar(11) not null unique
);


CREATE TABLE EMAIL
(
	ID_EMAIL serial primary key,
	INDIRIZZO varchar(50) not null unique
);

CREATE TABLE PERSONA
(
	ID_PERSONA serial primary key,
	NOME varchar (50) not null,
	COGNOME varchar (50) not null,
	USERNAME varchar(50) not null,
	PASSWORD varchar(100) not null,
	CF varchar (16) not null unique,
	constraint CFConsentito check(CF ~ '^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$'),
	ID_INDIRIZZO integer unique not null references INDIRIZZO(ID_INDIRIZZO),
    ID_EMAIL integer unique not null references EMAIL(ID_EMAIL),
    ID_DOCUMENTO integer unique not null references DOCUMENTO(ID_DOCUMENTO),
    ID_TELEFONO integer unique not null references TELEFONO(ID_TELEFONO),
	LUOGO_NASCITA varchar(50) not null,
	DATA_NASCITA date not null
);

CREATE TABLE STUD_LEG
(
	ID_STUDIO serial primary key,
	ID_INDIRIZZO integer references INDIRIZZO(ID_INDIRIZZO),
	ORARIO_INIZIO time not null,
	ORARIO_FINE time not null,
	DA_GIORNO varchar(20) not null,
	A_GIORNO varchar(20) not null

);

CREATE TABLE MEDICO
(
	ID_MEDICO integer primary key references PERSONA(ID_PERSONA),
	ID_STUDIO integer references STUD_LEG(ID_STUDIO)
);

CREATE TABLE PAZIENTE
(
	ID_PAZIENTE integer primary key references PERSONA(ID_PERSONA),
	ID_MEDICO integer references MEDICO(ID_MEDICO)
);

CREATE TABLE RICETTA
(
	ID_RICETTA serial primary key,
	ID_PAZIENTE integer references PAZIENTE(ID_PAZIENTE),
	ID_MEDICO integer references MEDICO(ID_MEDICO),
	CAMPO varchar(300) not null,
	DATA_EMISSIONE date not null
);
