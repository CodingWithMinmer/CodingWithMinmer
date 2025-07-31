from typing import List, Union
class CustomNestedInteger:
    def __init__(self,value):
        self.value: List['CustomNestedInteger' | int] = value