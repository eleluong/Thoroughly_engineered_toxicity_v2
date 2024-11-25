from services.together import infer_chat
from services.modestus import assess_toxicity
from config import settings

import numpy as np
import json
from tqdm import tqdm

model_list = settings.seed_model_list

import concurrent.futures


def execute_multithreading_functions(functions):
    results = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for function in functions:
            results.append(executor.submit(function["fn"], **function["args"]))

    return [result.result() for result in results]


def evaluate_prompt(
    test_prompt: str = "",
    model_list: list = model_list,
    test_policy_name: str = "",
    test_policy: str = "",
):
    """
    Evaluate a given prompt using a list of models and assess the safety of the responses.

    Parameters:
    - test_prompt (str): The prompt to be evaluated.
    - model_list (list): A list of models to generate responses.
    - test_policy_name (str): The name of the safety policy.
    - test_policy (dict): The safety policy configuration.

    Returns:
    - dict: A dictionary containing the prompt, results for each model, and policy details.
    """
    test_chat = [{"role": "user", "content": test_prompt}]

    outputs = []

    for model in model_list:
        try:
            response = infer_chat(test_chat, model)
            while True:
                try:
                    safety_score = assess_toxicity(
                        response, {test_policy_name: test_policy}
                    )
                    break
                except Exception as e:
                    print("ERROR: ", e)
            outputs.append(
                {
                    "model_name": model,
                    "response": response,
                    "safety_evaluation": safety_score,
                }
            )
        except Exception as e:
            print(f"Error processing model {model}: {e}")
            outputs.append(
                {
                    "model_name": model,
                    "response": None,
                    "safety_evaluation": None,
                    "error": str(e),
                }
            )

    return {
        "prompt": test_prompt,
        "results": outputs,
        "policy_name": test_policy_name,
        "policy_description": test_policy,
    }


def evaluate_results(
    results: list = [], test_policy_name: str = "", test_policy: str = ""
):

    avg = {
        "Qwen/Qwen2.5-7B-Instruct-Turbo": [],
        "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo": [],
        "google/gemma-2-9b-it": [],
        "mistralai/Mistral-7B-Instruct-v0.3": [],
    }
    for sample in results:
        for result in sample["results"]:
            # print(result)
            if (
                result["safety_evaluation"] != None
                and result["safety_evaluation"] != 0
                and result["safety_evaluation"] != {}
            ):
                try:
                    avg[result["model_name"]].append(
                        result["safety_evaluation"][test_policy_name]["result"]
                    )
                except Exception as e:
                    print("ERROR: ", e)
                    avg[result["model_name"]].append(0)
            else:
                avg[result["model_name"]].append(0)
    outputs = {}
    for k, v in avg.items():
        outputs[k] = np.mean(v)
    return outputs


def process_batch_prompts(
    prompts: list = [],
    test_policy_name: str = "",
    test_policy: str = "",
    output_file="./evaluation_results/outputs.json",
    batch_size=4,
):
    outputs = []
    functions = []

    for candidate in tqdm(prompts):
        if len(functions) >= batch_size:
            results = execute_multithreading_functions(functions)
            outputs += results
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(outputs, f, ensure_ascii=False)
            functions = []
            evaluation_results = evaluate_results(
                outputs, test_policy_name, test_policy
            )
            for k, v in evaluation_results.items():
                print(f"{k} Toxicity score: {v}")

        functions.append(
            {
                "fn": evaluate_prompt,
                "args": {
                    "test_prompt": candidate,
                    "model_list": model_list,
                    "test_policy_name": test_policy_name,
                    "test_policy": test_policy,
                },
            }
        )

    if functions:
        results = execute_multithreading_functions(functions)
        outputs += results

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(outputs, f, ensure_ascii=False)

    return evaluate_results(outputs, test_policy_name, test_policy)
