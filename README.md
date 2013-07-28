oavote
======

A custom online voting tool to fit the requirements of the 'Online-Abstimmung' of Junge Piraten e.V.


Setup
=====


```bash
mkdir oavote
cd oavote
mkdir src env bin 
virtualenv env
source env/bin/activate
cd src 
git clone https://github.com/lutoma/oavote
cd oavote
pip install -r requirements.txt
./mangae.py syncdb
./manage.py migrate
./manage.py runserver
```