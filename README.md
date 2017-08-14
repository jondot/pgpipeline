# Pgpipeline: automatic postgres pipeline for Scrapy

A Scrapy pipeline module to persist items to a postgres table automatically.


## Quick Start

Here's an example showing automatic item pipeline, with a custom `JSONB` field.

```python
# settings.py
from sqlalchemy.dialects.postgresql import JSONB

ITEM_PIPELINES = {
    'pgpipeline.PgPipeline': 300,
}

PG_PIPELINE = {
    'connection': 'postgresql://localhost:5432/scrapy_db',
    'table_name': 'demo_items',
    'pkey': 'item_id',
    'ignore_identical': ['item_id', 'job_id'],
    'types': {
        'some_data': JSONB
    },
    'onconflict': 'upsert'
}
```

All columns, tables, and indices are automatically created.

* `pkey`: a primary key for this item (other than database-generated `id`)
* `ignore_identical`: these are a set of fields by which we identify duplicates and skip insert.
* `types`: keys specified here will be using the type given, otherwise types are guessed.
* `onconflict`: upsert|ignore|non-null - `ignore` will skip inserting on conflict and `upsert` will update. `non-null` will upsert only values that are not `None` and thus avoid removing existing values.
## Developers

Set up a development environment
```
$ pip install -r requirements.txt
```

### Development

* Dependencies: list them in `requirements.txt`

### Release

* Dependencies: list them in `setup.py` under `install_requires`:

```python
install_requires=['peppercorn'],
```

Then:

```
$ make dist && make release
```

# Contributing

Fork, implement, add tests, pull request, get my everlasting thanks and a respectable place here :).


### Thanks:

To all [Contributors](https://github.com/jondot/pgpipeline/graphs/contributors) - you make this happen, thanks!


# Copyright

Copyright (c) 2017 [Dotan Nahum](http://gplus.to/dotan) [@jondot](http://twitter.com/jondot). See [LICENSE](LICENSE) for further details.
