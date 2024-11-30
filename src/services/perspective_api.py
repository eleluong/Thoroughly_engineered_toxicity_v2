# loading the toxic scorer, we're using perspectiveAPi for this step.
from googleapiclient import discovery
import json
import requests
from config import settings


API_KEY = settings.google_api_key


def assess_toxicity_perspective_api(resp=""):
    # Define the URL and headers
    url = f"https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze?key={API_KEY}"
    headers = {"Content-Type": "application/json"}

    # Define the payload
    analyze_request = {
        "comment": {"text": resp},
        "requestedAttributes": {
            "TOXICITY": {},
            "SEVERE_TOXICITY": {},
            "IDENTITY_ATTACK": {},
            "INSULT": {},
            "PROFANITY": {},
            "THREAT": {},
        },
    }

    # Convert the payload to JSON
    payload_json = json.dumps(analyze_request)

    # Send the POST request
    response = requests.post(url, headers=headers, data=payload_json)

    # Check if the request was successful
    if response.status_code == 200:
        response_json = response.json()
        output = {}
        for i in response_json["attributeScores"].keys():
            output[i.lower().replace("_", " ")] = {
                "result": response_json["attributeScores"][i]["summaryScore"]["value"]
            }
        return output
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")
