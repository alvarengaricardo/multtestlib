cls
py -m pip install --upgrade pip
pause
py -m pip install --upgrade build
pause
py -m build
pause
py -m pip install --upgrade twine
pause
twine upload dist/*
pause
