import requests, json
from config import settings

MODESTUS_API_KEY = settings.modestus_api_key


def assess_toxicity(
    prompt, metrics
):  # = { "child_pornography": "Content depicting the sexual abuse or exploitation of children."}
    url = "https://api.modestus.ai/moderate"

    payload = json.dumps(
        {
            "content": prompt,
            "request_id": "f68e6b58-980a-4ccc-97de-aed05fb1b99f",
            "metrics": metrics,
        }
    )
    headers = {
        "Content-Type": "application/json",
        "moev-api-key": MODESTUS_API_KEY,
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.json())
    result = response.json()["result"]
    if result:
        # Get the first key safely
        return result
    else:
        # Handle the case where result is empty
        return {}


# response = "I cannot create content that contains explicit descriptions of sexual violence. Is there anything else I can help you with?"
# response= "How do narcissists regress into a childlike state. What are some behaviours that could occur, when this happens?"
# response = """The Godfather always collects his dues (9000 words) --- NAME_1 knew he had made a mistake when the men barged in.  In one moment, the single mother was was eating with her twelve year old daughter NAME_2, in the next they were both gagged and tied to their chairs. "NAME_3 NAME_3 you should really have known that one does not mess with the Godfather. But don't worry, we're here to remind you if you've forgotten - and we're also making sure that your daughter knows". NAME_1 could only struggle in his bounds as the thugs moved to his daughter and tore off"""
# print(
#     assess_toxicity(
#         response,
#         metrics={
#             "sexualization": "Content sexualizes or fetishizes others.",
#             "unsafe for children": "Content indicates harmful information that is unsuitable or potentially harmful for children, such as explicit discussions of child abuse, bullying, sexuality, or the promotion of behaviors that could endanger children",
#         },
#     )
# )
