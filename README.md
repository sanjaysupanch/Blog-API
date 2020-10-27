# REST API example assignment


## Install

    pip install -r requirements.txt

## Run the app

    port -p 8000


# REST API

The REST API to the assignment app is described below.

## Login
   `Request`
   
    curl -i POST -H "Content-Type: application/x-www-form-urlencoded" -d 'username=s&password=s' 'http://127.0.0.1:8000/api/login/'
   
   `Response`
   
    HTTP/1.1 200 OK
    Date: Mon, 26 Oct 2020 12:23:59 GMT
    Server: WSGIServer/0.2 CPython/3.8.5
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: POST, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 50
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Set-Cookie:  csrftoken=QsVPCvfaErIvlQiJfq8z4eD4f0xICmFYlPHO2jXVHoWahThb1OZowcJVOUPqDdQI; expires=Mon, 25 Oct 2021 12:23:59 GMT; Max-Age=31449600; Path=/;         SameSite=Lax
    Set-Cookie:  sessionid=wwn9y0koymbz8ejl7qqxboypjrx1y2b2; expires=Mon, 09 Nov 2020 12:23:59 GMT; HttpOnly; Max-Age=1209600; Path=/; SameSite=Lax

    {"key":"b2487a31410fc0bc4c72c5889124621a140fdbbe"}
    

## GET List of story

### Request

`GET /api/story/`

    curl -i -X GET -H "Authorization: Token b2487a31410fc0bc4c72c5889124621a140fdbbe" -H "Content-Type: application/x-www-form-urlencoded"
    'http://127.0.0.1:8000/api/story/'

### Response

    HTTP/1.1 200 OK
    Date: Mon, 26 Oct 2020 13:38:02 GMT
    Server: WSGIServer/0.2 CPython/3.8.5
    Content-Type: application/json
    Vary: Accept
    Allow: GET, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 789
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

       {"count":6,"next":"http://127.0.0.1:8000/api/story/?limit=5&offset=5","previous":null,"results":[
       {"id":1,"tags":["s","san"],"title":" my name is  san","description":"kumar","body":" jfakjf jadksl flja","published":false,"timetoreads":               
       {"id":1,"hours":0,"mins":0,"secs":1}},{"id":2,"tags":["JAVA", "C"],"title":"dd","description":"d","body":"d","published":false,"timetoreads":
       {"id":2,"hours":0,"mins":0,"secs":1}},{"id":3,"tags":["JAVA", "C"],"title":"d","description":"d","body":"d","published":false,"timetoreads":
       {"id":3,"hours":0,"mins":0,"secs":1}},{"id":4,"tags":[],"title":"d","description":"d","body":"d","published":false,"timetoreads":
       {"id":4,"hours":0,"mins":0,"secs":1}},{"id":5,"tags":["JAVA", "C"],"title":"d","description":"d","body":"d","published":false,"timetoreads":
      


## Create Story

### Request

`POST /api/post/`

    curl -i -X POST -H "Authorization: Token b2487a31410fc0bc4c72c5889124621a140fdbbe" -H "Content-Type: application/x-www-form-urlencoded" -d 
    '{"tags":["JAVA","C"],"title":"Programming language","description":"xyz","body":"You hav to belive"} ' 'http://127.0.0.1:8000/api/post/'

### Response

    HTTP/1.1 201 Created
    Date: Mon, 26 Oct 2020 13:38:02 GMT
    Server: WSGIServer/0.2 CPython/3.8.5
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Location: /api/story/7
    {"id":7, "tags":["JAVA","C"],"title":"Programming language","description":"xyz","body":"You hav to belive"}

** Note: "Time is calculating by Algorithm"

## GET for UPDATE story

### Request

`GET /api/story/id/`

    curl -i -X GET -H "Authorization: Token b2487a31410fc0bc4c72c5889124621a140fdbbe" -H "Content-Type: application/x-www-form-urlencoded"
    'http://127.0.0.1:8000/api/story/7/'

### Response

    HTTP/1.1 200 OK
    Date: Mon, 26 Oct 2020 14:01:19 GMT
    Server: WSGIServer/0.2 CPython/3.8.5
    Content-Type: application/json
    Vary: Accept
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 178
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

    {"id":7,"tags":["JAVA","C"],"title":"Programming language","description":"xyz","body":"You hav to belive","published":false,"timetoreads":
    {"id":7,"hours":0,"mins":0,"secs":2}}

## UPDATE story

### Request

`PUT /api/story/id/`

    curl -i -X PUT -H "Authorization: Token b2487a31410fc0bc4c72c5889124621a140fdbbe" -H "Content-Type: application/x-www-form-urlencoded" -d ' {"id":7,"tags":
    ["JAVA","C"],"title":"Programming language","description":"xyz","body":"You hav to belive","published":false,"timetoreads":
    {"id":7,"hours":0,"mins":0,"secs":3}} ' 'http://127.0.0.1:8000/api/story/7/' 

### Response

    HTTP/1.1 200 OK
    Date: Mon, 26 Oct 2020 14:01:19 GMT
    Server: WSGIServer/0.2 CPython/3.8.5
    Content-Type: application/json
    Vary: Accept
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 178
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin


    {"id":7,"tags":["JAVA","C"],"title":"Programming language","description":"xyz","body":"You hav to belive","published":false,"timetoreads":
    {"id":7,"hours":0,"mins":0,"secs":3}}

## Publish Story

### Request

`GET /api/publish/id/publish/` 
    

    curl -i -X GET -H "Authorization: Token e230133d2321572384dc281082736eb9e3da6e7d" -H "Content-Type: application/x-www-form-urlencoded" 'http://127.0.0.1:8000/api/story/1/publish/'


### Response

    HTTP/1.1 200 OK
    Date: Mon, 26 Oct 2020 21:05:31 GMT
    Server: WSGIServer/0.2 CPython/3.8.5
    Content-Type: application/json
    Vary: Accept
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 609
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

    {"id":1,"tags":["C","C++"],"title":"Programming Language","description":"xyz","body":"A programming language is a formal language comprising a set of instructions that produce various kinds of output. Programming languages are used in computer programming to implement algorithms. Most programming languages consist of instructions for computers. A programming language is a formal language comprising a set of instructions that produce various kinds of output. Programming languages are used in computer programming to implement algorithms. Most programming languages consist of instructions for computers."}

    **Note: We can also do PUT and DELETE.

## Publish and unpublish a story Filter

### Request

`GET /api/publish/0/` 
    
    for filter for all publish 1 and for not publish 0.

    curl -i -X GET -H "Authorization: Token b2487a31410fc0bc4c72c5889124621a140fdbbe" -H "Content-Type: application/x-www-form-urlencoded"  
    'http://127.0.0.1:8000/api/publish/0/' 

### Response

    HTTP/1.1 200 OK
    Date: Mon, 26 Oct 2020 14:36:52 GMT
    Server: WSGIServer/0.2 CPython/3.8.5
    Content-Type: application/json
    Vary: Accept
    Allow: GET, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 793
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

    {"count":7,"next":"http://127.0.0.1:8000/api/publish/0/?limit=5&offset=5","previous":null,"results":[
    {"id":1,"tags":["s","san"],"title":" my name is san","description":"kumar","body":" jfakjf jadksl flja","published":false,"timetoreads":
    {"id":1,"hours":0,"mins":0,"secs":1}},{"id":2,"tags":[],"title":"dd","description":"d","body":"d","published":false,"timetoreads":
    {"id":2,"hours":0,"mins":0,"secs":1}},{"id":3,"tags":[],"title":"d","description":"d","body":"d","published":false,"timetoreads":
    {"id":3,"hours":0,"mins":0,"secs":1}},{"id":4,"tags":[],"title":"d","description":"d","body":"d","published":false,"timetoreads":
    {"id":4,"hours":0,"mins":0,"secs":1}},{"id":5,"tags":[],"title":"d","description":"d","body":"d","published":false,"timetoreads":
    {"id":5,"hours":0,"mins":0,"secs":1}}]}

## Find all the words in story body that have spelling mistakes

### Request

`GET /api/spellcheck/id/`

    curl -i -X GET -H "Authorization: Token b2487a31410fc0bc4c72c5889124621a140fdbbe" -H "Content-Type: application/x-www-form-urlencoded"
    'http://127.0.0.1:8000/api/spellcheck/7/'

### Response

    HTTP/1.1 200 OK
    Date: Mon, 26 Oct 2020 15:25:39 GMT
    Server: WSGIServer/0.2 CPython/3.8.5
    Content-Type: application/json
    Vary: Accept
    Allow: GET, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 38
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin


    {"misspelledWords": ["hav", "belive"]}
