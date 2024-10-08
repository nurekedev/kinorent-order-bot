import os
from dotenv import load_dotenv

load_dotenv()

settings = {
    'TOKEN': os.getenv('TELEGRAM_TOKEN'),
    'TELEGRAM_MANAGERS': os.getenv('TELEGRAM_GROUP_ID'),
    'TEST_MANAGERS': os.getenv('TELEGRAM_GROUP_ID_TEST'),
    'USER_PATH': '/app',
    'PROJECT_PATH': os.getenv('SECONDARY_PATH'),
    'OPENAI_TOKEN': os.getenv('OPENAI_API_KEY')
}
