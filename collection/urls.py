from django.urls import path
from . import views

urlpatterns = [
    path('', views.collections, name="collections"),
   path('<int:pk>/', views.CollectionDetailView.as_view(), name="collection_detail")
]
