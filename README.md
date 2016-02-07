# restful-ner
RESTful API for named entity recognition. 

Build the docker container
```
docker build -t restful-ner .
```

Start the docker container and run the API on port 9000
```
docker run -p 9000:8080 restful-ner 
```

Example usage:
```
curl http://localhost:3000/ner -d "data=Pomona College is located in Claremont, California" -X PUT
```
```
{
    "LOCATION": [
        "Claremont",
        "California"
    ],
    "ORGANIZATION": [
        "Pomona College"
    ]
}

```
