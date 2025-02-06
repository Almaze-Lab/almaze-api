from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
env_path = Path(__file__).parent / '.env'
load_dotenv(env_path)

# Server configuration
PORT = int(os.getenv('PORT', 8000))

# OpenAI configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
SERPER_API_KEY = os.getenv('SERPER_API_KEY')
if not SERPER_API_KEY:

# Configure default language model
    model="gpt-4-turbo-preview",
    temperature=0
)
# Logging configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')