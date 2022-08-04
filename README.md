# api testing project for book store.

## please install requirements file
## ****************************************
## run options:
### to run with default url and all tests 
```commandline
pytest ./test_petshop.py 
```
### to run with your own url if you run locally server
```commandline
pytest --url https://bookstore.toolsqa.com/ .\test_book_store.py
```


## run with allure report (u can use --url before .\test_book_store.py)
```commandline
 pytest --alluredir=reports\ .\test_book_store.py

```
## to see reports use
```commandline
allure serve reports/
```