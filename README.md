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
    - [Schema formate](#schema)
    - [Command-Line Interface](#commands)
4. [Example Usage](#examples)
5. [FAQs](#faqs)
6. [Contributing](#contributing)
7. [License](#license)
8. [Upcoming Features](#upcoming-features)

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

- **Clearing Database**:
    - **clear the data**: Wipe the database clean, starting fresh for new data.
- **Java Integration**
  - **Cross-Language Compatibility**: Our meticulously crafted Java driver ([SimpleDBDriver](https://github.com/YahyaAzzam/SimpleDBDriver)) seamlessly integrates with the Simple File System Database, allowing Java applications to interact with the database effortlessly. This cross-language compatibility enhances the database's versatility, extending its usability to diverse programming ecosystems.

## 2. Installation <a name="installation"></a>
To use DataHive, follow these installation steps:
1. **Install python**: Python 3.x installed on your machine.

2. **Install DataHive**: Install DataHive package on your local machine:

```shell
pip install DataHive
```
## 3. Usage <a name="usage"></a>

### Schema Format <a name="schema"></a>
Below is an example of the schema format that defines the structure of the database, including the database name and tables with their respective attributes:
   1. **Schema Example**:
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
             }
                      ]
       }
      ```
2. **Table Contents**:
  The schema format consists of the following elements for defining tables within the database:

      | Name | Type | Nullable | Notes |
      | ---- | ---- | -------- | ----- |
      | Name | string | No | Name of the table. |
      | Columns | List of Strings | No | List of column names, including the primary key. |
      | Primary_key | String | No | The primary key for the table. |
      | Index_key | List of Strings | Yes | List of column names that serve as index keys. |
      | Overwrite | string | Yes | Initial value is 'False'; you can set its value to 'True' to enable overwriting.|
   
### Command-Line Interface <a name="commands"></a>

*Note: Ensure that you have a JSON file containing your schema before creating the database.*

| Command | Parameters | Description |
|---------|------------|-------------|
| `Create` | `DatabaseSchemaPath` | Creates a database following the specified [schema](#schema).
| `Set` | `DatabaseName`, `TableName`, `InputData` | Sets a row with the provided input data.
| `Get` | `DatabaseName`, `TableName`, `InputQuery` | Utilizes the input query to retrieve specific data from the database.
| `Delete` | `DatabaseName`, `TableName`, `InputQuery` | Uses the input query to delete specific data from the database.
| `Clear` | `DatabaseName` | Resets the specified database to its initial state.

This Command-Line Interface (CLI) provides a set of commands for creating, updating, querying, deleting data, and resetting databases, offering comprehensive control over your data management tasks.

## 4. Example Usage <a name="examples"></a>
- **The general format for any command in the program is as follows**:

   ```python
   python DataHive -c [command] [options]
   ```
   Replace `[command]` with the desired database command and `[options]` with relevant command options.

- **Commands Examples**:

    - Creating a new database:
         ```python
         python DataHive -c create -sc <your_schema_path>
         ```
    
    - Sets a row with the provided input data:
         ```python
         python DataHive -c set -db <your_database> -t <your_table> -q '{"key": "value"}'
         ```

    - Utilizes the input query to retrieve specific data from the database:
         ```python
         python DataHive -c get -db <your_database> -t <your_table> -q '{"key": "value"}'
                 # if you didn't add -q it will get all data in the table
         ```

    - Uses the input query to delete specific data from the database:
         ```python
         python DataHive -c delete -db <your_database> -t <your_table> -q '{"key": "value"}'
         ```

   - Resets the specified database to its initial state:
     ```python
     python DataHive -c clear -db <your_database>'
     ```
## 5. FAQs <a name="faqs"></a>

- **Q1: What is DataHive?**
  - **A1:** DataHive is a lightweight database system designed for storing data in JSON files. It provides essential CRUD (Create, Read, Update, Delete) operations and ensures synchronization between read and write operations. DataHive is an ideal solution for small-scale applications where a simple and reliable data storage system is required.

- **Q2: How do I install DataHive?**
  - **A2:** To install DataHive, you need to have Python 3.x installed on your machine. After ensuring Python is installed, run the following command:

    ```shell
    pip install DataHive
    ```

- **Q3: What is the schema format for defining the database structure?**
  - **A3:** The schema format defines the structure of the database, including the database name, tables, and their attributes. It consists of elements like table names, column names, primary keys, index keys, and overwriting settings. You can find a detailed example of the schema format in the [Schema Format](#schema) section of this README.

- **Q4: How do I use the Command-Line Interface (CLI) to interact with DataHive?**
  - **A4:** The CLI offers a set of commands for creating, updating, querying, deleting data, and resetting databases. You can use the general command format:

    ```shell
    python DataHive -c [command] [options]
    ```

    Replace `[command]` with the desired database command and `[options]` with relevant command options. Examples of various commands can be found in the [Example Usage](#examples) section.

- **Q5: Is DataHive compatible with Java?**
  - **A5:** Yes, DataHive is cross-language compatible. We have developed a dedicated Java driver (SimpleDBDriver) that seamlessly integrates with DataHive. This Java driver allows Java applications to interact with the database, extending its usability to diverse programming ecosystems.

## 6. Contributing <a name="contributing"></a>

Contributions to DataHive are welcome! Feel free to fork the repository, make improvements, and create pull requests.

## 7. License <a name="license"></a>

DataHive is released under the MIT License. See the [LICENSE](https://github.com/YahyaAzzam/SimpleFSDB/blob/master/LICENSE) file for details.

## 8. Upcoming Features <a name="upcoming-features">
   - Stay tuned for future updates and additional features. We are constantly working on enhancing DataHive to provide an even better data storage solution for your needs.
-----
*Note: This documentation provides an overview of DataHive's functionality and usage. For detailed code explanations, refer to the source code and comments in SimpleFSDB's repository.*


  


