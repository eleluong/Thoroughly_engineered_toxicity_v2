from dotenv import load_dotenv
import os


load_dotenv()


class Settings:
    def __init__(self) -> None:
        self.together_api_key = os.getenv("TOGETHER_API_KEY")
        self.modestus_api_key = os.getenv("MODESTUS_API_KEY")
        self.ct2_encoder_path = os.getenv("CT2_ENCODER_PATH")

        self.seed_model_list = [
            "Qwen/Qwen2.5-7B-Instruct-Turbo",
            "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            "google/gemma-2-9b-it",
            "mistralai/Mistral-7B-Instruct-v0.3",
        ]
        self.chroma_dir = os.getenv("CHROMA_PERSISTENT_DISK")


settings = Settings()
