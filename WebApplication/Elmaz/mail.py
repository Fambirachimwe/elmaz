import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Elmaz.settings')
import django
django.setup()
from django.core.mail import send_mail

DEFAULT_TO = 'info@elmaztechnologies.co.zw'

send_mail(
    'another',
    'Testing.',
    't.svaku@gmail.com',
    [DEFAULT_TO],

    fail_silently=False,
)





