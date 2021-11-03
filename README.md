# Software Engineering for Machine Learning Assignment

Testing Explanation and Justification  

https://github.com/CMU-313/fall-2021-hw4-redfox/runs/4082631741?check_suite_focus=true  

Our automated test suite for our API is the github action sequence shown above. The test suite’s primary goal is to determine if the microservice can successfully take requests to predict endpoints, and the suite tests this by executing a series of actions. First, we build the docker image for the microservice, and then we test that we can successfully run it. Next, we test the microservice’s ability to receive requests by making requests to it using curl. These requests vary with two requests having high G3s and two requests having low G3s, including zero. If these requests are successful, the API tests pass. We used automated tests to only test build and request functionality since an automated system was more suited to run a variety of requests. We did not use an automated system to test model accuracy and improvement since it was much easier to print the result and have a person do a manual check on if our model had improved. When evaluating our new model’s accuracy with a common testing set, we were able to confirm improvement since our new model’s accuracy (0.99) was greater than the base model’s accuracy (0.51).
