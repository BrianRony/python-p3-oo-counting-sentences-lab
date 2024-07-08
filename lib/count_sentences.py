#!/usr/bin/env python3

class MyString:
    def __init__(self, value="") -> None:
        self._value = value

    @property
    def value(self):
        return self._value
  
    @value.setter
    def value(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")
  
    def is_question(self):
        return self._value.endswith("?")
  
    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        import re
        sentences = re.split(r'[.!?]', self._value)
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)