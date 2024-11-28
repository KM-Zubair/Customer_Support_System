from dotenv import load_dotenv
import os

def init_api():
    """
    Loads environment variables from the `.env` file.
    """
    load_dotenv()
    # Ensure OpenAI API key is set
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
