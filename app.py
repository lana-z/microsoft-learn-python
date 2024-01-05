object_size = 10
if object_size > 5:
    print('We need to keep an eye on this object.')
else:
    print('Object poses no threat.')

#===============
    
object_size = 10 
proximity = 9000
if object_size > 5 and proximity < 1000:
    print('Evasive maneuvers required.')
else:
    print('Object poses no threat.')


fact = "The Moon has no atmosphere."
two_facts = fact + "No sound can be heard on the Moon."
print(two_facts)

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)
print("temperatures" in text.lower())