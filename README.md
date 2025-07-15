# Teacher & Student API

A simple RESTful API for managing teachers and students.  
Built with Laravel and tested using Postman.

## Base URL

http://127.0.0.1:8000/api

### /teacher

| Method | Endpoint        | Description      |
| ------ | --------------- | ---------------- |
| GET    | `/teacher`      | Get all teachers |
| POST   | `/teacher`      | Create a teacher |
| PATCH  | `/teacher/{id}` | Update a teacher |
| DELETE | `/teacher/{id}` | Delete a teacher |

### /student

| Method | Endpoint        | Description      |
| ------ | --------------- | ---------------- |
| GET    | `/student`      | Get all students |
| POST   | `/student`      | Create a student |
| PATCH  | `/student/{id}` | Update a student |
| DELETE | `/student/{id}` | Delete a student |
