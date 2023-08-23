#!/usr/bin/env python3

class MyString:
    def __init__(self,value=""):
        self._value=value

    def get_value(self):
        return self._value
    def set_value(self,value):
        if type(value) == str:
            self._value=value
        else:
            print("The value must be a string.")
            return "The value must be a string."

    value=property(get_value,set_value,)

    def is_sentence(self):
        return True if self._value.endswith(".") else False
        
    def is_question(self):
        return True if self._value.endswith("?") else False
  
    def is_exclamation(self):
        return True if self._value.endswith("!") else False
    
    def count_sentences(self):
        sentence=self._value
        for mark in ["?","!"]:
            sentence=sentence.replace(mark,".")
        sentences=[s for s in sentence.split(".") if s]
        return len(sentences)    

first=MyString("john")
first.value=123