import os
from openai import OpenAI
from dotenv import load_dotenv


class Configuration:
    def __init__(self):
        self.load_env()
        self.api_key = os.getenv("LLM_API_KEY")
        self.url = os.getenv("URL")

    @staticmethod
    def load_env():
        load_dotenv()

    @property
    def llm_api_key(self):
        if not self.api_key:
            raise ValueError("LLM_API_KEY is not set in the environment variables.")
        return self.api_key

    @property
    def llm_url(self):
        if not self.url:
            raise ValueError("URL is not set in the environment variables.")
        return self.url


config = Configuration()
client = OpenAI(
    api_key=config.api_key,
    base_url=config.url,
)
completion = client.chat.completions.create(
    model="qwen-plus",  # 此处以qwen-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁？"},
    ],
)

print(completion.model_dump_json())
