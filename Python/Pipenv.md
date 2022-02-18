# Setup (Mac)

We must install pyenv. On terminal:

```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"'
```

# Pipenv

Pipenv allows us to manage python and the packages for a project.

## To start

```
pip3 install pipenv
```

To create a new environment:

```
mkdir project-name

cd projet-name

pipenv install --python 3.7 # this can be any version you want as long as it exists!

# To activate the pipenv environment:
pipenv shell

# From now on, whenever installing pakages, just do "pipenv install _PACKAGE_=_VERSION_
```

## On existing project (with Pipfile)

```
# Installs all the correct python version as well as the packages

pipenv install

pipenv shell
```

## Jupyter Lab

Activating jupyter lab through pipenv shell allows us to run jupyter notebook through the pipenv environment. This means any packages installed pipenv are already preinstalled in the jupyter lab environment.