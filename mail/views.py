from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from django.http import HttpResponse
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers

# Create your views here.

def email(request):
    notify_customers.delay("Whats Up?")
    return HttpResponse("hi")

# try:
#     message = BaseEmailMessage(
#         template_name="emails/hello.html",
#         context={"name": "Seath"}
#     )
#     file = "mail/static/images/4.jpg"
#     # message = EmailMessage("subject", "message", "from@gmail.com", ["to@gmail.com"])
#     # # send_mail("subject", "message", "john@gmail.com", ["doe@gmail.com"])
#     # # mail_admins("subject", "message", html_message="message")

#     # message.attach_file(file)
#     message.send(["to@gmail.com"])
# except BadHeaderError:
#     pass
