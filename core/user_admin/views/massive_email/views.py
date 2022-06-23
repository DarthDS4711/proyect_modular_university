from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from django.conf import settings
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from core.classes.obtain_color import ObtainColorMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from django.template.loader import render_to_string
import threading
from core.user.models import User
from django.contrib.auth.models import Group



class MassiveEmailView(LoginRequiredMixin, ValidateSessionGroupMixin, TemplateView, ObtainColorMixin):
    template_name = 'massiveEmail.html'

    # función que en base del tipo de correo, filtra los usuarios a los cuales
    # se les envia el correo
    def __define_type_user(self, type_send):
        match type_send:
            case 'inactive':
                return User.objects.filter(is_active = False)
            case 'active':
                return User.objects.filter(is_active = True)
            case 'admin':
                admin_group = Group.objects.get(name = 'Administrator')
                return User.objects.filter(groups__name = admin_group.name)
    
    # función que nos regresa el template renderizado a string dependiendo
    # del tipo de correo a mandar
    def __define_type_user_email(self, type_send, user):
        match type_send:
            case 'inactive':
                return render_to_string('massive_email/userActive.html', {
                    'username': user.username,
                    'title': 'Felicitaciones',
                })
            case 'active':
                return render_to_string('massive_email/userInactive.html', {
                    'username': user.username,
                    'title': 'Advertencia',
                })
            case 'admin':
                return render_to_string('massive_email/userAdmin.html', {
                    'username': user.username,
                    'title': 'Aviso',
                })

    def send_email_users(self, type_send):
        try:
            mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            mailServer.ehlo()
            mailServer.starttls()
            mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            users = self.__define_type_user(type_send)
            for user in users:
                email_to = user.email
                mensaje = MIMEMultipart()
                mensaje['From'] = settings.EMAIL_HOST_USER
                mensaje['To'] = email_to
                mensaje['Subject'] = 'Notificacion'
                content = self.__define_type_user_email(type_send, user)
                mensaje.attach(MIMEText(content, 'html'))
                mailServer.sendmail(settings.EMAIL_HOST_USER, email_to, mensaje.as_string())
            mailServer.quit()
        except Exception as e:
            print(str(e))
    
    # sobreescitura del método get, para el envio de correos masivos
    def get(self, request, *args, **kwargs):
        type_send = self.kwargs['type'] if 'type' in self.kwargs else ''
        thread = threading.Thread(target=self.send_email_active_user, args=(type_send))
        thread.start()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Correo masivo"
        context['color'] = self.get_number_color()
        return context
    
