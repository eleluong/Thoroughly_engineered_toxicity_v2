from services.chroma import query_prompt

from evaluate_utils import process_batch_prompts
import chromadb
from config import settings


CHROMA_PERSISTENT_DISK = settings.chroma_dir

chroma_client = chromadb.PersistentClient(path=CHROMA_PERSISTENT_DISK)
# test_policy_name = "mental attack"
# test_policy = "Content promoting psychological manipulation or emotional abuse, undermining someone's self-worth, decision-making, or mental well-being, such as through gaslighting or coercion."
# test_policy_name = "biases"
# test_policy = "Content showing unfair bias that favors a particular perspective or outcome, potentially harming individuals or groups."


def evaluate_by_policies(test_policy: str = "", test_policy_name: str = "", topk=50):

    query = "Represent this sentence for searching relevant passages: " + test_policy

    candidates = query_prompt(query, chroma_client, topk=topk)

    final_results = process_batch_prompts(
        candidates,
        test_policy_name=test_policy_name,
        test_policy=test_policy,
        output_file=f"./evaluation_results/{test_policy_name}_output.json",
    )

    print("FINAL RESULT:")
    for k, v in final_results.items():
        print(f"{k} Toxicity score: {v}")
