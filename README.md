# TD7A4 - Cloud Computing - Git & GitHub
## :star2: Goal
Create a container with flask that connects to a mongodb which runs on another container, fetches data and shows it on a webpage on your host machine.

Add to your application a feature, which reads a text file on your host and shows the content on a web page. Any changes in the content of this file should be shown by refreshing the web page. (by using a bind mount) 

Explain how you can migrate it! How to share it with another instance of the same database engine.

## :construction_worker_woman: Prerequisites
Be sure to have docker and docker compose installed, check with
```
docker --version
docker-compose --version
```

## :scissors: Fork the repository
And then clone it, go to the directory with:
```
git clone git@github.com:<your_github_username>/TD7A4.git
cd TD7A4
```

## :chart_with_downwards_trend: Without Docker compose
1. Pull the docker images (python, mongo)
```
docker pull mongo
docker pull python
```
It will pull the latest version as the default one without giving a tag, if you dont have it already.

2. Create a bridge network for the containers to connect to!
```
docker network create --driver bridge <your_bridge_network_name>
```

3. Start the MongoDB container by specifying the network and the port
```
docker run -d --network <your_bridge_network_name> --name <your_mongo_container_name> -p 27017 mongo
```

4. Build the Docker image for the Flask application
```
docker build -t <your_new_image_name> .
```

5. Create the docker Volume
```
docker volume create <your_volume_name>
```

6. Start the Flask container, specifying the network, bind mount, volume
```
docker run -d 
  --network <your_bridge_network_name> 
  --name <your_new_container_name> 
  -p 5000:5000 
  -v /path_to_your_directory/TP7A4/new_page:/app/data <your_new_image_name> 
  -v <your_volume_name>:/data/db mongo 
```

## :chart_with_upwards_trend: With Docker compose
Use the command
```
docker compose up -d
```
## :rocket: Let's go
The flask app is available on [http://localhost:5000](http://localhost:5000), you can go to [/text](http://localhost:5000/text) endpoint to check the content of the file file.txt. Any changes in the content of this file will be shown by refreshing the web page.

You can also verify mounts : 
```
docker inspect <your_mongo_container_name>
```
