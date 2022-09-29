#Makefile

gd-h:
	poetry run gendiff -h
gd-s:
	poetry run gendiff tests/fixtures/flat_1.json tests/fixtures/flat_2.json


show-files:
	echo '\n------------------------- FILES FOR EXAMPLE ------------------------ ' && \
	echo '\n---------------------------- FIRST FILE ---------------------------- ' && \
	cat tests/fixtures/flat_1.json && \
	echo '\n---------------------------- SECOND FILE --------------------------- ' && \
	cat tests/fixtures/flat_2.json && \
	echo '\n---------------------- GENERATE DIFFERENCES  -----------------------'
test-json:
	gendiff tests/fixtures/flat_1.json tests/fixtures/flat_2.json
test-yaml:
	gendiff ./tests/fixtures/flat_1.yaml ./tests/fixtures/flat_2.yaml
test-yml:
	gendiff tests/fixtures/flat_1.yml tests/fixtures/flat_2.json
example: show-files test-json test-yaml test-yml




mtest:
	poetry run pytest -vv
lint:
	poetry run flake8 gendiff
check: mtest lint


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


