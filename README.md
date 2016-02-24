# restful-ner
RESTful API for named entity recognition. 

 
   
   
Start the docker container and run the API on port 3000:
```
docker run -p 3000:3000 docker pull mbartoli/restful-ner 
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

Note:
The current implementation requires starting the ner server and flask application manually. You can do this by running the following two commands
```
java -mx1000m -cp stanford-ner.jar edu.stanford.nlp.ie.NERServer -loadClassifier classifiers/english.muc.7class.distsim.crf.ser.gz -port 8080 -outputFormat inlineXML &
python /home/restful-ner/ner/restful-ner.py
```
              
              
Docker Hub: [mbartoli/restful-ner](https://hub.docker.com/r/mbartoli/restful-ner/)
