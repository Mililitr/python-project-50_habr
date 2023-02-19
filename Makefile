install:
	poetry install


publish:
	poetry publish --dry-run


build:
	poetry build


gendiff:
	poetry run gendiff


package-install:
	python3 -m pip install --force-reinstall dist/*.whl
