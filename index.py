import re
def disemvowel(string):
    result = re.sub('a|i|u|e|o|A|I|U|E|O','',string) 
    return result