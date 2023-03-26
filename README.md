#FlaskApp

1. Create a FlaskApp folder
	
> mkdir FlaskApp
> cd FlaskApp

2. Create and activate a virtal environment
	
> py -3 -m venv venv
> venv\Scripts\activate
  
4. Flask installation

> pip install -r requirements.txt

5. Declare hello.py file as flask app.

> set FLASK_APP=hello.py

6. Run the Flask app

> flask run

7. Ryn docker
> docker run --publish 8000:5000 -e FLASK_APP=hello.py project-backend
