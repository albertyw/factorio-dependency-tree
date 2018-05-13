Factorio Dependency Tree
========================

Resource and Tech Dependencies


Getting raw data
----------------

From the factorio root directory:

 - raw/recipe/ is from data/base/prototypes/recipe
 - raw/technology.lua is from data/base/prototypes/technology/technology.lua

The `data.extend` and non-data functions need to be removed.

Setup
-----

```bash
mkvirtualenv --python=python3 factorio
pip install -r requirements.txt
python parse.py
```
