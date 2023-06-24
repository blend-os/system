import importlib
import pathlib
import re

modules = {}

### START: https://stackoverflow.com/a/75487598
path = pathlib.Path(__file__).parent.absolute()
names = [x.name[:-3] for x in path.iterdir() if x.is_file() and re.search("^[a-z]*\.py$", x.name)]
for name in names:
    modules[name] = importlib.import_module(f".{name}", __name__)
### END