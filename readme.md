### Todo:

1. Add Yaml, Toml converter.
2. Go grpc server.
3. Github application - get github username on login and store it on a cookie.
4. After user login - user sends a file as a input in web with basic github auth and results are stored in a gist and shared with the user.
5. Store user details like - github ID, username, filename, file created date, file extension in a mysql table.
6. Gin+GRPC server.
7. Use postgres DB.
8. CRUD add functionality - CREATE, GET ALL gist created by user, DELETE gist


#### Go guideline
1. To initialize a project with go module, run:
```go mod init your-project-name```

2.Add missing and/or remove unused modules:
```go mod tidy```

3. You can even vendor the modules in your project directory:
```
go mod vendor
```

Creating gists:
```
curl --location --request POST 'https://api.github.com/gists' \
--header 'Authorization: Bearer <ACCESS_TOKEN>' \
--header 'Content-Type: application/json' \
--header 'Cookie: _octo=GH1.1.329936248.1614167878; logged_in=no' \
--data-raw '{"public":true,"files":{"test.txt":{"content":"String file contents"}}}'
```