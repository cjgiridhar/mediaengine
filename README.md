# mediaengine

curl --dump-header - -H "Content-Type: application/json" -H "Authorization: ApiKey admin:<key>" -X POST --data '{"username":"deepti”, "email":"deepti@gmail.com","password":"ad2w", "first_name":"D", "last_name":"Giridhar"}' http://localhost:8000/api/v1/users/

curl --dump-header - -H "Content-Type: application/json" -H "Authorization: ApiKey admin:78fb77da661261a05f3e429108046ac16f032we3" -X POST --data '{"phone_number":"23423432", "title":"ENG", "company":"BJN", "user":{"username":"deepti.1"}}' http://localhost:8000/api/v1/user_profile/

curl --dump-header - -H "Content-Type: application/json" -H "Authorization: ApiKey admin:78fb77da661261a05f3e429108046ac16f032we3" -X POST --data '{"user":{"username":"deepti.1"}}' http://localhost:8000/api/v1/user_billing/
