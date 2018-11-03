print("Mad Libs Generator")

noun = input("Noun: ")
nouns = input("Nouns: ")
second_nouns = input("Noun: ")
place = input("Place: ")
adjective = input("Adjective: ")
third_noun = input("Noun: ")

print("Be kind to your %s-footed %s,For a duck may be somebody`s %s, Be kind to your %s in %s Where the weather is always %s. You may think that this is the %s, Well it is." % (noun,nouns,second_nouns,nouns,place,adjective,third_noun))