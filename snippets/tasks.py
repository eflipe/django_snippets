from django_snippets.celery import app
from django.core.mail import send_mail


@app.task
def enviar_mail(asunto, contenido, destinatario):
    send_mail(asunto, contenido, 'noreply@mail.com', [destinatario], fail_silently=False)
