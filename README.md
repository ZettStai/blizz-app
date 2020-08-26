# Blizz-App


Blizz-App is an example of a simple containerized application. The application itself will return the current/date and time. that allows `<insert_target_audience>` to do `<action/task_it_does>`.

Additional line of information text about what the project does. Your introduction should be around 2 or 3 sentences. Don't go overboard, people won't read it.

## Application Requirements

* Write a web application in your language of choice that returns the current date/time in JSON

This web application is written in Python Flask. After sending a request to the API, it returns the date in JSON.

* Write a simple test application that will query this “API” X times per second and record success/failure/TTLB (Time to last byte)

test.py is written to test the API. Below example will run the test 5 times per second. 

```
python3 test.py 5
```

* Perform a blue-green deploy with the method/technology of your choosing while the test application is running and demonstrate there were no failed requests

Blue and green deployment and service yamls are included. The blue deployment is from version 1.0.0 of the app and the green deployment is to run version 2.0.0 of the app. Both versions will be able to run simultaneously. Once the green deployment is tested, we can switch all pods to use version 2.0.0 seemlessly.

* Go from a single instance of v1 to a single instance of v2 gracefully

```
    kubectl create -f deployment.yaml
    kubectl create -f deployment-green.yaml
    
    kubectl create -f service.yaml
    kubectl create -f service-green.yaml
 ```

* The team suggests using the AWS Free Tier or GCP Free Tier to complete this task.

This was deployed on GCP Free Tier.
