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

        response = client.analyze_entities(
            document=document, 
            encoding_type='UTF32',
        )

        # for entity in response.entities:
        #     print('Name: {}'.format(entity.name))
        #     print('Type: {}'.format(entity.type))
        #     print('Metadata: {}'.format(entity.metadata))
        #     print('Salience: {}'.format(entity.salience))
        #     if (entity.type == 'PERSON'):
        #         list.add(entity)

        important_details = []
        for entity in response.entities:
            print('=' * 79)
            entity_type = enums.Entity.Type(entity.type).name
            results = [
                ('name', entity.name),
                ('type', entity_type),
                ('salience', entity.salience),
                ('wikipedia_url', entity.metadata.get('wikipedia_url', '-')),
            ]
            if (entity_type == 'PERSON' or entity_type == 'LOCATION' or
                entity_type == 'ORGANIZATION' or entity_type == 'PHONE_NUMBER' or
                entity_type == 'ADDRESS' or entity_type == 'DATE'):
                important_details.append(entity.name)

            for k, v in results:
                print('{:15}: {}'.format(k, v))    

        print(important_details)    
        print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

        if (sentiment.score <= -0.3):
            alert_users()
            alert_family()

analyze_text('copinteraction.txt')



