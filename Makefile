#Makefile

gendiff-flat:
	gendiff tests/fixtures/flat/flat_1.yaml tests/fixtures/flat/flat_2.json
gendiff-tree:
	gendiff ./tests/fixtures/tree/tree_1.yml ./tests/fixtures/tree/tree_2.json
example: gendiff-flat gendiff-tree


gendiff-help:
	poetry run gendiff -h

mtest:
	poetry run pytest --show-capture=stdout --disable-pytest-warnings -v --tb=no
vtest:
	poetry run pytest -vv
lint:
	poetry run flake8 gendiff
check: mtest lint
push: check
	git push


install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl --force
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
