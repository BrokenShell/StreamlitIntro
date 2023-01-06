from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    load_dotenv()
    db = MongoClient(
        getenv("DB_URL"),
        tlsCAFile=where(),
    )["Database"]["Collection"]

    def seed(self, amount):
        self.db.insert_many(Monster().to_dict() for _ in range(amount))

    def reset(self):
        self.db.delete_many({})

    def count(self):
        return self.db.count_documents({})

    def dataframe(self):
        return DataFrame(self.db.find({}, {"_id": False, "Timestamp": False}))

    def html_table(self):
        return self.dataframe().to_html() if self.count() else None


# if __name__ == '__main__':
#     db = Database()
#     db.reset()
#     db.seed(2048)
