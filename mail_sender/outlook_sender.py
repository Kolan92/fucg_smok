import win32com.client as win32

class OutlookSender:
    
    def send_email(self, to: str, subject: str, body: str):
        print('Sending email to:{}\nsubject:{}\nbody:\n{}'.format(to, subject, body))
        
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = to
        mail.Subject = subject
        mail.Body = body

        mail.Send()
        print('Successfully sended an email')
