from typing import List

class LLM:
    def __init__(self, name):
        self.name = name
        self.count = 0
        self.prompt_length = 0
        self.completion_length = 0


    def infer(self, prompt: List[str]):
        pass