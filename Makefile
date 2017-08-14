init:
	pip install -r requirements.txt
install:
	pip install -e .
test:
	nosetests tests
dist:
	rm -rf dist
	python setup.py sdist bdist_wheel
release:
	twine upload dist/*
.PHONY: init install test dist
