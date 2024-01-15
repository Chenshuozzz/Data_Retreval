import time
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat

from llms.llm import LLM
# from llms.config import OPENAI_KEY
import openai

openai.api_key = "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"


class Openai(LLM):
    models = {'gpt-4', 'gpt-3.5-turbo', 'text-davinci-003'}

    def __init__(self, name, interval=0, **kwargs):
        super().__init__(name)
        if 'api_key' in kwargs:
            if kwargs['api_key']:
                openai.api_key = kwargs['api_key']
        if self.name in {'gpt-4', 'gpt-3.5-turbo'}:
            self.api = openai.ChatCompletion.create
        elif self.name in {'text-davinci-003'}:
            self.api = openai.Completion.create
        else:
            raise LookupError("Please use valid model name for Openai model")
        self.interval = interval

    def infer(self, messages):
        response = None
        while not response:
            try:
                if self.name in {'gpt-4', 'gpt-3.5-turbo'}:
                    response = self.api(
                        model=self.name,
                        messages=messages,
                        # temperature=0,
                        max_tokens=1024,
                        # top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0,
                        request_timeout=30,
                    )
                elif self.name in {'text-davinci-003'}:
                    response = self.api(
                        model=self.name,
                        prompt=prompt,
                        # temperature=0,
                        max_tokens=128,
                        # top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0,
                        request_timeout=30,
                    )
            except Exception as e:
                print(e)
                time.sleep(12)
                response = None
        
        res_msg = response.choices[0].message
        
        return res_msg["content"].strip()


    # def infer(self, prompt, **kwargs):
    #     response = self.__infer_one(prompt, kwargs)
    #     return response.choices[0].message.content

    # def infer(self, prompt_list, **kwargs):
    #     assert isinstance(prompt_list, list), "Please make sure the input is a list of str"
    #     res = []
    #     with ThreadPoolExecutor(max_workers=min(len(prompt_list), 32)) as pool:
    #         response_list = pool.map(self.__infer_one, prompt_list, repeat(kwargs))
    #         for response in response_list:
    #             self.count += 1
    #             if self.name in {'gpt-4', 'gpt-3.5-turbo'}:
    #                 res.append([choice.message.content for choice in response.choices])
    #                 self.prompt_length += response.usage.prompt_tokens
    #                 self.completion_length += response.usage.completion_tokens
    #             elif self.name in {'text-davinci-003'}:
    #                 # res.append([choice.message.content for choice in response.choices])
    #                 res.append([choice.text.strip() for choice in response.choices])
    #                 self.prompt_length += response.usage.prompt_tokens
    #                 self.completion_length += response.usage.completion_tokens
    #             else:
    #                 res.append(response.choices)
    #         time.sleep(self.interval)
    #     return res


