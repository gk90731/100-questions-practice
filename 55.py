'''Question: Please add a new employee to the dictionary.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
Expected output:

{'employees': [{'firstName': 'John', 'lastName': 'Doe'},
               {'firstName': 'Anna', 'lastName': 'Smith'},
               {'firstName': 'Peter', 'lastName': 'Jones'},
               {'firstName': 'Albert', 'lastName': 'Bert'}],
 'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
            {'firstName': 'Jessy', 'lastName': 'Petter'}]}'''
######################################################################
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
d2={'firstName': 'Albert', 'lastName': 'Bert'}
d["employees"].append(d2)
print(d)


###################################################################
"""alternate:
d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))"""
