from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import serializers, viewsets, routers
from .models import  *
from rest_framework import permissions, generics

class QuoteSerializer(serializers.ModelSerializer):

    link  = serializers.CharField(source='get_link', read_only=True)
    class Meta:
        model = Post
        exclude = ('users_like', 'created', 'updated')
        read_only_fields = ('publish',)



class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = QuoteSerializer


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'quotes', QuoteViewSet)