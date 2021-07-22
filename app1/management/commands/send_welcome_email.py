from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
UserModel = get_user_model()


class Command(BaseCommand):
    help = "Sends an email to the provided addresses."

    def add_arguments(self, parser):
        parser.add_argument('emaillist', type=str)

    def handle(self, *args, **options):
        user = UserModel.objects.all()
        emaillist = []
        for item in user:
            emaillist.append(item.email)
        if (options['emaillist']):
            message = "welcome to our website"
            msg = EmailMultiAlternatives(
                'Registration',
                message,
                'panchalvishal2710@gmail.com',
                [options['emaillist']],
            )
            msg.content_subtype = "html"
            msg.send()
        else:
            raise CommandError('something is wrong')
            
