import os
 
script_dir = os.path.dirname(__file__)
with open (os.path.join(script_dir,"ads", "ad-contents", "content_66864339.txt")) as myfile:
   data=myfile.read()
   print data