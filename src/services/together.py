from openai import OpenAI
import json
from config import settings

TOGETHER_API_KEY = settings.together_api_key
client = OpenAI(
    api_key=TOGETHER_API_KEY,
    base_url="https://api.together.xyz/v1",
)
# default_model = "meta-llama/Llama-2-70b-chat-hf"
# default_model = "NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO"
# default_model = "cognitivecomputations/dolphin-2.5-mixtral-8x7b"

default_model = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"


def infer_chat(chat, model=default_model, max_tokens=250):
    chat_response = client.chat.completions.create(
        model=model,
        messages=chat,
        max_tokens=max_tokens,
        stream=False,
    )

    return chat_response.choices[0].message.content
