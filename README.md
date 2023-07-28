# Dangerous Writing App (GUI Desktop)

## Description
The Most Dangerous Writing App is a web application for free writing that combats writer's block by deleting 
all progress if the user stops typing for five seconds. It is targeted at creative writers who want to write
first drafts without worrying about editing or formatting.
Developer:	Manuel Ebert
Release: February 29, 2016
Platform:	Web Application
Type:	Text editor
License:	GNU General Public Licence
Website:	www.squibler.io/dangerous-writing-prompt-app

In this code, I make the desktop version of this app.
The user starts writing and if the user stops writing for more than 10 seconds or deletes more than 50 character,
the program stops.

In this version, the text written by the user before stopping the program is saved in a file for him.


## How to run
run following:
```bash
python -m venv env
. env/bin/activate
pip install -r requirements.txt
python main.py
```