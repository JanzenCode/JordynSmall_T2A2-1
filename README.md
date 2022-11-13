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

## Detail any third party services that your app will use

## Describe your projects models in terms of the relationships they have with each other

## Discuss the database relations to be implemented in your application

## Describe the way tasks are allocated and tracked in your project

Insturctions for Database Step up:

```
CREATE DATABASE vintageapi;
```
```
CREATE USER vintagedev WITH PASSWORD '123';
```
```
GRANT ALL PRIVILEGES ON DATABASE vintageapi TO vintagedev;
```
