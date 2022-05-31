# enrichpipe 

[![build](https://github.com/lara-imrsv/enrichpipe/actions/workflows/build.yml/badge.svg)](https://github.com/lara-imrsv/enrichpipe/actions/workflows/build.yml)
[![Deploy](https://github.com/lara-imrsv/enrichpipe/actions/workflows/deploy.yml/badge.svg)](https://github.com/lara-imrsv/enrichpipe/actions/workflows/deploy.yml)
![](https://github.com/lara-imrsv/enrichpipe/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/lara-imrsv/enrichpipe/branch/main/graph/badge.svg?token=3KW44NKWAS)](https://codecov.io/gh/lara-imrsv/enrichpipe) [![Documentation Status](https://readthedocs.org/projects/enrichpipe/badge/?version=latest)](https://enrichpipe.readthedocs.io/en/latest/?badge=latest)

## Summary

enrichpipe is a python package designed to perform exploratory data analysis, to help with missing data imputation and to give baseline models. Also, it assists in feature selection which is a common problem when undertaking a data science or machine learning analysis. As its name indicates, this function operates like sklearn. It carries out tasks such as splitting data, feature selection, model fitting, numerical missing data imputation etc.

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ enrichpipe
```

## Features

This package introduces features used to enrich databases with query result curated data. All functions can be used on a dataset with text data. The functions might have their own required and optional arguments.

- alphabet check
- bleu score

## Dependencies


- python = "^3.8"
- pandas = "^1.2.3"
- numpy = "^1.20.1"
- matplotlib = "^3.3.4"
- sklearn = "^0.0"
- seaborn = "^0.11.1"
- ipython = "^7.21.0"    
- jupyter = "^1.0.0"


## Usage

| Task | Function  |
|------------|-----|
| Alphabet Check| `alphabet_check('Suspected English', lang='en')`|
| Compute Bleu Score| `bleu_score(references=['hi'], hypothesis='Happy world',weight=(0.7,0.3))`|


## Example

```Python

from enrichpipe import alphabet_check, bleu_score
TODO 

```

## Documentation

The official documentation is hosted on Read the Docs: https://enrichpipe.readthedocs.io/en/latest/

## Contributors

Development Team:

- Lara Habashy
- Wyatt Kyte


We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](). If you would like to contribute, please view our [contributing guidelines]() and get familiar with the [Github flow](https://blog.programster.org/git-workflows) workflow.

### Credits

This package was created with Cookiecutter project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
