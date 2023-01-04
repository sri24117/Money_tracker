from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def healthz(request):
    return Response(data={"status": "ok"})


from rest_framework import viewsets
from .serializers import UserSerializer, TransactionSerializer
from .models import User, Transaction

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer