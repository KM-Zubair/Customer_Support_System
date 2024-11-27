import os

def init_api():
    """
    Load API credentials from a `.env` file and set them as environment variables.
    """
    with open(".env") as env_file:
        for line in env_file:
            key, value = line.strip().split("=")
            os.environ[key] = value

    os.environ["OPENAI_API_KEY"] = os.environ.get("API_KEY")
    os.environ["OPENAI_ORG_ID"] = os.environ.get("ORG_ID")
