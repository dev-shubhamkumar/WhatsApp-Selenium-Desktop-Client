from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions
import time
import win32com.client


class WhatsappWebController:

    contact_search_box_xpath = '/html/body/div/div/div/div[3]/div/div[1]/div/label/div/div[2]'
    message_box_xpath = '/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]'
    contact_heading_xpath = '/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[1]/div/span'
    chat_start_xpath = '/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div/div[2]/div[2]/div/div/div/span/span'
    chat_start_text = 'Messages are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them. Click to learn more.'
    contact_list_iterator = 200
    chat_read_iterator = 400


    def __init__(self, PATH):
        self.driver = webdriver.Chrome(PATH)

    
    def open_whatsapp_web(self, sleep_time):
        self.driver.get("https://web.whatsapp.com/")

        print('\n\nThe code execution has been put on hold for "{}" seconds, as per your request...\n\n'.format(sleep_time))
        time.sleep(sleep_time)
        print('The sleep/hold has ended after "{}" seconds!!!\n\n'.format(sleep_time))

    

    def check_if_contact_selected(self, contact_name, contact_heading_xpath=contact_heading_xpath):
        status = { 'on_contact_page': None ,'contact_name' : 'not_assigned'}

        try:
            heading = self.driver.find_element_by_xpath(contact_heading_xpath)
            status = {
                'on_contact_page': True,
                'contact_name': heading.text
            }
        except:
            status = {
                'on_contact_page': False,
                'contact_name' : 'not_assigned'
            }
        
        return status


    def select_contact_on_page(self, contact_name):
        contact = self.driver.find_element_by_xpath('//span[@title="{}"]'.format(contact_name))
        contact.click()

        time.sleep(2)
        status = self.check_if_contact_selected(contact_name)
        if status['contact_name'] == contact_name:
            return {
                'desired_contact_selected': True, 
                'on_contact_page': status['on_contact_page'],
                'contact_name': status['contact_name']
            }
        else:
            return {
                'desired_contact_selected': False, 
                'on_contact_page': status['on_contact_page'],
                'contact_name': status['contact_name']
            }


    def select_contact_by_search_box(self, contact_name, contact_search_box_xpath=contact_search_box_xpath):
        search_box = self.driver.find_element_by_xpath(contact_search_box_xpath)
        search_box.click()
        search_box.send_keys("{}".format(contact_name))
        time.sleep(5)
        search_box.send_keys(Keys.RETURN)

        time.sleep(5)
        status = self.check_if_contact_selected(contact_name)
        if status['contact_name'] == contact_name:
            return {
                'desired_contact_selected': True, 
                'on_contact_page': status['on_contact_page'],
                'contact_name': status['contact_name']
            }
        else:
            return {
                'desired_contact_selected': False, 
                'on_contact_page': status['on_contact_page'],
                'contact_name': status['contact_name']
            }
    

    def send_message(self, message, message_box_xpath=message_box_xpath):
        status = {'message_sent': None, 'message': None}
        try:
            text_input = self.driver.find_element_by_xpath(message_box_xpath)
            text_input.send_keys("{}".format(message))
            message_typed_text = text_input.text
            text_input.send_keys(Keys.RETURN)

            status = {'message_sent': True, 'message': message_typed_text}
        except:
            status = {'message_sent': False, 'message': None}

        return status
    

    def read_chat_on_page(self, user_name, chat_read_iterator=chat_read_iterator, 
                            contact_search_box_xpath=contact_search_box_xpath):  
        user = self.select_contact_by_search_box(user_name)

        if user['desired_contact_selected'] == False:
            return {'error_status': 'contact_not_selected'}, []

        time.sleep(5)

        chats = []
        # print(chats,'\n\n')
        for j in [2, 3]:
            for i in range(0, chat_read_iterator):
                msg_xpath = '/html/body/div/div/div/div[4]/div/div[3]/div/div/div[{}]/div[{}]/div/div/div/div[1]/div/span[1]/span'.format(j, i)
                time_stamp_xpath = '/html/body/div/div/div/div[4]/div/div[3]/div/div/div[{}]/div[{}]/div/div/div/div[2]/div/span'.format(j, i)
                msg_status_check_xpath = '/html/body/div/div/div/div[4]/div/div[3]/div/div/div[{}]/div[{}]/div/div/div/div[2]/div/div'.format(j, i)
                try:
                    # print(i)
                    
                    msg = self.driver.find_element_by_xpath(msg_xpath).text
                    time_stamp = self.driver.find_element_by_xpath(time_stamp_xpath).text
                    message_status = 'to_be_assined'

                    try:
                        # print('--->  ', i)
                        status_check = self.driver.find_elements_by_xpath(msg_status_check_xpath)
                        len_of_output = len(status_check)
                        if len_of_output >= 1:
                            message_status = 'sent'
                        else:
                            message_status = 'recieved'
                    except:
                        message_status = 'error_while_assignig_status'

                    msg_dict = {'message': msg, 'time_stamp': time_stamp, 'status': message_status}
                    chats.append(msg_dict)
                    # print(chats)
                except:
                    continue
                
        # print(chats,'\n\n')
        return {'error_status': 'no_error'}, chats
    

    def read_chat_on_page_raw(self, user_name, chat_read_iterator=chat_read_iterator):  
        try:
            time.sleep(5)

            chats = []
            # print(chats,'\n\n')
            for j in [2, 3]:
                for i in range(0, chat_read_iterator):
                    msg_xpath = '/html/body/div/div/div/div[4]/div/div[3]/div/div/div[{}]/div[{}]/div/div/div/div[1]/div/span[1]/span'.format(j, i)
                    time_stamp_xpath = '/html/body/div/div/div/div[4]/div/div[3]/div/div/div[{}]/div[{}]/div/div/div/div[2]/div/span'.format(j, i)
                    msg_status_check_xpath = '/html/body/div/div/div/div[4]/div/div[3]/div/div/div[{}]/div[{}]/div/div/div/div[2]/div/div'.format(j, i)
                    try:
                        # print(i)
                        
                        msg = self.driver.find_element_by_xpath(msg_xpath).text
                        time_stamp = self.driver.find_element_by_xpath(time_stamp_xpath).text
                        message_status = 'to_be_assined'

                        try:
                            # print('--->  ', i)
                            status_check = self.driver.find_elements_by_xpath(msg_status_check_xpath)
                            len_of_output = len(status_check)
                            if len_of_output >= 1:
                                message_status = 'sent'
                            else:
                                message_status = 'recieved'
                        except:
                            message_status = 'error_while_assignig_status'

                        msg_dict = {'message': msg, 'time_stamp': time_stamp, 'status': message_status}
                        chats.append(msg_dict)
                        # print(chats)
                    except:
                        continue
                    
            # print(chats,'\n\n')
            error_status, chat_list = {'error_status': 'no_error'}, chats
        except:
            error_status, chat_list = {'error_status': 'unable_to_read_chat'}, []
        
        return error_status, chat_list
    

    def read_entire_chat(self, user_name, chat_start_xpath=chat_start_xpath, chat_read_iterator=chat_read_iterator,
                        chat_start_text=chat_start_text, message_box_xpath=message_box_xpath, 
                        contact_search_box_xpath=contact_search_box_xpath):
        user = self.select_contact_by_search_box(user_name)

        if user['desired_contact_selected'] == False:
            return {'error_status': 'contact_not_selected'}, []
        
        message_box = self.driver.find_element_by_xpath(message_box_xpath)
        message_box.click()
        message_box.send_keys(Keys.TAB)
        windowsShell = win32com.client.Dispatch("WScript.Shell")

        break_loop = False

        while break_loop == False:
            for i in range(0, 10):
                windowsShell.SendKeys("{UP}")
            try:
                chat_start = self.driver.find_element_by_xpath(chat_start_xpath)
                if chat_start.text == chat_start_text:
                    break_loop = True
                else:
                    continue
            except:
                continue
        
        error_status, chat_list = self.read_chat_on_page_raw(user_name)
        return error_status, chat_list
        

    def get_on_page_contact_list(self, contact_list_iterator=contact_list_iterator):
        all_contacts = []
        
        for i in range(0, contact_list_iterator):
            try:
                try:
                    name_xpath = '/html/body/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[{}]/div/div/div[2]/div[1]/div[1]/span/span'.format(i)
                    time_xpath = '/html/body/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[{}]/div/div/div[2]/div[1]/div[2]'.format(i)
                    unread_status_xpath = '/html/body/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[{}]/div/div/div[2]/div[2]/div[2]/span[1]/div/span'.format(i)
                    name = self.driver.find_element_by_xpath(name_xpath)
                    time_stamp = self.driver.find_element_by_xpath(time_xpath)

                    unread_status = 'not_assigned'
                    try:
                        unread_status_len = self.driver.find_elements_by_xpath(unread_status_xpath)
                        if len(unread_status_len) >= 1:
                            unread_status = 'unread'
                        else:
                            unread_status = 'all_read'
                    except:
                        unread_status = 'an_error_occured_while_geting_unread_status'
                    

                    user_chat = {
                        'name': name.text, 
                        'chat_type': 'individual', 
                        'last_updated_time': time_stamp.text, 
                        'unread_status': unread_status
                    }
                    all_contacts.append(user_chat)
                    
                except:
                    name_xpath = '/html/body/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[{}]/div/div/div[2]/div[1]/div[1]/span'.format(i)
                    time_xpath = '/html/body/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[{}]/div/div/div[2]/div[1]/div[2]'.format(i)
                    unread_status_xpath = '/html/body/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[{}]/div/div/div[2]/div[2]/div[2]/span[1]/div/span'.format(i)
                    name = self.driver.find_element_by_xpath(name_xpath)
                    time_stamp = self.driver.find_element_by_xpath(time_xpath)

                    unread_status = 'not_assigned'
                    try:
                        unread_status_len = self.driver.find_elements_by_xpath(unread_status_xpath)
                        if len(unread_status_len) >= 1:
                            unread_status = 'unread'
                        else:
                            unread_status = 'all_read'
                    except:
                        unread_status = 'an_error_occured_while_geting_unread_status'
                    

                    user_chat = {
                        'name': name.text, 
                        'chat_type': 'group', 
                        'last_updated_time': time_stamp.text, 
                        'unread_status': unread_status
                    }
                    all_contacts.append(user_chat)
                    
            except:
                continue

        return all_contacts
    

    def get_all_contacts(self, expected_contacts, contact_search_box_xpath=contact_search_box_xpath,
                        contact_list_iterator=contact_list_iterator):
        time.sleep(2)

        given_length = int(int(expected_contacts)/10)
        search_box_xpath = contact_search_box_xpath
        search_box = self.driver.find_element_by_xpath(search_box_xpath)

        all_contacts = []

        for scroll in range(0, given_length):
            time.sleep(3)
            contacts = self.get_on_page_contact_list(contact_list_iterator=contact_list_iterator)
            all_contacts.extend(contacts)

            time.sleep(3)
            search_box.click()
            search_box.send_keys(Keys.TAB)
            windowsShell = win32com.client.Dispatch("WScript.Shell")

            for i in range(0, 10):
                #time.sleep(0.5)
                windowsShell.SendKeys("{DOWN}")
        
        dummy = []
        final_contact_list = []

        for i in all_contacts:
            name = i['name']
            if name in dummy:
                pass
            elif name not in dummy:
                dummy.append(name)
                final_contact_list.append(i)
        
        name_of_contacts = dummy

        return final_contact_list, name_of_contacts
