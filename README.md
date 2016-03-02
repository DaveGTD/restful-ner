# restful-ner
RESTful API for named entity recognition. 

 
   
   
Start the docker container and run the API on port 3000:
```
docker run -p 3000:3000 mbartoli/restful-ner 
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
              

               
Docker Hub: [mbartoli/restful-ner](https://hub.docker.com/r/mbartoli/restful-ner/)
