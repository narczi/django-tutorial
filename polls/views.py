#django-tutorial
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Question

#DRF
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from .permissions import PRI_DjangoModelPermissions
from rest_framework.settings import api_settings


#django-tutorial
def index(request):
    print(api_settings.DEFAULT_AUTHENTICATION_CLASSES)
    return HttpResponse("<html><body>%(app_label)</body></html>")


def detail(request, question_id):
    q = Question.objects.get(id=question_id)
    return HttpResponse("Pytanie %s. %s" % (question_id, q.question_text))

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


#DRF

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [PRI_DjangoModelPermissions]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [PRI_DjangoModelPermissions]