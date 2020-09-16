import json
from pywinauto.application import Application
from pywinauto import timings
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
import time

# with open("movies.json", "r") as input_file:
#     file = json.load(input_file)
# print(file)

app = Application(backend='uia').start(r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE")

timings.wait_until(10, 0.5, app['Inbox — w.szoltysek@brainhint.com - Outlook'].exists)
dlg = app['Inbox — w.szoltysek@brainhint.com - Outlook']
# dlg.print_control_identifiers()

# timings.wait_until(10, 0.5, dlg['Nowa wiadomość e-mail'].exists)
# dlg['Nowa wiadomość e-mail'].Button.click()

timings.always_wait_until(10, 0.5, dlg['Nowa wiadomość e-mail'].exists)
dlg['Nowa wiadomość e-mail'].Button.click()

# time.sleep(2)
# print(app.windows())

timings.wait_until(10, 0.5, app['Bez tytułu - Wiadomość (HTML) '].exists)
snd_dlg = app['Bez tytułu - Wiadomość (HTML) ']
# snd_dlg.print_control_identifiers()

addressee = snd_dlg['Edit4']
addressee.set_focus()
keyboard.send_keys("szoltysek.w@gmail.com")

subject = snd_dlg['Edit6']
subject.set_focus()
keyboard.send_keys("Trudne sprawy", with_spaces=True)

message = snd_dlg['Edit7']
message.set_focus()
keyboard.send_keys("Kasi ciasto jest lepsze niz twoje.", with_spaces=True)

send_button = snd_dlg['Wyślij']
send_button.click()
