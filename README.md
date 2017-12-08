## Log Analysis

This project is about creating reporting tools in python. This reporting tool will run from the command line using Gitbash. It won't take any input from the user. Instead, it will connect to the database, use SQL queries to analyze the log data, and print out the answers to following questions.

1.	What are the most popular three articles of all time? 
2.	Who are the most popular article authors of all time? 
3.	On which days did more than 1% of requests lead to errors? 

## Requirements 
1. Python 2 and up
2. Vagrant
3. VirtualBox

## Download and Installation
1.	Install Vagrant https://www.vagrantup.com/ and VirtualBox https://www.virtualbox.org/
2.	Download or Clone fullstack-nanodegree-vm repository. https://github.com/udacity/fullstack-nanodegree-vm
3.  Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
4.	Unzip this file your project folder after downloading it. The file inside is called newsdata.sql.

## Running this program
From your GitBash 
1.	cd to your project folder ( e.g. if the project folder is in desktop with folder name as project)
```
$ cd desktop/project
```
2.	Vagrant up (to load the machine)
3.	Vangrant ssh (logging in)
4.	cd  /vagrant
5.	To load the database use the following command line

```
psql -d news -f newsdata.sql;
```
## To get data, or running queries use following cmd line:
```
$; python3 news.py
```
