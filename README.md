# Swine Movement MS #

This project is a demo of a microservice implementation using Django REST apis, Postgresql, Kafka, Redis and Docker 
 ## Background ##
In food animal systems, animals move to different farms as they age. Each farm has a unique ID and must keep a record of the movement of animals from one farm to another. Here, we present some fictitious records of movements among pig farms.


## How do I get set up? ##
### System Prerequisite ###

2. System must have python 3.8 and pip installed (Recommended to use a python virtual environment)
1. System must have docker installed
3. System must have docker-compose installed
4. System must have enough RAM to run docker containers

### Local Setup Steps ###

1. Clone the repository
    ```shell
    git clone https://github.com/mithildani/swinemovement.git
    ```

2. Create and activate a new python environment. 
3. Set up environment for the first time
    ```shell
    make first_init
    ```
   For future setup just run
    ```shell
    make init
    ```
   
4. Run the server
    ```shell
    make runserver
    ```
5. Now go to localhost:9113/admin
