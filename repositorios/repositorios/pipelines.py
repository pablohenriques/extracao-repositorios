import pymongo


class RepositoriosPipeline:
    def __init__(self, mongodb_server, mongodb_port, mongodb_db, mongodb_collection):
        self.mongodb_server = mongodb_server
        self.mongodb_port = mongodb_port
        self.mongodb_db = mongodb_db
        self.mongodb_collection = mongodb_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_server=crawler.settings.get('MONGODB_SERVER'),
            mongodb_port=crawler.settings.get('MONGODB_PORT'),
            mongodb_db=crawler.settings.get('MONGODB_DB'),
            mongodb_collection=crawler.settings.get('MONGODB_COLLECTION')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongodb_server, self.mongodb_port)
        self.db = self.client[self.mongodb_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.mongodb_collection].insert_one(dict(item))
        return item
