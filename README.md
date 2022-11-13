# Vintage e-Commerce Shop API

## Identification of the problem you are trying to solve by building this particular app.

This API is designed to handle the essential functions of a simple e-Commerece web app. The API controls the communication between consumers and the store allowing consumers to filter, sort and browse the list of products that are available as per stock levels. The Managers, Admins or Stockhands have full CRUD control and able able to update, modify, delete or create new products, add additional staff users.

## Why is it a problem that needs solving?

This application will be across a global market to reduce the amount of clothing waste that is produced every year, giving discarded products a second chance. The market for recycled, reusable, upcycled products is growing year over year largly by the young consumers. This application allows consumers in Australia and around the world to have another access point to browse, shop and purhcase these second-hand goods.

## Why have you chosen this database system. What are the drawbacks compared to others?

This system uses PostgresSQL as the main RDMBS which is very similar syntaxly to other DBMS's like Microsoft SQL Server and MYSQL which allow develoeprs to use different programs and languages to create RESTful APIs.
Additionally, PostgresSQL is also available open source allowing a variety of different developers such as myself to use for free regardless of the usuage of the software whether it be for personal or commerical. PostgresSQL is highly adaptable to the different OS systems people use around the world making it very seemless to use. 

However, while there are many advantages to using PostgresSQL, other RDMBS like MYSQL are much quicker for loading large amounts of data - however, due to the early development of this particular application the diffence between PostgresSQL and MYSQL would be unnoticable; whereas, on a larger scale such as Amazon, MYSQL would be far faster to retrive, update, delete, and add to the database. 

## Identify and discuss the key functionalities and benefits of an ORM

SQLAlchemy provides the key functionalities as an ORM. The implementation of SQLAlchemy allows for developers to have an array of libraries to access allowing the manipulation and interaction witht he database through the application to the basically seemless. The core of SQLAlchemy allows developers to create user-friendly methods for accessing the database while sanitising and maintaining a modern level of security for the information stored within. Addititional packages such as JWT can be directly imported and used in conjunction with SQLAlchemy and other packages that improve the security as well as the funcationality of the database and the codebase. This allows the developer to create clean, DRY code that is interactable and interrelateable dependent on the data that is stored. 

## Document all endpoints for your API

## An ERD for your app

![alt](https://github.com/JanzenCode/JordynSmall_T2A2-1/blob/main/docs/ERD%20Diagram%20(1).png)

## Detail any third party services that your app will use

At the moment the application does not implement any third party services to operate. In later development verisons, third-party services may be implemented to fulfill orders that are placed on the client-side. 

## Describe your projects models in terms of the relationships they have with each other

### User
- The user model contains the primary data that is used across the database;
    - A generated ID (PK)
    - email/password for authentication and authorisation
    - is_admin to confirm the permissions of this user (CRUD Authority)
    - as well as other data that is sensitive to the user (shown in the ERD)
- The User model is interrelated to the remainder of the database:
    - Address
    - Orders
        - Products (when creating an order request)
### Address
- The address model contains information about a users location and is directly related to the user model via user_id(FK)
    - containing sensitive information about the users location, this table is used to create a layer of security. Access is only granted by the authorised user/admin JWT Tokens
- The address is used in assosication to the user_id when an order is requested to compile the necessary information for the order request.
### Products
- The products model contains the data pertaining to the available products.
    - Users/CRUD Authority are able to filter the products by their brand, style, size, etc.
- The product_id is used to uniquely identify the product that is ordered when an order is requested by a user or when tested by CRUD Authority.
### Orders
- The orders models sets up the essential data required for an order to be executed but not fulfilled. As there are no implemented payment processors (third party), users can only select their desired product to craft a draft order that remains in the cart without fulfilment. 
- The order models utilises information from the user and address and products via requesting the relevant id parameters and compiling them.

## Discuss the database relations to be implemented in your application

Relationsip 1: The User Model is classified as a "one-to-many relationship" to the Order Model. This means that the multiple orders with different products. But only one Order can have one User this is because the order model contains a user_id (FK) linked both models together.

Relationship 2: The Address Model is classified as a "one-to-one relationship" to the User Model. This is because of the user_id(FK) that links the address to that specific user, for example:
- if the user has an user_id of "1" then,
- the address contents that also has a user_id of "1" will be directly associated with that user.
This means that the address with the specified user_id will only link to that user. Creating a one-to-one relationship between the User Model and the Address Model, the user in this API cannot have multiple addresses at the moment and will have update their address if the user changes their address.

## Describe the way tasks are allocated and tracked in your project

Trello an Online Management Software System was used to manage the projects development. In trello I created a board that broke down the requirements of each module of the product from: 
- models,
- controllers,
- commands,
- env/requirements,
- ERD Diagram;
- and any additional information or final udpates

The modular tasks allow for sectioned completion of each module and then are tracked by the progress and debugging of each controllers functions related to the model and/or other task. 

[Trello Project Management](https://trello.com/invite/b/fI6qSSzC/ATTI302946e3bbe390b68f620b98324ea095D89C4694/t2a2-project-management)


### Insturctions for Database Step up:
```
psql -U Postgres 
```
```
CREATE DATABASE vintageapi;
```
```
CREATE USER vintagedev WITH PASSWORD '123';
```
```
GRANT ALL PRIVILEGES ON DATABASE vintageapi TO vintagedev;
```
```
\q
```
### Creating the Venv & Activation
``` 
python3 -m venv .venv
```
```
source .venv/bin/activate
```
### Flask CLI Commands Shortcut:
```
flask db drop && flask db create && flask db seed
```
```
flask db drop
```
```
flask db create && flask db seed
```

### API Py-Package Requirements:

[API Requirements](https://github.com/JanzenCode/JordynSmall_T2A2-1/blob/main/requirements.txt)


