# django-with-poetry-template

## How to set Poetry.

1. [Install poetry](https://python-poetry.org/docs/#installation) and configure your bash shell.
2. Set poetry env by python version you want.
3. Enter poetry virtual env.
4. Install package. command example

```shell
poetry add pendulum
```

This is how to fix the version of packages.

```shell
poetry add pendulum@^2.0.5
poetry add "pendulum>=2.0.5"
```

## How to set Django.

### Models

1. It is recommended to [substitute user model](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model).
2. If you relocate model files into `models` directory, create `__init__.py` under the `models` directory and write the import statement of each model file.

### Settings.py

1. Do not forget to add app name to `INSTALLED_APPS`.
2. If you substitute user model, add `AUTH_USER_MODEL` properly.
