from whatsapp.whatsapp_client import WhatsappWebController

PATH = r'C:\Users\devsh\Desktop\whatsapp_bot_client\driver\chromedriver_win32\chromedriver.exe'

wp = WhatsappWebController(PATH)
wp.open_whatsapp_web(sleep_time=30)


contact_name = 'Whatsapp Bot'

select_contact = wp.select_contact_by_search_box(contact_name)

print('\n\n{}\n\n'.format(select_contact))
msg = '''
hi user
what is 
this

'''
send_msg = wp.send_message(msg)

print('\n\n{}\n\n'.format(send_msg))