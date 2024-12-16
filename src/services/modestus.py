import requests, json
from config import settings

MODESTUS_API_KEY = settings.modestus_api_key


def assess_toxicity(
    prompt, metrics
):  
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


