from os import walk
from ganbun import input
import json
jsonpath = './ctdb/json'
# const HOA = item.hoabun ?? item.english 
# const HANLO = item.hanlo_taibun_poj ?? item.hanlo_taibun ?? item.hanji_taibun
# const KAISOEH = item.hanlo_taibun_kaisoeh_poj ?? item.descriptions_poj
# const GANBUN = item.ganbun
# const URL = item.url
for (_, _, filename) in walk(jsonpath):
	for fname in filename:
		fromjson = []
		with open(jsonpath+"/"+fname, 'r', encoding='utf-8-sig') as jsonf:
			fromjson = json.load(jsonf)

		for i in fromjson:
			if 'hanlo_taibun' in i:
				i['hanlo_ganbun'] = input(i['hanlo_taibun'])[0]
			elif 'hanlo_taibun_poj' in i:
				i['hanlo_ganbun'] = input(i['hanlo_taibun_poj'])[0]
			elif 'hanji_taibun' in i:
				i['hanlo_ganbun'] = input(i['hanji_taibun'])[0]

			if 'hanlo_taibun_kaisoeh_poj' in i:
				i['kaisoeh_ganbun'] = input(i['hanlo_taibun_kaisoeh_poj'])[0]
			elif 'descriptions_poj' in i:
				i['kaisoeh_ganbun'] = input(i['descriptions_poj'])[0]


			poj = i['poj_input'].split('/')
			rep = []
			for p in poj:
				rep.append(input(p)[0])

			i['ganbun'] = '/'.join(rep)

		with open(jsonpath+"/"+fname, 'w', encoding='utf-8-sig') as jsonf:
			jsonString = json.dumps(fromjson, indent=4, ensure_ascii=False)
			jsonf.write(jsonString)