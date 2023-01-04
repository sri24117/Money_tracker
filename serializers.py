
from rest_framework import serializers
from .models import Transaction, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class TransactionSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Transaction
        fields = ['id', 'users', 'category', 'amount']