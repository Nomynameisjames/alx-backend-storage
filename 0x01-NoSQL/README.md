				What is NoSQL?
NoSQL stands for "Not Only SQL," This refers to a type of database management system that is different from traditional, SQL-based systems.
NoSQL databases are designed to handle large volumes of unstructured or semi-structured data, such as text, documents, and media files.

				SQL vs. NoSQL
The main difference between SQL and NoSQL databases is in their structure and data modeling.
SQL databases are based on a structured query language that uses tables with rows and columns to store data.
NoSQL databases, on the other hand, use different models, such as document, key-value, or graph.

				ACID
ACID stands for Atomicity, Consistency, Isolation, and Durability, and it is a set of properties that guarantee the reliability of database transactions.
SQL databases are typically ACID compliant, which means that they ensure that each transaction is executed reliably and without errors.

				Document Storage
In a document storage model, data is stored in a document format, such as JSON or XML. Each document can have its own structure and can be nested,
making it a flexible and scalable model for handling unstructured or semi-structured data.

				NoSQL Types
There are different types of NoSQL databases, including document-based, key-value, column-family, and graph databases.
Each type has its own strengths and weaknesses, and they are suited for different use cases.

				Benefits of a NoSQL database
NoSQL databases are designed to handle large volumes of unstructured or semi-structured data,
making them suitable for applications that require scalability and flexibility.
They can also be used for real-time analytics, as they can handle data in real-time and provide insights immediately.

				Querying information from a NoSQL database
To query information from a NoSQL database, you use the database's query language, which can vary depending on the type of database.
For example, MongoDB uses a query language called the MongoDB Query Language (MQL), while Cassandra uses CQL (Cassandra Query Language).

				Inserting/updating/deleting information from a NoSQL database
To insert, update, or delete information from a NoSQL database, you use the database's API or client libraries.
Each database has its own API, which can be used to interact with the database and perform CRUD (Create, Read, Update, Delete) operations.

				Using MongoDB
MongoDB is a popular document-based NoSQL database that is designed to handle large volumes of unstructured data.
To use MongoDB, you need to install it on your system and then use the MongoDB shell or one of the client libraries such as PyMongo or MongoDBEngine
to interact with the database. MongoDB supports a flexible data model and provides powerful querying and indexing capabilities.

				Installation

```$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$  sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
$  
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1' ```
