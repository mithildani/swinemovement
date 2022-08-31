# Swine Movement MS #
This project is a demo of a microservice implementation using Django REST apis, Postgres, Redis and Docker

## Background ##
In food animal systems, animals move to different farms as they age. Each farm has a unique ID and must keep a record of the movement of animals from one farm to another. Here, we present some fictitious records of movements among pig farms.

## Demo ##
https://user-images.githubusercontent.com/24509876/187802283-e2a1da1f-9ea8-485a-b323-94c4ea4b742a.mp4

## Architecture and Design ##
Checkout technical details about the service [here](./app/README.md)

## How do I run this service? (Prod setup) ##
### System Prerequisite ###
1. System must have git, docker, docker-compose installed 
2. System must have enough RAM to run docker containers

### Steps to run service ### 
1. Clone the repository
   ```shell
   git clone https://github.com/mithildani/swinemovement.git
   ```
2. Build docker image for microservice
   ```shell
   make buildapp
   ```
3. Start running application
   ```shell
   make startapp 
   ```

If you are running this setup for the first time continue steps 4 to steps 6 <br />

4. Run migrations
   ```shell
   make migrate
   ```

5. Load Dummy Data
   ```shell
   make loaddata
   ```

6. Create Admin User
   ```shell
   make admin
   ```

7. Sign in and start using the application on [localhost:9113/admin](localhost:9113/admin)
8. Visit [localhost:9113/admin/population/](localhost:9113/admin/population/) for population data
9. Stop the application
   ```shell
   make stopapp
   ```


## How do I start dev? (Dev Setup) ##
### System Prerequisite ###
1. System must have python 3.8 and pip installed (Recommended to use a python virtual environment)
2. System must have git, docker, docker-compose installed 
3. System must have enough RAM to run docker containers

### Steps to setup dev service ###

1. Clone the repository
    ```shell
    git clone https://github.com/mithildani/swinemovement.git
    ```

2. Create and activate a new python environment. 
3. Set up environment for the first time
    ```shell
    make dev_first_init
    ```
   For future setup just run
    ```shell
    make dev_init
    ```
   
4. Run the server
    ```shell
    make dev_runserver
    ```
5. Sign in and start using the application on [localhost:9113/admin](localhost:9113/admin)
6. Visit [localhost:9113/admin/population/](localhost:9113/admin/population/) for population data
