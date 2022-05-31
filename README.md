# enrichpipe 

[![build](https://github.com/lara-imrsv/enrichpipe/actions/workflows/build.yml/badge.svg)](https://github.com/lara-imrsv/enrichpipe/actions/workflows/build.yml)
[![Deploy](https://github.com/lara-imrsv/enrichpipe/actions/workflows/deploy.yml/badge.svg)](https://github.com/lara-imrsv/enrichpipe/actions/workflows/deploy.yml)
[![codecov](https://codecov.io/gh/lara-imrsv/enrichpipe/branch/main/graph/badge.svg?token=3KW44NKWAS)](https://codecov.io/gh/lara-imrsv/enrichpipe) 
[![Documentation Status](https://readthedocs.org/projects/enrichpipe/badge/?version=latest)](https://enrichpipe.readthedocs.io/en/latest/?badge=latest)

## Summary

enrichpipe is a python package designed to provide enrichments to text data using a variety of features. Tasks include quality checks for data validation and a variety of scoring functionalies for assessing text data. The functions support text data but will soon support audio data (Stay Tuned!) 

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ enrichpipe
```

## Features

This package introduces features used to enrich databases with curated data based on user query results. Note that the functions might have their own required and optional arguments.

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

For a complete list of dependencies, see [poetry.toml](https://github.com/lara-imrsv/enrichpipe/blob/main/poetry.lock)

## Usage

| Task | Function  |
|------------|-----|
| Alphabet Check| `alphabet_check('Suspected English', lang='en')`|
| Compute Bleu Score| `bleu_score(references=['hi'], hypothesis='Happy world', weight=(0.7, 0.3))`|


## Example

```Python

from enrichpipe import alphabet_check, bleu_score
TODO 

```

## Documentation

The official documentation is hosted on [Read the Docs](https://enrichpipe.readthedocs.io/en/latest/?badge=latest).
TODO Vignette - refer to usage.rst

## Contributors

Development Team:

- Lara Habashy
- Wyatt Kyte


We welcome and recognize all contributions. If you would like to contribute, please view our [contributing guidelines](https://github.com/lara-imrsv/enrichpipe/blob/main/CONTRIBUTING.rst) and get familiar with the [Github flow](https://blog.programster.org/git-workflows) workflow.

### Credits

This package was created with Cookiecutter project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
