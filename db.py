from pymongo import MongoClient
from os import walk, getenv
from dotenv import load_dotenv
import json
import re 
ENV = load_dotenv('.env')

class MongoGo(object):
	def __init__(self):
		self.client = MongoClient(getenv("MONGODB_URI"))
		self.db = self.client['Taigi']

	def insert(self, object, colname):
		col = self.db[f'{colname}']
		col.insert_many(object)

	def getAllCollections(self):
		return self.db.list_collection_names()

	def find(self, keyword, blur=True):
		all_result = []
		if blur:
			p = re.compile(keyword, re.IGNORECASE)
		else:
			p = keyword

		for colname in self.getAllCollections():
			col = self.db[f'{colname}']
			results = col.find({'poj_input': p})
			
			for result in results:
				result.pop('_id')
				result['f'] = colname
				all_result.append(result)

		return all_result

def loadJson(jsonpath):
	with open(jsonpath, encoding="utf-8-sig") as f:
		datas = json.load(f)

	return datas

# def init():
# 	client = MongoGo()
# 	for (_, _, filename) in walk('./ctdb/json'):
# 		for fname in filename:
# 			name = fname.split('_')[-1].split('.')[0]
# 			fromjson = loadJson(f'./ctdb/json/{fname}')
# 			client.insert(fromjson, name)

def main():
	client = MongoGo()
	client.findone('khau','iTaigiHoataiTuichiautian', False)
