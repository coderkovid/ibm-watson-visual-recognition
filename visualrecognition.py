import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
	'2018-03-19',
	url='https://gateway.watsonplatform.net/visual-recognition/api',
	iam_api_key='{iam_api_key}')

with open('./fruitbowl.jpg', 'rb') as images_file:
	classes = visual_recognition.classify(
		images_file,
		threshold='0.6',
		classifier_ids='kovid_692856023')
	print(json.dumps(classes, indent=2))
