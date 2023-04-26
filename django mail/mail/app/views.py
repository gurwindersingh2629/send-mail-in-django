from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail

def mail(request):
    subject="Greetings"
    msg="kidan bhau ki haal aw"
    to="ranagurwinder0001@gmail.com"
    res=send_mail(subject,msg,settings.EMAIL_HOST_USER, [to])
    if (res==1):
        msg="mail sent successfully"
    else:
        msg="mail could not be sent"
    return HttpResponse(msg)



# Create your views here.
