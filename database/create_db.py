import pandas as pd
import numpy as np


user_table_df = pd.DataFrame(columns=[
    'contact_name',
    'chat_type',
    'created_date',
    'last_updated',
    'frizza_number'
])


user_action_table_df = pd.DataFrame(columns=[
    'uid',
    'contact_name',
    'update_time',
    'event_name',
    'user_query_type',
    'phase1_problem_type',
    'admin_note'
])


user_chat_table_df = pd.DataFrame(columns=[
    'uid',
    'contact_name',
    'message',
    'time_stamp',
    'status',
    'multimedia_msg'
])



## Creating the csv
user_table_df.to_csv(r'data/user_table.csv', index=True)
user_action_table_df.to_csv(r'data/user_action_table.csv', index=True)
user_chat_table_df.to_csv(r'data/user_chat_table.csv', index=True)
