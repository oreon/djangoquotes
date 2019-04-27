from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import serializers, viewsets, routers
from .models import  *
from rest_framework import permissions, generics
from rest_framework.permissions import IsAuthenticated

class QuoteSerializer(serializers.ModelSerializer):

    link = serializers.CharField(source='get_link', read_only=True)
    permission_classes = (IsAuthenticated,)

    class Meta:
        model = Post
        exclude = ('users_like', 'created', 'updated')
        read_only_fields = ('publish',)



class ArticleSerializer(serializers.ModelSerializer):

    permission_classes = (IsAuthenticated,)
    class Meta:
        model = Article
        fields = '__all__'


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = QuoteSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'quotes', QuoteViewSet)
router.register(r'articles', ArticleViewSet)