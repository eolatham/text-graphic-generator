setup:
	pdm install

test:
	pdm run bash -c "cd public; flask run;"
