import os
from dotenv import load_dotenv
import pathlib


dotenv_path = pathlib.Path(__file__).joinpath('../', '.env')
load_dotenv(dotenv_path.resolve())

HOSTNAME = os.environ.get('HOSTNAME')
DF_CMD = os.environ.get('DF_CMD')
DISK_INFO_CMD = os.environ.get('DISK_INFO_CMD')
SMART_LIST_CMD = os.environ.get('SMART_LIST_CMD')
SMART_INFO_CMD = os.environ.get('SMART_INFO_CMD')
SMART_TABLE_COLUMN = ['id', 'description', 'value', 'worst_value', 'threshold', 'raw_value', 'status']
TEMPLATE_PATH = os.environ.get('TEMPLATE_PATH')

MAIL_SUBJECT = os.environ.get('MAIL_SUBJECT')
MAIL_INFO = {
    'smtp_server': os.environ.get('SMTP_SERVER'),
    'smtp_port': os.environ.get('SMTP_PORT'),
    'smtp_user': os.environ.get('SMTP_USER'),
    'smtp_pass': os.environ.get('SMTP_PASS'),
    'mail_to': os.environ.get('MAIL_TO')
}

