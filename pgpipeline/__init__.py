import logging
import dataset
from sqlalchemy.dialects.postgresql import JSONB
logger = logging.getLogger(__name__)


class PgPipeline(object):
    def __init__(self, **kwargs):
        self.args = kwargs

    @classmethod
    def from_crawler(cls, crawler):
        args = crawler.settings.get('PG_PIPELINE', {})
        return cls(**args)

    def open_spider(self, spider):
        if self.args.get('connection'):
            self.db = dataset.connect(self.args.get('connection'))
            self.table = self.db[self.args.get('table_name')]
            self.pkey = self.args.get('pkey')
            self.types = self.args.get('types', {})
            self.ignore_identical = self.args.get('ignore_identical')
            self.table.create_index([self.pkey])
            self.table.create_index(self.ignore_identical)
            self.onconflict = self.args.get('onconflict', 'ignore')

            self.enabled = True

    def process_item(self, item, spider):
        if self.enabled:
            if self.onconflict == 'ignore':
                logger.debug("SAVE(ignore) %s", item)
                self.table.insert_ignore(
                    item, self.ignore_identical, types=self.types)
            elif self.onconflict == 'upsert':
                logger.debug("SAVE(upsert) %s", item)
                self.table.upsert(
                    item, self.ignore_identical, types=self.types)
            elif self.onconflict == 'non-null':
                logger.debug("SAVE(non-null) %s", item)
                row, res = self.table._upsert_pre_check(
                    item, self.ignore_identical, None)
                selected = item
                if res is not None:
                    # remove keys with none value
                    selected = dict((k, v) for k, v in item.iteritems() if v)

                self.table.upsert(
                    selected, self.ignore_identical, types=self.types)
            else:
                raise Exception("no such strategy: %s" % (self.onconflict))

        else:
            logger.debug("DISABLED")
        return item
