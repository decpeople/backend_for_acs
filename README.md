# Backend for ACS
`##Structure avia-food`

 *Backend for the initial start of the project, where the mechanics are displayed
An airline is being created, an airline can have three types of rotation, each rotation has a team type (economy class, business class, flight attendants, pilot, commander), a type of food is added for each of the team members (breakfast, lunch, dinner) any number of menu images can be added to each type of food.*


`##Installing and launching the project`
Clone the repository using Git:
```git clone https://github.com/your-username/your-project.git```


Go to the project directory:
```cd your-project```

Create a virtual environment using venv:
```python 3 -m ven ven```

Activate the virtual environment:
Note that for Windows, the command will be different: v env\Scripts\activate.
```source venv/bin/activate```

Install dependencies from the file requirements.txt:
```pip install -r requirements.txt```

Apply migrations:
```python manage.py migrate```

Start the server:
```python manage.py runserver```

After starting the server, you will be able to open the project in the browser at http://127.0.0.1:8000 /.

To stop the server, use the keyboard shortcut Ctrl+C.

After completing the work, you can deactivate the virtual environment.:
```deactivate```

Note that for Windows, the command will be different: deactivate.

![Alt text](images/readme.jpg "Optional title")
