import pymongo
from pymongo.collection import Collection
from pymongo.database import Database
import time
import ssl


if __name__ == '__main__':
    print(ssl.get_default_verify_paths())
    conn: pymongo.MongoClient = pymongo.MongoClient("mongodb+srv://ellisjoe:<password>@cluster01.mfx5h.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE", 27017)
    author: Collection = conn['database01']['author']

#    start: float = time.time()
#    author.insert_many([{'number': num} for num in range(10)])
#    end: float = time.time()
#    print(f'took {end - start} seconds...')

    # author.delete_many({'number': {'$gt': 5}})
    for res in author.find():
        print(res)
    
    conn.close()