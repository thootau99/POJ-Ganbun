from os import walk
import csv 
import json 

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8-sig') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  		
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8-sig') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        jsonf.write(jsonString)

f = []

for (_, _, filename) in walk('./ChhoeTaigiDatabase'):
	for fname in filename:
		name = fname.split('.')[0]
		csv_to_json(rf'./ChhoeTaigiDatabase/{name}.csv', rf'./json/{name}.json')