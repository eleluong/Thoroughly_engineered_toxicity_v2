import ctranslate2
from transformers import AutoTokenizer

import torch
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import argparse
import time

model_name = "BAAI/bge-small-en-v1.5"
model_save_path = "/home/tinh/llama2/TET_v2/output/ct2_distilled_small"
# model_path = "bge_model_ctranslate2_base"


device = "cuda"
tokenizer = AutoTokenizer.from_pretrained(model_name)
if device == "cuda":
    translator = ctranslate2.Encoder(
        model_save_path, device=device, compute_type="float16", inter_threads=64
    )  # or "cuda" for GPU
else:
    translator = ctranslate2.Encoder(model_save_path, device=device)


def generate_embeddings(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    input_ids = inputs["input_ids"].tolist()[0]
    output = translator.forward_batch([input_ids])
    pooler_output = output.pooler_output
    if device == "cuda":
        embeddings = (
            torch.as_tensor(pooler_output, device=device).detach().cpu().tolist()[0]
        )
    else:
        pooler_output = np.array(pooler_output)
        embeddings = torch.as_tensor(pooler_output, device=device).detach().tolist()[0]
    return embeddings
