from django.shortcuts import render
from  login_app.models import Poll,Choise

# Create your views here.
poll=Poll.object(qestions__contains="what").first()
choise=Choise(choise_text="dupa", votes=9)
poll.choises.append(choise)
poll.save()
print (poll.question)