import kronos


from django.contrib.auth.models import User
from django.template.loader import render_to_string




from .models import  *
from datetime import date, timedelta
from mysite.utils import send_mass_html_mail
from  django.core.mail import send_mass_mail, send_mail


# Register cron job to run once a week (every Sunday) at midnight
#@kronos.register('1 0 * * * *')
@kronos.register('1 0 * * *')
def notify_newcontent():
    """Sets up a cron job and runs this service function once a day.

        Installed With:
           ``./manage.py installtasks``
    """
    users = User.objects.all()
    yesterday = date.today() - timedelta(1)
    changes = Post.objects.filter(publish__gte=yesterday)
    if(changes.count() == 0):return
    msg_html = render_to_string('blog/post/mail.html', {'posts': changes})
    userEmails = list(map(lambda x: x.email, users))  #['first@example.com', 'other@example.com']

    data = ('New Posts on Spiritual Quotes', "text", msg_html, 'from@example.com',userEmails)

    #TODO:  use EmailAlternatives , all mails are visible we need to bcc them
    send_mail('New Posts on Spiritual Quotes'," txt msg ",'from@example.com',userEmails,
              fail_silently=False,html_message=msg_html)
    #send_mass_html_mail(data)
