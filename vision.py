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
    texts = response.text_annotations
    for text in texts:

        if len(text.description) == 7:
                license_number=text.description
    print(licensePlateInfo(license_number))
    return license_number


def licensePlateInfo(licensePlate):
    #check in database for a match between license plate and cop, and return cop details
    #returning hard coded information for now

    return "Officer: XXX YYY, Officer ID: XXXXXX, Officer License Number: " + licensePlate + " Police Station: Seattle Police Station, Arrest History: Has arrested people in the past for murder and gun violence, Miscellaneous Details: "

print(detectText('carpic.jpg'))  # pass in name of image