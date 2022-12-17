Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import nltk
print(nltk._file_)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(nltk._file_)
AttributeError: module 'nltk' has no attribute '_file_'. Did you mean: '__file__'?
print(nltk._file__)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(nltk._file__)
AttributeError: module 'nltk' has no attribute '_file__'. Did you mean: '__file__'?
print(nltk.__file__)
C:\Users\ACER\AppData\Roaming\Python\Python310\site-packages\nltk\__init__.py
from nltk.corpus import brown
print(",".join(brown.words()))
Traceback (most recent call last):
  File "C:\Users\ACER\AppData\Roaming\Python\Python310\site-packages\nltk\corpus\util.py", line 84, in __load
    root = nltk.data.find(f"{self.subdir}/{zip_name}")
  File "C:\Users\ACER\AppData\Roaming\Python\Python310\site-packages\nltk\data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mbrown[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('brown')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/brown.zip/brown/[0m

  Searched in:
    - 'C:\\Users\\ACER/nltk_data'
    - 'C:\\Users\\ACER\\AppData\\Local\\Programs\\Python\\Python310\\nltk_data'
    - 'C:\\Users\\ACER\\AppData\\Local\\Programs\\Python\\Python310\\share\\nltk_data'
    - 'C:\\Users\\ACER\\AppData\\Local\\Programs\\Python\\Python310\\lib\\nltk_data'
    - 'C:\\Users\\ACER\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(",".join(brown.words()))
  File "C:\Users\ACER\AppData\Roaming\Python\Python310\site-packages\nltk\corpus\util.py", line 121, in __getattr__
    self.__load()
  File "C:\Users\ACER\AppData\Roaming\Python\Python310\site-packages\nltk\corpus\util.py", line 86, in __load
    raise e
  File "C:\Users\ACER\AppData\Roaming\Python\Python310\site-packages\nltk\corpus\util.py", line 81, in __load
    root = nltk.data.find(f"{self.subdir}/{self.__name}")
  File "C:\Users\ACER\AppData\Roaming\Python\Python310\site-packages\nltk\data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mbrown[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('brown')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/brown[0m

  Searched in:
    - 'C:\\Users\\ACER/nltk_data'
    - 'C:\\Users\\ACER\\AppData\\Local\\Programs\\Python\\Python310\\nltk_data'
    - 'C:\\Users\\ACER\\AppData\\Local\\Programs\\Python\\Python310\\share\\nltk_data'
    - 'C:\\Users\\ACER\\AppData\\Local\\Programs\\Python\\Python310\\lib\\nltk_data'
    - 'C:\\Users\\ACER\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************

