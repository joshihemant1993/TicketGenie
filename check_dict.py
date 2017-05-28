import shelve

description_to_keywords = shelve.open('description_to_keywords.db')

print len(description_to_keywords)

#print description_to_keywords
