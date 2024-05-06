### Installation
    https://realpython.com/dependency-management-python-poetry/#install-poetry-on-your-computer

### Check version
    Poetry --version

### Create project with poetry 
    Poetry new ProjectName
### Go to that project and run any command with poetry
    Poetry run python --version

.toml file actually manage package.

### To add any of the dependency in the .toml file
    Poetry add library-name
    E.g:
### Poetry add pytest
    
### To run Poetry test
    In the test folder add test file. Name of the file as well as of function should start with "test_".

### Install Fast Api & Uvicorn
    Poetry add fastapi "uvicorn[standard]"

### Running app and uvicorn server
    poetry run uvicorn firstpoetryproject.main:app --reload
    
### Running Pytest:
    Poetry run pytest -v

