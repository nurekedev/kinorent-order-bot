import os
from dotenv import load_dotenv

load_dotenv()

settings = {
    'TOKEN': os.getenv('TELEGRAM_TOKEN'),
    'TELEGRAM_MANAGERS': os.getenv('TELEGRAM_GROUP_ID'),
    'TEST_MANAGERS': os.getenv('TELEGRAM_GROUP_ID_TEST'),
    'USER_PATH': os.getenv('MAIN_PATH'),
    'PROJECT_PATH': os.getenv('SECONDARY_PATH')
}
