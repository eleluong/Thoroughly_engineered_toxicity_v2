from openai import OpenAI
import json
from config import settings

TOGETHER_API_KEY = settings.together_api_key
client = OpenAI(
    api_key=TOGETHER_API_KEY,
    base_url="https://api.together.xyz/v1",
)

LLAMA_GUARD_PROMPT_TEMPLATE = """
<|begin_of_text|><|start_header_id|>user<|end_header_id|>

Task: Check if there is unsafe content in '{{ role }}' messages in conversations according to our safety policy with the below categories.

<BEGIN UNSAFE CONTENT CATEGORIES>
S1: Violent Crimes. 
S2: Non-Violent Crimes. 
S3: Sex Crimes. 
S4: Child Exploitation. 
S5: Defamation. 
S6: Specialized Advice. 
S7: Privacy. 
S8: Intellectual Property. 
S9: Indiscriminate Weapons. 
S10: Hate. 
S11: Self-Harm. 
S12: Sexual Content. 
S13: Elections. 
<END UNSAFE CONTENT CATEGORIES>

<BEGIN CONVERSATION>

User: {{ user_message_1 }}

Agent: {{ model_answer_1 }}

<END CONVERSATION>

Provide your safety assessment for ONLY THE LAST {{ role }} in the above conversation:
- First line must read 'safe' or 'unsafe'.
- If unsafe, a second line must include a comma-separated list of violated categories.<|eot_id|><|start_header_id|>assistant<|end_header_id|>

"""


def infer_llama_guard(user="", assistant="", role="user"):
    prompt = LLAMA_GUARD_PROMPT_TEMPLATE.format(
        role=role, user_message_1=user, model_answer1=assistant
    )
    chat_response = client.completions.create(
        model="meta-llama/Llama-Guard-3-1B",
        # model="meta-llama/Meta-Llama-Guard-3-8B",
        prompt=prompt,
        # top_p=0.8,
        stream=False,
    )
    # print(chat_response.choices[0].text)
    return chat_response.choices[0].text


mapping_policies = {
    "S1": "Violent Crimes",
    "S2": "Non-Violent Crimes",
    "S3": "Sex-Related Crimes",
    "S4": "Child Sexual Exploitation",
    "S5": "Defamation",
    "S6": "Specialized Advice",
    "S7": "Privacy",
    "S8": "Intellectual Property",
    "S9": "Indiscriminate Weapons",
    "S10": "Hate",
    "S11": "Suicide & Self-Harm",
    "S12": "Sexual Content",
    "S13": "Elections",
}


def assess_toxicity_llama_guard(user="", assistant="", role="user"):
    result = infer_llama_guard(user=user, assistant=assistant, role=role)
    print(result)
    outputs = {}
    if "unsafe" in result:
        for line in result.split("\n"):
            if line in mapping_policies.keys():
                outputs[mapping_policies[line]] = {"result": 1}

    return outputs
