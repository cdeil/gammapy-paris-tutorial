# gammapy-paris-tutorial

Tutorial repo for Gammapy Paris workshop, Feb 2017

What should we do?

## Brief overview for Gammapy repo 

* Overview of code, tests, docs in Gammapy
    * Use PointingInfo class as an example

## How to hack on Gammapy

* In Gammapy, everything works the same as in Astropy.
  We don't have a lot of written docs for contributors,
  but they have a ton: http://astropy.readthedocs.io/en/latest/
* Know which version of Gammapy are you running.
    * `python setup.py build`
    * `python setup.py install`
    * `pip install .`
    * `python setup.py build_ext --inplace`
    * `python setup.py develop`
    * `pip install --editable .`
* Run tests:
    * `python setup.py test`
    * `python -m pytest`
* Build docs locally:
    * `python setup.py build_docs`
    * `open docs/_build/html/index.html`
* Look at one pull request, travis-ci

## Exercises

### Coding

* Python coding exercise & testing with pytest.org
* Test-driven development -- let's write a `Point` class

### Make a pull request

* Working with git locally
    * `git clone`
    * `git pull`
    * `git status`
    * `git branch`
    * `git checkout`
    * `git commit`
* Forking a repo, making a pull request
    * Make a branch
    * Make a commit
    * Fork via Github website
    * `git remote -v`
    * `git push`
    * Make pull request via Github website
