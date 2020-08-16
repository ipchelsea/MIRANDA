# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
# export GOOGLE_APPLICATION_CREDENTIALS="/Users/rahulpulidindi/Downloads/Miranda-60c57eeb597d.json"

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""

# Instantiates a client
client = language.LanguageServiceClient()

<<<<<<< HEAD
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

analyze_text('policeinteraction.txt')

# # The text to analyze
# with open('policeinteraction.txt') as f:
#     text = f.read()
# document = types.Document(
#     content=text,
#     type=enums.Document.Type.PLAIN_TEXT)

# # Detects the sentiment of the text
# sentiment = client.analyze_sentiment(document=document).document_sentiment

# print('Text: {}'.format(text))
# print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

# response = client.analyze_entities(
#     document=document,
#     encoding_type='UTF32',
# )

# for entity in response.entities:
#     print('Name: {0}'.format(entity.name))
#     print('Type: {0}'.format(entity.type))
#     print('Metadata: {0}'.format(entity.metadata))
#     print('Salience: {0}'.format(entity.salience))


