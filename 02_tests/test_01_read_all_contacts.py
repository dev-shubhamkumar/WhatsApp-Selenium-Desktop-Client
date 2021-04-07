from whatsapp.whatsapp_client import WhatsappWebController

PATH = r'C:\Users\devsh\Desktop\whatsapp_bot_client\driver\chromedriver_win32\chromedriver.exe'

wp = WhatsappWebController(PATH)
wp.open_whatsapp_web(sleep_time=30)

final_contact_list, name_of_contacts = wp.get_all_contacts(
    expected_contacts = 86
)


for contact in range(0, len(final_contact_list)):
    print('{}   ---->   {}\n'.format(contact, final_contact_list[contact]))


print('\n\nThe name of all contacts are...\n\n')
for i in name_of_contacts:
    print('\n{}\n'.format(i))


print('\n\n ######### TEST PASS ######### \n\n')