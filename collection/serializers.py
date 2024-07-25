from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import CollectionTitles, Type, Genre, TitleEntry, EntryText


class CollectionTitlesSerializer(ModelSerializer):
    type_name = serializers.ReadOnlyField(source='type.name')
    genre_name = serializers.ReadOnlyField(source='genre.name')
    class Meta:
        model = CollectionTitles
        fields = ('title', 
                  'author', 
                  'type', 
                  'genre',
                  'user', 
                  'type_name', 
                  'genre_name','id'
                  )

class TypeSerializer(ModelSerializer):
   
    class Meta:
        model = Type
        fields = ('__all__')

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ('__all__')

class EntryTextSerializer(ModelSerializer):
    class Meta:
        model = EntryText
        fields = ('__all__')

class EntrySeriializer(ModelSerializer):
    text_scanned = serializers.ReadOnlyField(source='text.text_scanned')
    text_generated = serializers.ReadOnlyField(source='text.text_generated')
    feature = serializers.ReadOnlyField(source='text.feature')
    
    class Meta:
        model = TitleEntry
        fields = ('title', 
                  'entry_name', 
                  'page', 
                  'text_scanned', 
                  'text_generated', 
                  'feature', 
                  'text', 
                  'image_text',
                  )

