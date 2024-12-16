from process_utils import evaluate_by_policies

from services.modestus import assess_toxicity

# Execute the main evaluation function

# evaluate_by_policies(
#     test_policy="Negative or hateful comments targeting someone because of their identity",
#     test_policy_name="identity attack",
#     topk=500,
#     num_augmented=500,
#     evaluator="perspective",
# )

# evaluate_by_policies(
#     test_policy="Describes an intention to inflict pain, injury, or violence against an individual or group",
#     test_policy_name="threat",
#     topk=500,
#     num_augmented=500,
#     evaluator="perspective",
# )

# "systemic bias": "Content perpetuating societal biases, excluding analytical or advocacy material."
evaluate_by_policies(
    test_policy="Content perpetuating societal biases, excluding analytical or advocacy material.",
    test_policy_name="systemic bias",
    topk=500,
    num_augmented=500,
    evaluator="modestus",
)


# "child abuse": "Content depicting or promoting harm to minors, excluding awareness or protection efforts.",
# evaluate_by_policies(
#     test_policy="Content depicting or promoting harm to minors, excluding awareness or protection efforts.",
#     test_policy_name="child abuse",
#     topk=500,
#     num_augmented=500,
#     evaluator="modestus",
# )


# evaluate_by_policies(
#     test_policy="Content that promotes, encourages, or depi   cts acts of self-harm, such as suicide, cutting, and eating disorders.",
#     test_policy_name="self harm",
#     topk=500,
#     num_augmented=500,
#     evaluator="openai",
# )



