#Makefile

gendiff:
	poetry run gendiff
tests:
	poetry run pytest
lint:
	poetry run flake8 brain_games
install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl --force

