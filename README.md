# SimpleFSDB

## Description

## Installation and use
To use this database you need to pass the commands by CMD so we made [SimpleDBDriver](https://github.com/YahyaAzzam/SimpleDBDriver) in jave you can use it to call the database 

## Commands
| Name | parameters | Description |
|------|------------|-------------|
| CreateCommand() | DatabaseSchemaPath | Create database which follow input [schema](#schema-sample) |
| SetCommand() | DatabaseName, TableName, Inputdata | Set row with the inputdata |
| GetCommand() | DatabaseName, TableName, InputQuery | Use the query to get specific data |
| DeleteCommand() |  DatabaseName, TableName, InputQuery | Use the query to delete specific data |
| ClearCommand() |  DatabaseName | retrun the database to the initial state |

## Schema

1. ### Schema sample:
  ```
  {
      "database_name" : "ClassA1",
      "Tables" : [
          {
              "name" : "student",
              "columns" : ["First_name", "Last_name", "CGPA", "Gender", "Age"],
              "primary_key"  : "Last_name",
              "index_keys" : ["First_name", "Last_name", "CGPA"],
              "overwrite" : "True",
              "consistently" : "Eventual"
         }
                  ]
   }
  ```
  
2. ### Table Contents:

  | Name | Type | Nullable | Notes |
  | ---- | ---- | -------- | ----- |
  | Name | string | No | |
  | Columns | List of Strings | No | should contain the primary-key |
  | Primary_key | String | No | |
  | Index_key | List of Strings | No | |
  | Overwrite | String | No | should be True or False only |
  | Consistently | String | NO | |
  


