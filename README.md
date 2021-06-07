# TodoController
Django rest framework for TodoController and JWT authentication

After running the code, we go to the server "http://127.0.0.1:8000/api/"

We get following json information:
{
    "get - get one": "get/id/",
    "getall - get all": "getall/",
    "put - update": "put/id/",
    " - create": "create/",
    "delete": "delete/id/"
}

Which indicates that "http://127.0.0.1:8000/api/get/id/" is for getting one data "server/getall/" for getall and so on.

using "http://127.0.0.1:8000/api/authcontroller/register" in thunder client of vscode we create new user providing json data example:
{
    "username": "new0",
    "password": "1234",
    "FirstName": "Abhi",
    "LastName": "Tiwari",
    "Email": "at22abhi@gmail.com",
    "Isactive": true,
    "Roles": "Admin"
}
and send POST request to get the token and pasting the access token to the server "http://127.0.0.1:8000/api/authcontroller/token/verify/" in the Token area to verify the token.
If the token is valid we will see that token is accepted with empty json data otherwise we will get following json:
{
    "detail": "Token is invalid or expired",
    "code": "token_not_valid"
}
