from llms.openai import Openai
from utils.prompt import get_prompt

model = Openai("gpt-3.5-turbo")
prompt = get_prompt()

print(f"[user] \n{prompt}")
messages = [{"role": "user", "content": prompt}]
while True:
    res = model.infer(messages)
    print(f"[chatgpt]\n{res}")
    messages.append({"role": "system", "content": res})
    prompt = input("[user]\n")
    messages.append({"role": "user", "content": prompt})
