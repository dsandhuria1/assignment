### Setup steps

## 1) Install python 

  mkdir project  <br />
  cd project <br />
  python3 -m venv venv

## 2) Activate Environment
  . venv/bin/activate

## 3) Install Flask
  pip install Flask
  > Alternatively refer to https://flask.palletsprojects.com/en/2.2.x/installation/


### Run the flask server

  ksh run_server.ksh <br />
  This script sets the PORT environment variable and brings up the server

### To make the request 
curl localhost:$PORT/employees
