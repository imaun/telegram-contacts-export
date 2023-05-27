import os, logging
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon import functions, types
import csv

load_dotenv()

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def save_to_csv(contacts):
    with open('contacts.csv', 'w') as file:
        writer = csv.writer(file, delimiter=',')
        cols = ['FirstName', 'LastName', 'Phone']
        writer.writerow(cols)
        for x in enumerate(contacts):
            writer.writerow([x.first_name, x.last_name if x.last_name else '', x.phone])
        print('exported to contacts.csv file successfully.')


required_configs = ['TELEGRAM_API_ID', 'TELEGRAM_API_HASH']
missing_configs = [value for value in required_configs if os.environ.get(value) is None]
if len(missing_configs) > 0:
    logging.error(f'Error: missing config values. {",".join(missing_configs)}')
    exit(1)

TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID')
TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')
session_name = 'imun_export_contacts'

with TelegramClient(session_name, TELEGRAM_API_ID, TELEGRAM_API_HASH) as telegram:
    telegram.connect()

    with telegram.takeout(contacts=True) as takeout:
        contacts = takeout(functions.contacts.GetSavedRequest())
        for x in enumerate(contacts):
            print(f'{x.first_name} {x.last_name} - {x.phone}')
        save_to_csv(contacts)
        print('Goodbye!')