#!/usr/bin/env python3

def return_evens(num_list):
    evens = [num for num in num_list if num % 2 == 0]
    return evens
# example usage
result = return_evens([0, 1, 3, 5, 7, 8, 9])
print(result) #the example,s output [0, 8]

def make_exclamation(sentence_list):
    if not sentence_list:
        return  []
    exclamation_list = [sentence + '!' for sentence in sentence_list]
    return exclamation_list
# example usage
result = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(result)  #the example's output ['Hello!', "I'm doing great!", 'Python is fun!']
