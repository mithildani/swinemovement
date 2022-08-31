## DB Schema ##
![ER Diagram](https://github.com/mithildani/swinemovement/blob/main/app/swinemovement/models/ERDiagram.png?raw=true)

<br />

### Company ###
Stores meta data of all companies involved in movement of animals

### Species ###
Stores meta data of all species of animals for which movement is recorded

### Premise ###
Stores meta data of all farms. Every animal movement in/out of a premise is linked to the Movement table.

### Movement ###
Every animal movement in/out of a premise is recorded in this table. It links to the company and which species is moved.

### Population ###
Since this is an aggregate value it is not stored in the database. 
The difference of origin and destination movement of a premise gives the current population at the premise.
This calculated value is stored in cache for each premise for faster retreival.
