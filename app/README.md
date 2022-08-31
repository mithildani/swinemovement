# Architecture and Design #

## Components ##
### Django ###
Django is used as the fullstack webserver for this application
### Django Admin and REST API ###
The Django Admin panel is used for CRUD operations and viewing the data. 
Example, a GET request provides the population data of each premise in the database. 
This can be extended to expose Django APIs for a different Typescript or any Frontend stack in the future.
### Postgres ###
Movement data is stored in Postgres. Refer [here](./swinemovement/models/README.md) for DB schema.
### Redis ###
A Redis caching layer is added between API and DB as per usecase. For example, fetching total population.
### Docker ###
Official Postgres and Redis docker images are used for deployment.
A custom docker image is built for the service deployment.
