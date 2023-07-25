
# IronHomework

This is a partial implementation.
Scope: Customer API + MongoDB

How to run it?


```
git clone https://github.com/JaKourdi/IronHome.git
cd IronHome
docker-compose up --build
```

---
# Idea 

I'm more conformable with Python rather than Javascript.
Flask is more minimal from Django, so less bloat for the scope of the assignment.

# Structure

Model class for User identity to model the underlining BSON document.
Powered by MongoEngine ODM.


Validation for User Object is achieved using validators (helper functions).
For username & password properties regex validation seems like the relevant approach (not supported by marshmallow)
Schema validation is achieved for the Item and Order identities Powered by Marshmallow.


Routing module that encapsulate the backend routing abilities.

Restricting access with JWT token is achieved by decorator design pattern

https://refactoring.guru/design-patterns/decorator

---

# How can I test it?

* Boostrap data to MongoDB
```
# navigate to MongoDB container UI
http://localhost:8081/db/customermgmt/

```

* JWT Token + authorized routing

```
curl -X POST http://localhost:5000/auth/login  -H 'Content-Type: application/json' -d '{"username":"dummy1","password":"IRON552!$source"}'

```
See Generate JWT token - web app can auth user and use the JWT to access restricted page.

Value is saved as a session under user_id

API Token is for 24h
```

{
  "data": {
    "_id": "64c02aa05be48c23a34bcf5e",
    "active": true,
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjRjMDJhYTA1YmU0OGMyM2EzNGJjZjVlIn0.iv5Q7tIbrWzsTg2PSEXNUpphcc-cQUfCBTaCqg_dpy4",
    "username": "dummy1"
  },
  "message": "Successfully fetched auth token"
}

```
Attempt to access API without a token / for invalid token a diff error will occur.
```
curl http://localhost:5000/order/list                     

```

```
{
  "data": null,
  "error": "Unauthorized",
  "message": "Authentication Token is missing!"
}

```

Use token to fetch all the orders under the authenticate user.
```
 curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" http://localhost:5000/order/list
 ```
 ```
 {"_id": {"$oid": "64c02aa05be48c23a34bcf64"}, "name": "Order1", "description": "Description 1", "total": 11.99, "items": [{"itemId": {"$oid": "64c02aa05be48c23a34bcf60"}}], "usernameId": {"$oid": "64c02aa05be48c23a34bcf5e"}}, {"_id": {"$oid": "64c02aa05be48c23a34bcf65"}, "name": "Order2", "description": "Description 2", "total": 12.99, "items": [{"itemId": {"$oid": "64c02aa05be48c23a34bcf61"}}], "usernameId": {"$oid": "64c02aa05be48c23a34bcf5e"}}]%  
```

* User creation:
```

curl -X POST http://localhost:5000/user/add -H 'Content-Type: application/json'  -d '{"username":"my_login","password":"YyPasswo2112rd!!jsjsjsj"}'

```
```
{
  "data": {
    "_id": "64c02f3b236c971c10a488b8",
    "active": true,
    "username": "my_login"
  },
  "message": "Successfully created new user"
}
```

* Health check

```
curl http://localhost:5000/hello
```
