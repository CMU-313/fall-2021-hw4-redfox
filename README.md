# Software Engineering for Machine Learning Assignment

This is the implementation of a Machine Learning microservice to determine the various predictors of student performance. 

[Enter model features here]

Deployment Instructions

1) Build and deploy the models by using Docker and Flask
2) In order to run the flask service, build a docker container using run docker build -t ml:latest . as part of the dockerfile directory. Then run docker run -d -p 5000:5000 ml
3) The default route to run the service is on port http://localhost:5000 and the prediction service lies at curl http://localhost:5000/predict
4) Run Jupyter Notebook and navigate to the notebook to view and analyze the given Student Performance dataset and view the trained ML model and the accuracy of our trained model.

API Specifications

1) Perform the API call using the url: http://localhost:5000/predict?age=16&absences=3&health=3&studytime=5&traveltime=5&Walc=2&goout=4&famrel=5
2) The input data expected by the API are values of the various prediction features training our model and it is predicting the quality of the student with a certain level of accuracy. The sample prediction values of the features are provided in the above API call.
3) The output of the service is a numeric value that determines the quality of the student after predicting the data.


Testing Explanation and Justification  

https://github.com/CMU-313/fall-2021-hw4-redfox/runs/4082631741?check_suite_focus=true  

Our automated test suite for our API is the github action sequence shown above. The test suite’s primary goal is to determine if the microservice can successfully take requests to predict endpoints, and the suite tests this by executing a series of actions. First, we build the docker image for the microservice, and then we test that we can successfully run it. Next, we test the microservice’s ability to receive requests by making requests to it using curl. These requests vary with two requests having high G3s and two requests having low G3s, including zero. If these requests are successful, the API tests pass. We used automated tests to only test build and request functionality since an automated system was more suited to run a variety of requests. We did not use an automated system to test model accuracy and improvement since it was much easier to print the result and have a person do a manual check on if our model had improved. When evaluating our new model’s accuracy with a common testing set, we were able to confirm improvement since our new model’s accuracy (0.99) was greater than the base model’s accuracy (0.51).
