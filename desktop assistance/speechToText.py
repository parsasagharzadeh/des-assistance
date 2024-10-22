import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
class VoiseText():
  def __init__(self):
    self.text=""
  def recordVoise(self):
    while(1):
      try:
        with sr.Microphone() as source2 :
          r.adjust_for_ambient_noise(source2,duration=0.2)
          audio2 = r.listen(source2)
          self.text = r.recognize_google(audio2)
          self.saveLastText()
          if self.text == "exit":
            break
          return self.text
      except sr.RequestError as e:
        print("could not request results; {0}".format(e))
      except sr.UnknownValueError:
        print("unknown error")
        
      
        
  def saveLastText(self):
    f= open("lastSpeach.txt","a")
    f.write(self.text)
    f.write("/n")
    f.close()
    return
  
# f = VoiseText()

# # while(1):
# f.recordVoise()