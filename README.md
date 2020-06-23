[![Build Status](https://travis-ci.org/thomarite/test-ci.svg?branch=master)](https://travis-ci.org/thomarite/test-ci)

# CI + Python best practice tools

# Goals

- 1 Testing CI with Travis
- 2 Adding python testing and best practices with pylama, black, pytest and tox.

# Some details

- pylama --> config file is setup.cfg
- black --> config file is pyproject.toml
- tox --> config file is tox.ini
- travis --> config file is .travis.yml
- tools folder --> python script to validate yaml files to call from tox
- pytest and tests folder --> tests and conftest.py for managing pytest

At the end of the day, you can make travis to call tox. And tox manage all tests for pylama, black and pytest.

Need to get used to create the virtual env inside its own folder, then it is easy to ignore for pylama/black etc.

```
pyenv local 3.7.3
python -m venv virt_env
source virt_env/bin/activate
```

# Pytest

How to run pytest (if you have the VMs ready)

```
$ py.test -s -v tests/
Type password for api user in Arista: 
=================================================== test session starts ====================================================
platform linux -- Python 3.7.3, pytest-5.4.1, py-1.8.1, pluggy-0.13.1 -- /home/tomas/.pyenv/versions/3.7.3/bin/python3
cachedir: .pytest_cache
metadata: {'Python': '3.7.3', 'Platform': 'Linux-5.6.0-2-amd64-x86_64-with-debian-bullseye-sid', 'Packages': {'pytest': '5.4.1', 'py': '1.8.1', 'pluggy': '0.13.1'}, 'Plugins': {'html': '2.1.1', 'metadata': '1.8.0'}, 'JAVA_HOME': '/opt/java/64/jre1.8.0_221/'}
rootdir: /home/tomas/storage/technology/ci-cd-jenkins/test-ci-travis
plugins: html-2.1.1, metadata-1.8.0
collected 8 items                                                                                                          

tests/test_eos.py::test_ssh PASSED
tests/test_eos.py::test_json PASSED
tests/test_eos.py::test_eapi PASSED
tests/test_sample.py::test_answer PASSED
tests/test_sample.py::test_answer2 PASSED
tests/test_sample.py::test_answer3 PASSED
tests/test_sample2.py::test_answer PASSED
tests/test_sample2.py::test_answer2 PASSED
tests/test_sample2.py::test_answer3 PASSED
```

# Tox

Somehow if you add a new library to the requirements-dev file, it is not installed when running tox, so you need to remove .tox folder and then when running tox again, it will reinstall all libraries.

# Json

A bit painful for python3. Had to install "jsonrpclib-pelix" and disable ssl verification. All this just for "test_json" in Arista.
