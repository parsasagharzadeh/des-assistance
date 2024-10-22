from media import Media
from fileManager import fileManager
from speechToText import VoiseText

class Main (Media , fileManager , VoiseText):
  def __init__(self, sender):
    super().__init__(sender)
    
my_instance = Main(sender="psa")    
# ساخت دیکشنری که نام متدها را به خود متدها نگاشت می‌کند
method_map = {method_name: getattr(my_instance, method_name) for method_name in dir(my_instance) if callable(getattr(my_instance, method_name)) and not method_name.startswith("__")}
methodName = []
for method  in method_map:
  methodName.append(method)
  
mtoi =[i for i in range(len(methodName))]

print(method_map[methodName[mtoi[0]]]())

# so we have to create model to convert propose to final desion

