Factorio Dependency Tree
========================

Resource and Tech Dependencies


Data
----

 - [data/recipes.csv](https://github.com/albertyw/factorio-dependency-tree/blob/master/data/recipes.csv)
   is a CSV file of all recipes.  The first column is the product; the later columns are required to produce the product.
 - [data/science_packs.csv](https://github.com/albertyw/factorio-dependency-tree/blob/master/data/science_packs.csv)
   is a CSV file for all recipes required to produce science packs.
 - [data/technology.csv](https://github.com/albertyw/factorio-dependency-tree/blob/master/data/technology.csv)
   is a CSV file of all technologies.  The first column is the technology to be researched; the later columns are prerequisite technology requirements.


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
