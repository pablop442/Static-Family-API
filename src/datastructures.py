
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": 'John',
                "last_name": self.last_name, 
                "age" : 33,
                'lucky_numbers': [7, 13, 22]
            },

            {
                "id": self._generateId(),
                "first_name": 'Jane',
                "last_name": self.last_name, 
                "age" : 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": 'Jimmy',
                "last_name": self.last_name, 
                "age" : 5,
                "lucky_numbers": [1]
            },

        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        value = {
            # "id": self._generateId(),
            "first_name": str(member["first_name"]),
            "last_name": self.last_name,
            "age": int(member["age"]), 
            "lucky_numbers": member["lucky_numbers"]
            }
        
        if "id" in member:
            value["id"] = int(member["id"])
        else:
            value["id"] = self._generateId()
        self._members.append(value)
        

    def delete_member(self, id):
        for member in range(len(self._members)):
            if self._members[member]['id'] == int(id):
                return self._members.pop(member)
        return None
            
    def get_member(self, id):
        for member in range(len(self._members)):
            if self._members[member]['id'] == int(id):
                return self._members[member]
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members


    def update_member(self, id, member):
        for member in range(len(self._members)):
            if self._members[member]["id"] == int(id):
                return self._members[member].update(member)


jackson_family = FamilyStructure('Jackson')
# jackson_family.add_member('2')


print(jackson_family.get_all_members())
# print(jackson_family.delete_member('2'))
# print(jackson_family.get_member('2'))