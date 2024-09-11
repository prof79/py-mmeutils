default:
    pyproject-build

test:
    py -m pytest -v

clean:
    rm -rf build/ dist/ **/*.egg-info/
