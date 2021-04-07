from whatsapp.whatsapp_client import WhatsappWebController

PATH = r'C:\Users\devsh\Desktop\whatsapp_bot_client\driver\chromedriver_win32\chromedriver.exe'

wp = WhatsappWebController(PATH)
wp.open_whatsapp_web(sleep_time=30)


contact_name = 'Abdul'

error_status, chat_list = wp.read_entire_chat(contact_name)

print('\n\n{}\n\n'.format(error_status))

for i in range(0, len(chat_list)):
    print('{}   --->    {}'.format(i, chat_list[i]))