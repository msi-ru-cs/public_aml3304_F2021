import numpy as np
import nltk
nltk.download('punkt')

sentence = "At eight o'clock on Thursday morning"
tokens = nltk.word_tokenize(sentence)
print(tokens)


x = np.array([2, 5])
a = x[0]
b = x[1]
c = a + b

if (c >= 5):
    c = c + 1
    # Swap the values of a and b
    a = a + b
    b = a - b
    a = a - b
else:
    c = c + 10
    temp = a
    a = b
    b = temp
# print(a, b)