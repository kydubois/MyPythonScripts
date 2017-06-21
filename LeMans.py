'''This program creates a database of cars that raced in the 2017 Le Mans 24 hour race.
Developed by Kyle DuBois.  Version 1.0'''

import sqlite3
import urllib.request, urllib.parse, urllib.error
import bs4

conn = sqlite3.connect('Lemans.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Class;
DROP TABLE IF EXISTS Driver;
DROP TABLE IF EXISTS Car;

CREATE TABLE Team (
  id  INTERGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  name    TEXT
);

CREATE TABLE Class (
  id  INTERGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  type    TEXT UNIQUE
);

CREATE TABLE Driver (
  id  INTERGER NOT NULLL PRIMARY KEY AUTOINCREMENT UNIQUE,
  team_id  INTEGER,
  name    TEXT UNIQUE,
  age  INREGER,
  nationality  TEXT UNIQUE
);

CREATE TABLE Car (
  id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  class_id  INTEGER,
  driver_id  INTEGER,
  model    TEXT UNIQUE, make    TEXT, Engine    TEXT
);
''')

url = urllib.request.urlopen('https://www.motorsport.com/lemans/news/full-2017-le-mans-24-hours-entry-list-870556/')
html = url.open()

soup = bs4.BeautifulSoup(html, 'html.parser')

