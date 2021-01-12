# wasuaje.com Site


This is a personal docker stack made to set up a small pipeline on my personal website, this
stack uses a docker-compose,  with nginx, django and mysql images exposed sharing volumes, this 
allows nginx to serve statics while uwsgi serve dynamic content.

Initial Setup
-------------
* Install pre requisites:
```
 sudo apt  install python-dev python3-dev build-essential libmysqlclient-dev mysql-server -y  # for python2.x installs
 mysqladmin create mydb -uroot -p
 CREATE USER 'myuser'@'localhost' IDENTIFIED BY '123456qwe';
 GRANT ALL PRIVILEGES ON mydb.* TO 'myuser'@'localhost';
 FLUSH PRIVILEGES;
```


**Notice**

Don't forget to connect to mysql container to make django test work


```
docker exec %(docker ps | grep mysql ) mysql -uroot -p
GRANT ALL PRIVILEGES ON mydb.* TO 'myser'@'%' IDENTIFIED BY 'your_password' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```