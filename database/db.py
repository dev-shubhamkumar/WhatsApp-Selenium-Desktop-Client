import pandas as pd
import numpy as np


class Database:

    user_table_loctaion = r'database/data/user_table.csv'
    user_action_table_loctaion = r'database/data/user_action_table.csv'
    user_chat_table_loctaion = r'database/data/user_chat_table.csv'

    def __init__(self, user_table_loctaion=user_table_loctaion, 
                user_action_table_loctaion=user_action_table_loctaion,
                user_chat_table_loctaion=user_chat_table_loctaion):
        
        self.user_table = pd.DataFrame(pd.read_csv(user_table_loctaion))
        self.user_action_table = pd.DataFrame(pd.read_csv(user_action_table_loctaion))
        self.user_chat_table = pd.DataFrame(pd.read_csv(user_chat_table_loctaion))
    

    def search_user_by_contact_name(self, contact_name):
        search_instance = None
        try:
            search_instance = self.user_table[self.user_table['contact_name'] == contact_name]
        except:
            search_instance = 'error'
        
        if len(search_instance) == 1:
            return {
                'contact_found': True,
                'uid': search_instance.index[0],
                'contact_name': search_instance['contact_name'][0],
                'chat_type': search_instance['chat_type'][0],
                'created_date': search_instance['created_date'][0],
                'last_updated': search_instance['last_updated'][0],
                'frizza_number': search_instance['frizza_number'][0]
            }
        elif len(search_instance) == 0:
            return {
                'contact_found': False
            }
        else:
            return {
                'contact_found': 'error!!!'
            }
    

    def search_user_by_uid(self, uid):
        search_instance = None
        try:
            search_instance = self.user_table.iloc[uid]
        except:
            search_instance = 'error'

        if len(search_instance) == 1:
            return {
                'contact_found': True,
                'uid': search_instance.index[0],
                'contact_name': search_instance['contact_name'][0],
                'chat_type': search_instance['chat_type'][0],
                'created_date': search_instance['created_date'][0],
                'last_updated': search_instance['last_updated'][0],
                'frizza_number': search_instance['frizza_number'][0]
            }
        elif len(search_instance) == 0:
            return {
                'contact_found': False
            }
        else:
            return {
                'contact_found': 'error!!!'
            }
    

    def insert_user(self, contact_name, chat_type, created_date, last_updated, frizza_number):
        make_instance = {
            'contact_name': contact_name,
            'chat_type': chat_type,
            'created_date': created_date,
            'last_updated': last_updated,
            'frizza_number': frizza_number
        }

        try:
            self.user_table = self.user_table.append(make_instance, ignore_index = True)
            output = {'status': 'user_created'}
        except:
            output = {'status': 'error!!!'}
        
        return output
    

    def update_user_information(self, contact_name, chat_type, created_date, last_updated, frizza_number):

        search_instance = self.search_user_by_contact_name(contact_name)

        if search_instance['contact_found'] == True:

            uid = search_instance['uid']
            self.user_table.at(uid, 'contact_name') = contact_name
            self.user_table.at(uid, 'chat_type') = chat_type
            self.user_table.at(uid, 'created_date') = created_date
            self.user_table.at(uid, 'last_updated') = last_updated
            self.user_table.at(uid, 'frizza_number') = frizza_number

            return {'data_update_status': True, 'data': self.search_user_by_uid(uid)}
        
        elif search_instance['contact_found'] == False:
            return {'data_update_status': False, 'data': 'entered_user_not_found'}

        elif search_instance['contact_found'] == 'error!!!':
            return {'data_update_status': False, 'data': 'an_error_occured'}
        
        else:
            return {'data_update_status': False, 'data': 'UNACCEPTABLE_ERROR'}

    ##----------------------------------------------------------------------------------

    def search_user_action_by_contact_name(self, contact_name):

        search_instance = self.user_action_table[self.user_action_table['contact_name'] == contact_name]
        return search_instance, list(search_instance.index)
    

    def search_user_action_by_uid(self, uid):

        search_instance = self.user_action_table[self.user_action_table['uid'] == uid]
        return search_instance, list(search_instance.index)
    

    def search_user_action_by_table_index(self, index_list):

        search_instance = self.user_action_table.iloc[index_list]
        return search_instance, list(search_instance.index)
    

    def insert_action(self, uid, contact_name, update_time, event_name, user_query_type, 
                        phase1_problem_type, admin_note):
        
        make_instance = {
            'uid': uid,
            'contact_name': contact_name,
            'update_time': update_time,
            'event_name': event_name,
            'user_query_type': user_query_type,
            'phase1_problem_type': phase1_problem_type,
            'admin_note': admin_note
        }

        try:
            self.user_action_table = self.user_action_table.append(make_instance, ignore_index = True)
            output = {'status': 'action_inserted'}
        except:
            output = {'status': 'error!!!'}
        
        return output
    
    ##----------------------------------------------------------------------------------

    def search_chats_by_contact_name(self, contact_name):

        search_instance = self.user_chat_table[self.user_chat_table['contact_name'] == contact_name]
        return search_instance, list(search_instance.index)
    

    def search_chats_by_uid(self, uid):

        search_instance = self.user_chat_table[self.user_chat_table['uid'] == uid]
        return search_instance, list(search_instance.index)
    

    def search_chats_by_table_index(self, index_list):

        search_instance = self.user_chat_table.iloc[index_list]
        return search_instance, list(search_instance.index)
    

    def insert_chat(self, uid, contact_name, message, time_stamp, status, multimedia_msg):

        make_instance = {
            'uid': uid,
            'contact_name': contact_name,
            'message': message,
            'time_stamp': time_stamp,
            'status': status,
            'multimedia_msg': multimedia_msg
        }

        try:
            self.user_chat_table = self.user_chat_table.append(make_instance, ignore_index = True)
            output = {'status': 'action_inserted'}
        except:
            output = {'status': 'error!!!'}
        
        return output