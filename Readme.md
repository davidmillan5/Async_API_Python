

## Required Packages

- [FastAPI](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)


```
pip install fastapi uvicorn
```

Then you need to run 
```
pip freeze > requirements.txt
```

The command **pip freeze > requirements.txt** in Python is used to generate a list of all the currently installed Python packages and their versions and then save this list to a file named requirements.txt. This is a common practice in Python development to create a "requirements.txt" file that specifies the dependencies of a Python project.

Here's a breakdown of what each part of the command does:

**pip freeze**: This part of the command uses the pip tool, which is the package installer for Python, to list all the installed packages and their versions. The freeze subcommand outputs a list of package names and versions in the format package==version.

**>** : This is a redirection operator in the command line. It is used to take the output of the previous command (in this case, the list of installed packages and their versions) and redirect it to a file.

**requirements.txt**: This is the name of the file to which the output of pip freeze will be written. It's a common convention to name this file requirements.txt, but you can choose a different name if you prefer.

After running this command, you will have a file named requirements.txt in your current directory that contains a list of all the Python packages installed in your environment, along with their versions. This file is often used in conjunction with package management tools like pip and virtual environments to ensure that the same package versions are installed when you or someone else works on the project in the future. You can later use this file to recreate the same environment by running pip install -r requirements.txt.

In order to make the server run you have to define the file name that will work as an entry point
for uvicorn like this:

```
uvicorn main:app
```

You also will need to install [SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)

```
pip install sqlalchemy[asyncio]
```

SQLAlchemy is an open-source SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a set of high-level API for connecting to relational databases, such as MySQL, PostgreSQL, SQLite, and Oracle, and performing various database operations using Python code. SQLAlchemy allows developers to work with databases in a more Pythonic way, making it easier to interact with and manipulate database data.

Here are some key features of SQLAlchemy:

1. **ORM (Object-Relational Mapping)**: SQLAlchemy provides an ORM that allows you to define your database schema and data models using Python classes. These classes are mapped to database tables, and you can interact with the database using Python objects rather than writing raw SQL queries.

2. **SQL Expression Language**: SQLAlchemy also provides a SQL expression language, which allows you to construct and execute SQL queries using Python code. This is useful when you need to work with raw SQL in a more structured way.

3. **Connection Pooling**: SQLAlchemy includes built-in support for connection pooling, which helps manage and reuse database connections efficiently.

4. **Cross-Platform Compatibility**: SQLAlchemy supports various database backends, making it possible to write code that works with different databases without major changes.

5. **Transactions and Sessions**: SQLAlchemy provides tools for handling database transactions and sessions, making it easier to manage changes to the database.

6. **Query Building**: SQLAlchemy provides a powerful and flexible way to construct database queries, allowing you to build complex queries using Python code.

Overall, SQLAlchemy is a versatile and powerful library that is widely used in Python applications to interact with relational databases. It's commonly used in web development, data analysis, and other Python projects that require database access.


and the driver to connect to [postgresql asynchronously](https://magicstack.github.io/asyncpg/current/)

```
pip install asyncpg
```

This to run the app asynchronously in Python with [asyncio](https://docs.python.org/es/3/library/asyncio.html)

Also, you need to install [python-env](https://pypi.org/project/python-dotenv/)
in order to define your environment variables for the whole project.


...

The chronological steps are:

#1 main.py --
#2 db.py --
#3 models.py --
#4 create_db.py --

After building the create_db.py file you need to run the following command in the terminal 
to create the table into the database 

```
python create_db.py
```
