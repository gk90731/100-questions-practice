'''Question: Please download the json file in the attachment and use Python to add a new employee to the content of the file so that the file looks like in the expected output below.'''

#########################################################################

import json

content = json.loads(open('58company1.json').read())
d1={"firstName":"Albert","lastName":"Bert"}
content["employees"].append(d1)
print(content)
