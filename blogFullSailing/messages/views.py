from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message

# Create your views here.

@login_required
def message_list(request):
    received_messages = request.user.received_messages.all()
    sent_messages = request.user.sent_messages.all()
    return render(request, 'messages/message_list.html', {'received_messages': received_messages, 'sent_messages': sent_messages})
