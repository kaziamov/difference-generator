#Makefile

gd-h:
	poetry run gendiff -h
gd-flat:
	poetry run gendiff tests/fixtures/flat_1.json tests/fixtures/flat_2.json
gd-tree:
	poetry run gendiff tests/fixtures/tree_1.json tests/fixtures/tree_2.yml


test-json:
	gendiff tests/fixtures/flat_1.json tests/fixtures/flat_2.json
test-yaml:
	gendiff ./tests/fixtures/flat_1.yaml ./tests/fixtures/flat_2.yaml
test-yml:
	gendiff tests/fixtures/flat_1.yml tests/fixtures/flat_2.json
example: test-json test-yaml test-yml



mtest:
	poetry run pytest --show-capture=stdout --disable-pytest-warnings -v --tb=no
vtest:
	clear && poetry run pytest -vv
lint:
	poetry run flake8 gendiff
check: mtest lint
push: check


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


