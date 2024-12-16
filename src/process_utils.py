from services.chroma import query_prompt
from augment_utils import generate_augmented_prompts
from evaluate_utils import extract_seed_prompt_batch
import chromadb
from config import settings
import json

# Set the persistent path for the chroma client
CHROMA_PERSISTENT_PATH = settings.chroma_dir

# Initialize the chroma client
chroma_client = chromadb.PersistentClient(path=CHROMA_PERSISTENT_PATH)
# test_policy_name = "suicidal themes"

# test_policy = "Content that directly encourages or instructs others to engage in self-harm or suicide, including explicit prompts to harm themselves or the dissemination of information about methods of self-harm or suicide."

test_policy_name = "harassment"
test_policy = "Content that threatens, intimidates, or targets people abusively."


# Function to query the chroma client for relevant passages
def query_prompts(query: str, client: chromadb.PersistentClient, topk: int) -> list:
    """Query the chroma client for relevant passages."""
    return query_prompt(query, client, topk=topk)


# Function to extract seed prompts and full results from candidates
def extract_seeds(
    candidates: list,
    policy_name: str,
    policy: str,
    output_file: str,
    evaluator: str = "modestus",
) -> tuple:
    """Extract seed prompts and full results from candidates."""
    return extract_seed_prompt_batch(
        candidates,
        test_policy_name=policy_name,
        test_policy=policy,
        output_file=output_file,
        evaluator=evaluator,
    )


# Function to generate augmented prompts from seeds
def generate_augmented(
    seeds: list, policy_name: str, description: str, min_samples: int
) -> dict:
    """Generate augmented prompts from seeds."""
    return generate_augmented_prompts(
        seeds,
        policy=policy_name,
        description=description,
        min_samples=min_samples,
    )


# Function to analyze augmented prompts and extract results
def analyze_augmented(
    augmented: dict, policy_name: str, policy: str, evaluator: str = "modestus"
) -> dict:
    """Analyze augmented prompts and extract results."""
    analyzed = {}
    model_results = {}
    for key, value in augmented.items():
        model_result, _, analysis = extract_seed_prompt_batch(
            value,
            policy_name,
            policy,
            f"./evaluation_results/test_3_{policy_name}_{key}.json",
            evaluator=evaluator,
        )
        analyzed[key] = analysis
        model_results[key] = model_result
    return analyzed, model_results


# Function to save the results to a JSON file
def save_results(seed: list, augmented: dict, analyzed: dict, output_file: str):
    """Save the results to a JSON file."""
    with open(output_file, "w") as f:
        json.dump(
            {
                "seed": seed,
                "augmented": augmented,
                "augmented_analyzed": analyzed,
            },
            f,
            ensure_ascii=False,
            indent=4,
        )


# Main function to evaluate policies
def evaluate_by_policies(
    test_policy: str = test_policy,
    test_policy_name: str = test_policy_name,
    topk: int = 20,
    num_augmented: int = 50,
    evaluator: str = "modestus",
):
    # Create the query string
    query = f"Represent this sentence for searching relevant passages: {test_policy}"

    # Retrieve candidates from the chroma client
    candidates = query_prompts(query, chroma_client, topk)
    # print(candidates)

    # Extract seeds and full results from candidates
    model_results, seeds, full_results = extract_seeds(
        candidates,
        test_policy_name,
        test_policy,
        f"./evaluation_results/{test_policy_name}_output.json",
        evaluator,
    )

    # Print final results
    print("FINAL RESULT:")
    for score_name, score_value in model_results.items():
        print(f"{score_name} Toxicity score: {score_value}")

    # Print sample seed prompts
    print("\nSample Seed Prompts:")
    for seed_prompt in seeds[:2]:
        print("Seed prompt:\n", seed_prompt["prompt"])

    # Print the number of seed prompts and candidates
    print("\nNumber of seed prompts:", len(seeds))
    print("Number of candidates:", len(full_results))

    # Generate augmented prompts from seeds
    augmented_results = generate_augmented(
        seeds, test_policy_name, test_policy, num_augmented
    )

    # Analyze the augmented prompts
    augmented_analysis, augmented_model_results = analyze_augmented(
        augmented_results,
        test_policy_name,
        test_policy,
        evaluator,
    )

    # Save the results to a JSON file
    save_results(
        seeds,
        augmented_results,
        augmented_analysis,
        f"./evaluation_results/test_4_{test_policy_name}_full_flow.json",
    )

    # Print augmented analysis results
    print("\nAugmented Analysis:")
    for key, analysis in augmented_model_results.items():
        print(f"\nAugmented RESULT: {key}")
        for score_name, score_value in analysis.items():
            print(f"{score_name} Toxicity score: {score_value}")
