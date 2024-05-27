#!/usr/bin/env python3

class MyString:

  def __init__(self, value = ""):
    self._value = value
    
  def get_value(self):
    return self._value

  def set_value(self, stringVal):
    if (type(stringVal) == str):
      self._value = stringVal
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
    return self._value.endswith(".")

  def is_question(self):
    return self._value.endswith("?")

  def is_exclamation(self):
    return self._value.endswith("!")

  def count_sentences(self):
    value = self.value
    value = self.replace_punctuation(value)
    sentences = self.split_into_sentences(value)
    return len(sentences)

  def replace_punctuation(self, value):
    for punc in ['!','?']:
        value = value.replace(punc, '.')
    return value

  def split_into_sentences(self, value):
    sentences = [s for s in value.split('.') if s]
    return sentences
  
my_string = MyString("I am going to the store. Do you want some? That's great!")
print(my_string.count_sentences()) 