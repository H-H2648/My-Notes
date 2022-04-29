 Note -d refers to dev packages (we don't need this when we run the code in production)

```
pipenv install -d black==21.5b1
```

```
pipenv install -d pylint==2.8.2
```

Allows us to format code

* `pipenv run python -m black .` will automatically format all python codes
* `pipenv run python -m black --check .` will tell us which python files require formatting changes
* `pipenv run python -m black --check --diff FILE` will tell us what part of the file (`FILE`) requires formatting chagnes
  * Sometimes, hard to tell what needs to change (like there is a space at the end of the line)
* `pipenv run pylint -E *.py` gives us our "score" for our formatting of the codes