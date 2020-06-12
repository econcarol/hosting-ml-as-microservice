How to make API call to our simple model and analyze a review?

(1) Anaconda Prompt: cd [path to the folder that has app.py]
(2) Anaconda Prompt: set FLASK_APP = app
(3) Anaconda Prompy: flask run
(4) copy the URL where the site is running
(5) open sentiment.html in a text editor: xhttp.open("POST", "[past the URL here]", true)
(6) save sentiment.html and open it in a web browser
(7) enter a review in the textbox and hit "Analyze It!" button to see the predicted sentiment


To make the site available on the web, we can create a container and host it on GCP or AWS. 
- The docker folder has all the files needed to create the container
- Follow the instructions in Part 4 to create the docker image
- Follow the instructions on GCP or AWS to host the container online and get the public IP
- In sentiment.html, update the URL with the public IP
- Use GCP or AWS file hosting services to host sentiment.html 
- Open the file URL and change https:// to http://

This simple app is available on my website: http://carolcui.com/myapps/review-sentiment/review-sentiment.html
