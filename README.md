# api testing project for pet store.

## please install requirements file
## ****************************************
## run options:
### to run with default url and all tests 
```commandline
pytest ./test_petshop.py 
```
### to run with your own url if you run locally server
```commandline
pytest --url "localhost8080..." ./test_petshop.py
```
### to run only pet(mark) tests 
```commandline
pytest -m "pet" ./test_petshop.py  
```
### to run only user(mark) tests 
```commandline
pytest -m "user" ./test_petshop.py  
```
### to run only store(mark) tests 
```commandline
pytest -m "store" ./test_petshop.py 
```
## run with allure report (u can use --url before ./test_petstore.py)
```commandline
 pytest --alluredir=reports\ .\test_petshop.py

```
## to see reports use
```commandline
allure serve reports/
```