
import speech_recognition as sr

def main():
    sound = "audio2.wav"

    r = sr.Recognizer()



    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)


        print("Converting Audio To Text ..... ")


        audio = r.listen(source)



    try:
        
        print("Converted Audio Is : \n" + r.recognize_google(audio))

        

    


    except Exception as e:
        print("Error {} : ".format(e) )



if __name__ == "__main__":
    main()
