#!/usr/bin/env python3

def return_evens(num_list):
    evens = [num for num in num_list if num % 2 == 0]
    return evens
# example 
result = return_evens([0,1,2,3,4,5,6,7,8,9,10,11])
print(result) #the example,s output [0, 2, 4, 6, 8, 10]

def make_exclamation(sentence_list):
    if not sentence_list:
        return  []
    exclamation_list = [sentence + '!' for sentence in sentence_list]
    return exclamation_list
# exxample
result = make_exclamation(["Hello there", "I'm a developer", "I am learning  python"])
print(result)  #the example's output  ['Hello there!', "I'm a developer!", 'I am learning  python!']
