from pywinauto.application import Application
from pywinauto import timings
import pywinauto.keyboard as keyboard


class OutlookRobot:

    def __init__(self, sender: str, addressee: str, subject: str, message: str):
        self.sender = sender
        self.addressee = addressee
        self.subject = subject
        self.message = message

    def launch_outlook(self):
        self.app = Application(backend='uia').start(r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE")
        timings.wait_until(10, 0.5, self.app[f'Inbox — {self.sender} - Outlook'].exists)
        self.dlg = self.app[f'Inbox — {self.sender} - Outlook']

    def send_message(self):
        timings.always_wait_until(10, 0.5, self.dlg['Nowa wiadomość e-mail'].exists)
        self.dlg['Nowa wiadomość e-mail'].Button.click()

        timings.wait_until(10, 0.5, self.app['Bez tytułu - Wiadomość (HTML) '].exists)
        self.snd_dlg = self.app['Bez tytułu - Wiadomość (HTML) ']

        addressee_input = self.snd_dlg['Edit4']
        addressee_input.set_focus()
        keyboard.send_keys(self.addressee, with_spaces=True)

        subject_input = self.snd_dlg['Edit6']
        subject_input.set_focus()
        keyboard.send_keys(self.subject, with_spaces=True)

        message_input = self.snd_dlg['Edit7']
        message_input.set_focus()
        keyboard.send_keys(self.message, with_spaces=True)

        send_button = self.snd_dlg['Wyślij']
        send_button.click()

    def close_outlook(self):
        self.app.kill()

    def run(self):
        self.launch_outlook()
        self.send_message()
        self.close_outlook()


sender = "w.szoltysek@brainhint.com"
recipients = "szoltysek.w@gmail.com; k.szewczyk@brainhint.com"
subject = "Test subject"
message = "Test message."

robot = OutlookRobot(sender, recipients, subject, message)
robot.run()
