from email.mime.multipart import MIMEMultipart
import smtplib
import uuid
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import FormView
from django.urls import reverse_lazy
from core.access_system.forms.form_reset_pwd import UserResetPwdForm
from core.classes.obtain_color import ObtainColorMixin
from core.user.models import User
from django.template.loader import render_to_string
from email.mime.text import MIMEText




class ResetPasswordEmailiew(FormView, ObtainColorMixin):
    template_name = 'reset_password_email.html'
    form_class = UserResetPwdForm
    success_url = reverse_lazy('app_views:homepage')


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    # método que envia un correo electrónico a la persona para reestablecer la contraseña
    def send_email(self, user:User):
        user = user[0]
        URL = settings.DOMAIN if not settings.DEBUG else self.request.META['HTTP_HOST']
        user.token = uuid.uuid4()
        user.save()

        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        mailServer.starttls()
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

        email_to = user.email
        mensaje = MIMEMultipart()
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = 'Reseteo de contraseña'

        content = render_to_string('template_email_pass.html', {
            'user': user,
            'link_resetpwd': 'http://{}/access/change-password/{}/'.format(URL, str(user.token)),
            'link_home': 'http://{}'.format(URL)
        })
        mensaje.attach(MIMEText(content, 'html'))

        mailServer.sendmail(settings.EMAIL_HOST_USER, email_to, mensaje.as_string())


    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        data = {}
        user = User.objects.filter(username = username)
        if user.exists():
            try:
                self.send_email(user)
                data['success'] = self.success_url
            except Exception as e:
                data['error'] = str(e)
        else:
            data['error'] = 'Usuario no válido'
        return JsonResponse(data, safe=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "¿Olvidaste tu contraseña?"
        context['color'] = self.get_number_color()
        return context
    
