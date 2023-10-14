

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