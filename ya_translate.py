import argparse
import os.path
import sys
import requests

parser = argparse.ArgumentParser()
parser.add_argument("-s", default="en", help="Source language code")
parser.add_argument("-t", default="ru", help="Target language code")
parser.add_argument("-a", default="", help="Yandex.Cloud API key")
parser.add_argument("-f", default="", help="Yandex.Cloud folder ID")
parser.add_argument("-v", default="0", help="Verbose")
args = parser.parse_args()

fileName = "Localizable"
fileExtension = "strings"

originFile = fileName + "." + fileExtension
outputFile = fileName + "_" + args.t + "." + fileExtension
 
if not os.path.exists(originFile):
	sys.exit(originFile + " not found")
if os.path.exists(outputFile):
	os.remove(outputFile)

print("Will start translating")

stringSeparator = " = "

def translate(origin):
	url = "https://translate.api.cloud.yandex.net/translate/v2/translate"
	body = {
		"sourceLanguageCode": args.s,
		"targetLanguageCode": args.t,
		"folderId": args.f,
		"texts": [
			origin
		]
	}
	headers = {
		"Authorization": "Api-Key " + args.a
	}

	response = requests.post(url, json=body, headers=headers)
	response.raise_for_status()

	json = response.json()

	return json["translations"][0]["text"]

def writeTranslation(key, translation):
	with open(outputFile, "a") as output:
		output.write(key + stringSeparator + translation + "\n")
		output.close()

origin_file = open(originFile, "r")
for line in origin_file:
	if line[0] == "\"":
		origin_pair = line.split(stringSeparator)
		translation = translate(origin_pair[1][:-1])

		if args.v == "1":
			print("Translating " + origin_pair[0] + ": " + origin_pair[1] + " -> " + translation)

		writeTranslation(origin_pair[0], translation)
