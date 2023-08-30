# shiny

# Requirements

- ### Install poetry - [Link](https://python-poetry.org/docs/#installation)

- ### Install Docker Windows - [Link](https://docs.docker.com/desktop/install/windows-install/)

- ### Install pyenv (Optional)
```shell
# Install pyenv
python3 -m pip install pyenv
# Install python 3.10
pyenv install 3.10
```

- ### Install project dependencies
```shell
# Set currenty python as 3.10
pyenv shell 3.10
# Set poetry env with python 3.10
poetry env use $(pyenv which python)
# Install pip dependencies + create venv
poetry install
```

