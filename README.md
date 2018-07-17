<h1 align="center"><img alt="HealthSystem Logo" src="https://i.imgur.com/NwZwVHN.jpg" width="320"></h1>
<h2 align="center"> Enanched comunication </h2>

### About
**Health system** is an University (Università degli Studi di Napoli Parthenope) project created by **Vittorio Fones** and **Antonio Mentone** (by an idea of Antonio Mentone).<br>
Increasing the comunication between doctors and patients is the main purpose of this project.

### How does it work
* Inside docker containers are working together flask, mongo, nginx, postgres
* nginx is reverse proxying to flask all request and is serving only static files
* flask is creating web page dinamically with Jinja2
* after a successful login, information are queried from postgres
* mongo is used for storing information about biometrics and health purposes


### Some screenshots
| Login | Doctor homepage | Patient Homepage | Mobile
|:--:|:--:|:--:|:--:|
| ![original](https://i.imgur.com/YUOX97u.png) | ![doctor](https://i.imgur.com/5V0xxpP.png) | ![patient](https://i.imgur.com/QaVCYuP.png) | ![mobile](https://i.imgur.com/Sr4sSHd.jpg) |

## Features
Every doctor and patient got the same functions, down below are illustrated doctor first:

Doctor:
- [x] Able to modify personal informations
- [x] Add new patients to personal list
- [x] List all patients
- [x] Detailed info about patients  
- [x] Add/remove prescriptions
- [x] Notify via email about new prescriptions
- [x] Biometrics/health data shown by date

Patient:
- [x] Able to modify personal informations
- [x] Add new biometrics, healthdata
- [x] list all prescriptions
- [x] Check personal doctor informations

### Requirements
The system is developed under OS X and Arch Linux running docker latest version but probably will work the same with other version.

To avoid bugs/crash/errors run this version:

* Docker version 18.03.1-ce, build 9ee9f40
* docker-compose version 1.21.1, build 5a3f1a3
* docker-machine version 0.14.0, build 89b8332

To install Docker software check their website if you are on [OSX](https://docs.docker.com/docker-for-mac/install/) or [Ubuntu Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/).

## Install

```bash
$ git clone https://gitlab.com/xMentos5091/HealthSystem.git
$ cd HealthSystem/hs
$ touch .env
```

Inside .env file copy that:

```bash
  SECRETKEY="my super secret key"
  MAPS=
  GAPI=


  MAIL_USERNAME=
  MAIL_PASSWORD=

  POSTGRES_USER=postgres
  POSTGRES_PASSWORD=postgres
```

If you want to use flask-mail and be able to send emails about new prescriptions, insert Google credential in MAIL_USERNAME and MAIL_PASSWORD.<br>
If you want to use Google Api and LeafLet Api use your own otherwise Map will not render and return error.<br>
n.d.r. **DON'T** use quotes or will return error.

Inside hs folder run:
```bash
$ docker-compose up --build -d
```
If you want to read log don't run in detached mode (remove -d).

Now go to your browser and go to: http://127.0.0.1 and you are ready to go.

### Credential
To login use usernames provided in hs/postgres/dml.sql .

Password for ALL users is "tecweb".

Or here there are some:
Doctor:
* rherrieven14
* blantiff15
* gmenichi16

Patient:
* eballintime0
* ckearford4
* emaraw

### Health box
Also a **Raspberry(+Arduino+XD58C)** is used to create an health box to monitor patients and communicate health info to doctors.
