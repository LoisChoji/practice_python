#collects input and prints it backward
n = input("Enter a sentence and will get it backward: ")
def your_request(n):
    return n
print(your_request(n))
word_backward =' '.join(reversed(n.split(' ')))
print(word_backward )