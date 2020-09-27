from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
#
from .models import *
from .serializers import *

# API View (another approach)
from rest_framework.views import APIView
from rest_framework.response import Response
# post Hello
from rest_framework import status


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

# API View (another approach)


class HelloApiView(APIView):
    """ API View sample by Harvey Triana """

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        beautiful_ladies = [
            "Alexa",
            "Allison",
            "Scarlett",
            "Johana",
            "Glenn"
        ]
        return Response({
            'message': 'API View Approach',
            'beautiful_ladies': beautiful_ladies
        })

    def post(self, request):
        """ Create a message with our name """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
