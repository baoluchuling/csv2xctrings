import argparse
import csv
import json

def generateSingleLanguage(comment, translates):

    localizations = {}
    for (language, trsnalate) in translates:
        localizations[language] = {
            "stringUnit" : {
                "state" : "translated",
                "value" : trsnalate
            }
        }

    return {
            "comment": comment,
             "extractionState" : "manual",
             "localizations" : localizations
        }

def generateLanguage(keys, translates):
    strings = {}
    for (key) in list:
        strings[key] = generateSingleLanguage("", {"":"", "":""})


parser = argparse.ArgumentParser(description='csv to xcstrings')
parser.add_argument('source', metavar='N', type=str, help='源文件')
parser.add_argument('target', metavar='N', type=str, help='目标文件')
args = parser.parse_args()
source = args.source
target = args.target

with open(source, encoding='utf-8') as file_obj:
    reader_obj = csv.reader(file_obj)
    languageList = {}
    strings = {}
    line = 0
    for row in reader_obj:
        if line == 0:
            1
        elif line == 1:
            del row[0]
            del row[0]
            languageList = row
        else:
            comment = row[1]
            key = row[2]
            del row[0]
            del row[0]
            strings[key] = generateSingleLanguage(comment, zip(languageList, row))
        line+=1
        

xcstrings = {
 "sourceLanguage" : "en",
 "strings" : strings,
 "version" : "1.0"
}

with open(target, 'w') as targetFile: 
     targetFile.write(json.dumps(xcstrings))
