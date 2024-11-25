import chromadb
from dotenv import load_dotenv
import uuid
from tqdm import tqdm

from services.ct2_embeddings import generate_embeddings
from config import settings

load_dotenv()
import os

CHROMA_ENDPOINT = None
COLLECTION_NAME = "prompts"
CHROMA_PERSISTENT_DISK = settings.chroma_dir

chroma_client = chromadb.PersistentClient(path=CHROMA_PERSISTENT_DISK)
chroma_client


def generate_id():
    return str(uuid.uuid4())


print(chroma_client.heartbeat())


def init_prompts(
    CHROMA_PERSISTENT_DISK=CHROMA_PERSISTENT_DISK, CHROMA_ENDPOINT=CHROMA_ENDPOINT
):
    if CHROMA_PERSISTENT_DISK != None:
        print("YAH")
        chroma_client = chromadb.PersistentClient(path=CHROMA_PERSISTENT_DISK)
    else:
        chroma_client = chromadb.HttpClient(host=CHROMA_ENDPOINT)
    print(chroma_client.heartbeat())
    chroma_client.get_or_create_collection(
        COLLECTION_NAME, metadata={"hnsw:space": "cosine"}
    )
    print(f"Collection {COLLECTION_NAME} initial successfully")


import concurrent.futures


def execute_multithreading_functions(functions):
    try:
        results = []

        with concurrent.futures.ThreadPoolExecutor() as executor:
            for function in functions:
                results.append(executor.submit(function["fn"], **function["args"]))

        return [result.result() for result in results]
    except Exception as e:
        raise Exception(f"Error executing multithreading functions: {e}")


def add_prompt(prompt="", collection=None):
    chunk = f"""{prompt}"""
    chunk_id = f"PROMPT-{generate_id()}"
    embedding = generate_embeddings(chunk)
    collection.add(
        embeddings=[embedding],
        metadatas=[{"content": prompt}],
        # documents = documents,
        ids=[chunk_id],
    )
    return "Suck seed"


def add_prompts(
    prompts=[],
    chroma_client=None,
    CHROMA_PERSISTENT_DISK=CHROMA_PERSISTENT_DISK,
    CHROMA_ENDPOINT=CHROMA_ENDPOINT,
):
    try:
        if chroma_client == None:
            if CHROMA_PERSISTENT_DISK != None:
                print("YASSS")
                chroma_client = chromadb.PersistentClient(path=CHROMA_PERSISTENT_DISK)
            else:
                chroma_client = chromadb.HttpClient(host=CHROMA_ENDPOINT)
        print(chroma_client.heartbeat())
        collection = chroma_client.get_collection(COLLECTION_NAME)
    except Exception as e:
        print("ERROR: ", e)
        return "Fail"
    functions = []
    contents = []
    for i in tqdm(prompts):
        try:
            if len(functions) >= 32:
                embeddings = execute_multithreading_functions(functions)

                collection.add(
                    embeddings=embeddings,
                    metadatas=contents,
                    ids=[generate_id() for i in range(len(contents))],
                )
                functions = []
                contents = []
            contents.append({"content": i})
            functions.append(
                {
                    "fn": generate_embeddings,
                    "args": {
                        "text": i,
                    },
                }
            )
            # add_prompt(i, collection)

        except Exception as e:
            print("ERROR: ", e)
            print("DROP: ", i)
    return "Suck seed"


def format_faqs(metadatas):
    # print(metadatas)
    outputs = [i["content"] for i in metadatas]

    return outputs


def query_prompt(
    policy="",
    chroma_client=None,
    CHROMA_PERSISTENT_DISK=CHROMA_PERSISTENT_DISK,
    CHROMA_ENDPOINT=CHROMA_ENDPOINT,
    topk=50,
):
    try:
        if chroma_client == None:
            if CHROMA_PERSISTENT_DISK != None:
                chroma_client = chromadb.PersistentClient(path=CHROMA_PERSISTENT_DISK)
            else:
                chroma_client = chromadb.HttpClient(host=CHROMA_ENDPOINT)
            print(chroma_client.heartbeat())
        collection = chroma_client.get_collection(name=COLLECTION_NAME)
    except:
        return f"Collection {COLLECTION_NAME} not found"
    query_results = collection.query(
        query_embeddings=generate_embeddings(policy), n_results=topk
    )
    # print(query_results)
    return format_faqs(query_results["metadatas"][0])
