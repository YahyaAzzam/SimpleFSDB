# Simple file system database (DataHive)
[![PyPI](https://img.shields.io/pypi/v/DataHive.svg)](https://pypi.python.org/pypi/DataHive)
[![Downloads](https://pepy.tech/badge/DataHive)](https://pepy.tech/project/DataHive)
[![PyPI](https://img.shields.io/pypi/l/DataHive.svg)](https://github.com/YahyaAzzam/SimpleFSDB/blob/master/LICENSE)

## Overview
DataHive is a meticulously crafted, lightweight database system tailored for the purpose of data storage in JSON files. With a strong emphasis on simplicity and reliability, it offers essential CRUD (Create, Read, Update, Delete) operations and guarantees seamless synchronization between read and write operations. This project has been thoughtfully designed to serve as an elegant and file-based data storage solution, ideally suited for small-scale applications.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
    - [Initialization](#initialization)
    - [Scraping](#scraping)
4. [Command-Line Interface](#command-line-interface)
5. [Scraper Configuration](#scraper-configuration)
6. [Customization](#customization)
7. [Data Storage](#data-storage)
8. [FAQs](#faqs)
9. [Contributing](#contributing)
10. [License](#license)
11. [Upcoming Features](#upcoming-features)

## 1. Features <a name="features"></a>
- **Data Storage Excellence**
  - **Robust Storage**: Securely store data in JSON format.
  - **Flexibility**: JSON supports diverse data types and complex structures.
  - **Transparency**: Human-readable format simplifies debugging.
  - **Compatibility**: Platform-independent for use in various applications.

- **CRUD Functionality**
  - **Create (C)**: Add new data with specified identifiers.
  - **Read (R)**: Retrieve and query data for targeted searches.
  - **Update (U)**: Modify existing data, ensuring accuracy.
  - **Delete (D)**: Remove data to maintain a clean database.

- **Synchronization Assurance**
  - **ead-Write Consistency**: Guarantee synchronization between read and write operations for up-to-date data.
  - **Data Integrity**: Maintain reliable and trustworthy data, preventing inconsistencies.

- **Clearing Database**: Wipe the database clean, starting fresh for new data.
- **Java Integration**
  - **Cross-Language Compatibility**: Our meticulously crafted Java driver ([SimpleDBDriver](https://github.com/YahyaAzzam/SimpleDBDriver)) seamlessly integrates with the Simple File System Database, allowing Java applications to interact with the database effortlessly. This cross-language compatibility enhances the database's versatility, extending its usability to diverse programming ecosystems.

## 2. Installation <a name="installation"></a>
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
  | Consistently | String | No | |
  


