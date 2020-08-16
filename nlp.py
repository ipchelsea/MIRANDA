# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
# export GOOGLE_APPLICATION_CREDENTIALS="/Users/rahulpulidindi/Downloads/Miranda-60c57eeb597d.json"

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/rahulpulidindi/Downloads/Miranda-60c57eeb597d.json"

# Instantiates a client
client = language.LanguageServiceClient()

def analyze_text(textFile) :
    with open(textFile) as f:
        text = f.read()
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT
        )

        sentiment = client.analyze_sentiment(document=document).document_sentiment

        print('Text: {}'.format(text))
        print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

        response = client.analyze_entities(
            document=document, 
            encoding_type='UTF32',
        )

        for entity in response.entities:
            print('Name: {}'.format(entity.name))
            print('Type: {}'.format(entity.type))
            print('Metadata: {}'.format(entity.metadata))
            print('Salience: {}'.format(entity.salience))

analyze_text('/Users/rahulpulidindi/Downloads/policeinteraction.txt')



