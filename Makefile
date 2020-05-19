setup:
	pipenv install

test:
	pipenv run bash -c "cd public; flask run;"
