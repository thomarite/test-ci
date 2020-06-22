# CI + Python best practice tools

Goals:

- 1 Testing CI with Travis
- 2 Adding python testing and best practices with pylama, black and tox.

Some details:

- pylama --> config file is setup.cfg
- black --> config file is pyproject.toml
- tox --> config file is tox.ini
- travis --> config file is .travis.yml

At the end of the day, you can make travis to call tox. And tox manage all tests for pylama and black.

Need to get used to create the virtual env inside its own folder, then it is easy to ignore for pylama/black etc.

```
pyenv local 3.7.3
python -m venv venv
source venv/bin/activate
```
