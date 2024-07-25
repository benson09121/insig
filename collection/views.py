from typing import Any
from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.reverse import reverse
from django.views.generic import DetailView
from .models import CollectionTitles, Type, Genre, TitleEntry, EntryText, Features
from .serializers import CollectionTitlesSerializer, TypeSerializer, GenreSerializer, EntrySeriializer

def collections(request):
    """ To Show the collection of page"""
    if not request.user.is_authenticated:
        return redirect('home')
    types = Type.objects.all()
    genres = Genre.objects.all()
    return render(request, 'collection/collections.html',{"genres" : genres, "types" : types})

class CollectionDetailView(LoginRequiredMixin, DetailView):
    model = CollectionTitles
    template_name = 'collection/collection_detail.html'
    login_url = 'login_signup'
    context_object_name = 'collection'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class CollectionViewSet(ModelViewSet):
    queryset = CollectionTitles.objects.all()
    serializer_class = CollectionTitlesSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user.id)
    

    def create(self, request, *args, **kwargs):
        data = request.data
        data._mutable = True
        data['user'] = request.user.id
        data._mutable = False
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)    
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
class TypeViewset(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    def get_queryset(self):
        return super().get_queryset()
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
class GenreViewset(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_queryset(self):
        return super().get_queryset()

class EntryViewset(ModelViewSet):
    queryset = TitleEntry.objects.all()
    serializer_class = EntrySeriializer

    def get_queryset(self):
        return super().get_queryset().filter(title__user=self.request.user.id)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        data._mutable = True
        text_scanned = data.pop('text_scanned')
        text_generated = data.pop('text_generated')
        feature = data.pop('feature')
        title = data.pop('title')
        features = Features.objects.get(chosen=feature[0])
        title = CollectionTitles.objects.get(id=title[0])
        entry_data = { 
            'text_scanned' : text_scanned[0], 
            'text_generated' :text_generated[0],
            'feature' : features,
                      }
        text = EntryText.objects.create(**entry_data)
        data['text'] = text
        data['title'] = title
        data['image_text'] = ''
        print(data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)