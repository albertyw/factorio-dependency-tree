Factorio Dependency Tree
========================

Resource and Tech Dependencies


Getting raw data
----------------

From the factorio root directory:

 - raw/recipe/ is from data/base/prototypes/recipe
 - raw/technology.lua is from data/base/prototypes/technology/technology.lua

Setup
-----

```bash
mkvirtualenv --python=python3 factorio
pip install -r requirements.txt
python parse.py
```
