input_string = "Hello, how are you? This is a simple example. Hello, world!"
input_string = "I can't code and I cant study"

'''
Write a Python function called word_frequency_counter that takes a string as input and returns a dictionary where keys are unique words in the input string, and values are the frequencies of those words.
special characters should be ignored

can't and cant should be considred as one word
'''

def word_frequency_counter(input_string) :
    strlist = input_string.split(" ")
    _dict ={}
    for s in strlist:
        chlist = [c for c in s if c.isalnum()]
        word = "".join(chlist).lower()
        if _dict.get(word,0) == 0:
            _dict.update({word :1})
        else :
            val = _dict.get(word, 0)
            _dict.update({word :val+1})
    return _dict

result = word_frequency_counter(input_string)
print(result)