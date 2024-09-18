for adding new users:
  cURL:
    windows: curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d "{\"name\": \"name Test\", \"email\": \"test@example.com\"}"
    linux: curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d '{"name": "name Test", "email": "test@example.com"}'
postman:
  json:
  {
  "name": "John Doe",
  "email": "john@example.com"
  }

for getting all users:
curl http://127.0.0.1:5000/users

for update user:
curl -X PUT http://127.0.0.1:5000/users/9 \ -H "Content-Type: application/json" \ -d "{\"name\": \"Saule Anarova\"}"

for delete user:
curl -X DELETE http://127.0.0.1:5000/users/9
