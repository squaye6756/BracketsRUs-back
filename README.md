# Brackets-R-US
Back-end server for Brackets-R-Us.

[Link to live site](https://bracketsrus.herokuapp.com/api/tournaments)

## Technologies Used
  * Django
  * Python
  * SQL
  * Postgres
  * CORS

## Approach Taken
* cors enabled, restricting access from unknown origins
* bcrypt password hashing used in user authentication
* many-to-many relationship between users and tournaments
* pseudo (annoyingly so) many-to-many relationship between users and brackets
* one-to-many relationship between owners and tournaments
* one-to-many relationship between tournaments and brackets
* one-to-many relationship between champion and tournaments

## Known Issues
* player list stored in brackets would ideally be a manytomany field, but heroku's version of Postgres (13.4 at this time) does not maintain the randomized order of the bracket pairings.
* password security could be increased by limiting the hashed passwords from being transmitted to the front end.
