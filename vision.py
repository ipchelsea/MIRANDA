import os
import io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd
#export GOOGLE_APPLICATION_CREDENTIALS="/Users/karra/PycharmProjects/MIRANDA/venv/VisionAPI/Miranda-e0b8f3bf9017.json"

def detectText(imageName):
    client = vision.ImageAnnotatorClient()
    file_name = os.path.join(
        os.path.dirname(__file__),
        imageName)

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)  # returns TextAnnotation
    df = pd.DataFrame(columns=['locale', 'description'])

    texts = response.text_annotations
    for text in texts:
        df = df.append(
            dict(
                locale=text.locale,
                description=text.description
            ),
            ignore_index=True
        )
    return df
print(detectText('carpic.jpg'))    #pass in name of image


