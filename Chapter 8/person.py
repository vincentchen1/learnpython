def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

#this function takes in simple textual information and puts it into a more meaningful data structure that lets you work with the information beyond just printing it

#storing person's age as well
#added new optional parameter age to the function definition and assigned the parameter the special value None, used when a variable has no specific value
#in conditional tests, None evaluates to False
def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
