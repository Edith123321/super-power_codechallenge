# super-power_codechallenge

A Flask REST API for managing heroes, their powers, and relationships between them.

## Features

- RESTful endpoints
- SQLite database
- Flask-Migrate for database migrations
- CRUD operations for Heroes and Powers
- Association management via HeroPowers(The junction table)

## Setup

1. Clone the repository
2. Activate the virtual environment using pipenv
   ```bash
   pipenv install
   pipenv shell
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initiaize the database
   ```bash 
      flask db init
      flask db migrate -m "Initial migration"
      flask db upgrade
       python seed.py
    ```
5. Run the server 
  ```bash
python app.py
```

## Route Endpoints 
### Heros
#### GET /heroes
To display all the heroes in the terminal, run the command;
```bash
   curl http://localhost:5555/heroes
```
#### GET /heros/:id
To display the contents of a specific id of heroes. Run
``` bash
    curl http://localhost:5555/heroes/1
```
#### POST /heroes
To add a new hero on the list of existing heroes
``` bash
  curl -X POST http://localhost:5555/heroes \
  -H "Content-Type: application/json" \
  -d '{"name": "Peter Parker", "super_name": "Spider-Man"}'
  ```
#### PATCH /heroes
To update a hero on the terminal
```bash
  curl -X PATCH http://localhost:5555/heroes/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Miles Morales"}'
```
#### DELETE /heroes
To delete a hero from the existing list of the heroes
```bash
curl -X DELETE http://localhost:5555/heroes/1
```

### Powers
#### GET /powers
To display all the powers available with their description. Run 
``` bash
curl http://localhost:5555/powers
```
#### GET /powers/:id
To display the descriptions of a specific power, run
```bash
   curl http://localhost:5555/powers/1
```

#### POST /Powers
To add a new hero on the list of existing heroes
``` bash
  curl -X POST http://localhost:5555/powers \
  -H "Content-Type: application/json" \
  -d '{"name": "Telekinesis", "description": "Move objects with mind"}'
  ```
#### PATCH /powers/:id
To update a power on the terminal
```bash
 curl -X PATCH http://localhost:5555/powers/1 \
  -H "Content-Type: application/json" \
  -d '{"description": "Can move objects with mind up to 1000kg"}'
```
#### DELETE /heroes/:id
To delete a power from the existing list of the heroes
```bash
curl -X DELETE http://localhost:5555/powers/1
```

## Database layout/schema used
```bash
heroes
- id (Integer)
- name (String)
- super_name (String)

powers
- id (Integer)
- name (String)
- description (String)

hero_powers
- id (Integer)
- hero_id (Integer, ForeignKey)
- power_id (Integer, ForeignKey)
- strength (String)
```



