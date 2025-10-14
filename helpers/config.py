from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()  # loads variables from .env into os.environ
api = os.environ["gemini_API"]

