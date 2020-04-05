from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from reservations.serializers import UserSerializer, GroupSerializer, ReservationSerializer
from .models import Reservation

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'reservations/home.html'

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reservations to be viewed or edited.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    #permission_classes = [permissions.IsAuthenticated]
