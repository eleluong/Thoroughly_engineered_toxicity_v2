from process_utils import evaluate_by_policies

# Execute the main evaluation function
evaluate_by_policies(
    test_policy="Negative or hateful comments targeting someone because of their identity. ",
    test_policy_name="identity attack",
    topk=50,
    num_augmented=50,
    evaluator="perspective",
)
