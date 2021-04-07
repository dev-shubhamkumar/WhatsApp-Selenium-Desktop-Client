import pandas as pd
import numpy as np

from whatsapp.whatsapp_client import WhatsappWebController
from database.db import Database

## Initializing WhatsappWebController
PATH = r'C:\Users\devsh\Desktop\whatsapp_bot_client\driver\chromedriver_win32\chromedriver.exe'

wp = WhatsappWebController(PATH)
wp.open_whatsapp_web(sleep_time=30)

## Initializing Database
db = Database(
    user_table_loctaion= r'database/data/user_table.csv',
    user_action_table_loctaion = r'database/data/user_action_table.csv',
    user_chat_table_loctaion = r'database/data/user_chat_table.csv'
)

