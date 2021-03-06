Pokr - Politics in Korea
==================================

**Pull requests are always welcome.**

## Installation

1. Install dependencies

    - Ubuntu

            $ sudo apt-get install nodejs postgresql-9.3 npm python-psycopg2 node-less node-uglify
            $ sudo pip install -r requirements.txt
            $ sudo make install

<<<<<<< HEAD
    - Mac OS X

            $ brew install node postgresql
            $ npm install less uglify-js -g
            $ pip install -r requirements.txt
            $ pip install psycopg2
            $ make install
=======
            Install postgresql (http://www.postgresql.org/download/)
            Install nodejs to use npm (http://nodejs.org/download/)
            Install Redis (http://redis.io/download)
            (sudo)# apt-get update
            (sudo)# apt-get install python python-dev python2.7 libpq-dev libevent-dev
            (sudo)# npm install less uglify-js@1 -g
    - Mac OS X:

            Install Homebrew (http://mxcl.github.com/homebrew/)
            Install nodejs to use npm (http://nodejs.org/download/)
            Install Redis (http://redis.io/download)
            (sudo)# brew install python postgresql libevent
            (sudo)# initdb /usr/local/var/postgres -E utf8
            (sudo)# npm install less uglify-js@1 -g
>>>>>>> added troubleshooting for macosx

1. Create & modify configuration files

        $ make init
        $ createuser postgres
    - Set password for user "postgres" in PostgreSQL
    - Modify `alembic.ini`
        - `ID_HERE`: postgres id (ex: postgres)
        - `PASSWD_HERE`: postgres pw
        - `HOST_HERE`: postgres host (ex: localhost)

1. Create & init DB (You should first obtain a `pokrdb.dump` from [here](https://drive.google.com/file/d/0BwxUh0GzMJ4VMXJncHM4Qm1LZDQ/view?usp=sharing))

<<<<<<< HEAD
        $ sudo -u postgres psql -h localhost -U postgres -c 'CREATE DATABASE pokrdb;'
        $ sudo -u postgres psql -d pokrdb -f pokrdb.dump
        $ ./shell.py db init
        $ alembic stamp head
=======
1. Install python packages
    - sudo pip install git+https://github.com/teampopong/popong-models.git
pip install git+https://github.com/teampopong/popong-data-utils.git
    - sudo pip install git+https://github.com/teampopong/popong-models.git
pip install git+https://github.com/teampopong/popong-nlp.git
    - sudo pip install nltk

1. Create & modify configuration files:
    - Do `make init`
    - Then, settings.py should be created.
    - In alembic.ini, modify as below.
        - `ID_HERE`: postgres id
        - `PASSWD_HERE`: postgres pw
        - `HOST_HERE`: postgres host
>>>>>>> added troubleshooting for macosx

## Run Server

<<<<<<< HEAD
    $ ./run.py [-d] [-l LOCALE] [--port PORT]
=======
        $ make init_db
>>>>>>> added troubleshooting for macosx

## Update Data

1. Bills

        $ ./shell.py bill update "some/where/*.json" # from files
        $ ./shell.py bill update --source redis  # from Redis queue
        $ ./shell.py bill update --source db  # existing bills of the current session

1. Bill Keywords

        $ ./shell.py bill_keyword update "some/where/*.txt"

1. Candidacies

        $ ./shell.py candidacy update "some/where/*.json"

<<<<<<< HEAD
=======

## Run Server

    $ ./run.py [-d] [-l LOCALE] [--port PORT]

## Troubleshooting

- Mac OS X:
    - Trouble with installing psycopg2 -> install postgresql first.
        - brew install postgresql
    - Trouble with installing gevent -> install libevent first.
        - brew install libevent
        - export LDFLAGS=-L/usr/local/lib/
        - export CFLAGS=-I/usr/local/include/
        - sudo pip install gevent
    - Before doing createdb (postgres), do:
        - postgres -D /usr/local/var/postgres
    - env: python2: No such file or directory 
        - sudo ln -s /usr/bin/python /usr/bin/python2
        - On Mac, you don't have python2. Thus, make a symbolic link.
    - You need latest version of sqlalchemy before doing make init\_db
        - sudo pip install --upgrade sqlalchemy
    - Trouble with installing konlpy (Mac OS X version >= 10.9)
        1. It requires JPype1 before installing konlpy.
        1. Download latest version of jpype from [here](https://pypi.python.org/pypi/JPype1/0.5.5.4)
        1. setup.py of JPype1 has an error to locate jdk path. You should correct it first.
            1. java\_home in line 52~54 should be '/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.9.sdk/System/Library/Frameworks/JavaVM.framework/Versions/A/'
            1. Insert this at the first line of _def getJDKIncludes(java\_home):_
                - java\_home = '/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.9.sdk/System/Library/Frameworks/JavaVM.framework/Versions/A/'
            1. Yes, you should have Xcode.app first. (It's free!)


>>>>>>> added troubleshooting for macosx
## License
[Apache v2.0](http://www.apache.org/licenses/LICENSE-2.0.html)
