# SimpleFSDB

## Description

## Installation and use
To use this database you need to pass the commands by CMD so we made [SimpleDBDriver](https://github.com/YahyaAzzam/SimpleDBDriver) in jave you can use it to call the database 

## Commands
| Name | parameters | Description |
|------|------------|-------------|
| CreateCommand() | DatabaseSchemaPath | Create database which follow input [schema](https://github.com/YahyaAzzam/SimpleFSDB/edit/main/README.md##schema-sample) |
| SetCommand() | DatabaseName, TableName, Inputdata | Set row with the inputdata |
| GetCommand() | DatabaseName, TableName, InputQuery | Use the query to get specific data |
| DeleteCommand() |  DatabaseName, TableName, InputQuery | Use the query to delete specific data |
| ClearCommand() |  DatabaseName | retrun the database to the initial state |

## Schema

### schema sample:
  ```
  {
      "database_name" : "csed25",
      "Tables" : [
          {
              "name" : "Reservations",
              "columns" : ["ReservationId", "First_name", "Last_name", "Passport_Id", "Gender", "Age", "Flight_Id", "Luggage_allowance", "Seat"],
              "primary_key"  : "ReservationId",
              "index_keys" : ["First_name", "Last_name", "Seat"],
              "overwrite" : "False",
              "consistently" : "Eventual"
         }
                  ]
   }
  ```
