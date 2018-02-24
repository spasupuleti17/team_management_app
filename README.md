Team management Application
 
The goal of the project is to implement an HTTP API to support a team-member management application. 
* Database used: MySQL
Following actions are supported:
* Adding a new team member
* Updating already existing team member details
* Deleting existing team member 

Prerequisites
Edit MySQL localhost db username/password in the following file team_management/team_management/settings.py under DATABASES; default is user:root, password: ''

CREATE DATABASE DB_TEAM; 

Installing (team_management/requirements.txt)
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

Running the tests

Adding Team member
curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/users/ -d '{"firstName": "David", "lastName": "Jones", "phone": "+15101234567", "emailId": "DavidJones@test.com", "role": 0}'

Adding another Team member
curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/users/ -d '{"firstName": "Alfonso", "lastName": "Williams", "emailId": "alfonso.w@test.com", "role": 0}'

Listing all Team members
curl -X GET -H "Content-Type:application/json" http://127.0.0.1:8000/users/

Updating Team member with id 1
curl -X PUT -H "Content-Type:application/json" http://127.0.0.1:8000/users/1/ -d '{"firstName": "Richard", "role": 1}'

Delete Team member with id 2
curl -X DELETE -H "Content-Type:application/json" http://127.0.0.1:8000/users/2/

Built With
Django web framework, Python and MySQL

Authors
Sai Babu Pasupuleti 
