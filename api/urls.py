from rest_framework.routers import DefaultRouter
from django.urls import path, include
from collection.views import CollectionViewSet, TypeViewset, GenreViewset, EntryViewset
from myapp.views import GeminiViewset
from myapp.views import UserStatOverviewViewSet
from . import views


router = DefaultRouter()

router.register('collection', CollectionViewSet, 'collection')
router.register('type', TypeViewset,'type')
router.register('genre', GenreViewset,'genre')
router.register('entry', EntryViewset, 'entry')
router.register('userstat', UserStatOverviewViewSet, 'userstat')
router.register('gemini', GeminiViewset, 'gemini')

urlpatterns = [
    path('', include(router.urls))
    
]
