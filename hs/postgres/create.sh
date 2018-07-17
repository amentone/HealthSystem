#!/bin/bash

#   Create user and db
createuser dbahealthsystem -d -E
createdb healthsystem -O dbahealthsystem
createuser medico -D -E
createuser paziente -D -E
psql -c "alter USER dbahealthsystem WITH PASSWORD 'passwddba'"
psql -c "alter USER medico WITH PASSWORD 'passwdmedico'"
psql -c "alter USER paziente WITH PASSWORD 'passwdpaziente'"
#   Change date format from MDY (Month/Day/Year) to DMY (Day/Month/Year)
#psql -c "ALTER DATABASE healthsystem SET datestyle TO 'ISO, DMY'"
#   Change time zone
#psql -c  "ALTER DATABASE healthsystem SET timezone TO 'Europe/Rome'";
#launch script for permission, tables and first population
psql -d healthsystem -U dbahealthsystem -W -f /scripts/ddl.sql
psql -d healthsystem -U dbahealthsystem -W -f /scripts/dcl.sql
psql -d healthsystem -U dbahealthsystem -W -f /scripts/dml.sql
