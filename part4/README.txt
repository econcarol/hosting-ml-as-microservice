Q1: How to build docker image in Windows using Docker Toolbox?

My Windows 10 Home build version does not meet Docker Desktop requirements, so I use Docker Toolbox instead. 

(1) Open Docker CLI from Kitematic 
(2) Windows PowerShell: cd [path to the web folder]
(3) Windows PowerShell: $env:COMPOSE_CONVERT_WINDOWS_PATHS=1
(4) Windows PowerShell: docker-compose build
(5) Windows PowerShell: docker-compose up
(6) test the model
(6a) browse to http://[provided IP address, mine is 192.168.99.100]:5000/predict?review=great+movie 
(6b) CMD: curl -d "{\"review\":\"great movie\"}" http://192.168.99.100:5000/predict
(7) Windows PowerShell: hit Ctrl + C to stop image


Q2: How to push image to Docker Hub?

(1) Windows PowerShell: docker login
(2) docker tag [image ID] [your docker username]/[name of your repository]
(3) docker push [your docker username]/[name of your repository]
(4) go to Docker Hub and you should see the image there
