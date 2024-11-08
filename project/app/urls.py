from django.urls import path
from .views import AuthorCreateView, AuthorDeleteView, AuthorListView, AuthorUpdateView  
from .views import VideoGameListView, VideoGameCreateView,  VideoGameDeleteView, VideoGameUpdateView

urlpatterns = [
    # URLs para AuthorModel
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/create/', AuthorCreateView.as_view(), name='author-create'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
    path('authors/<int:pk>/update/', AuthorUpdateView.as_view(), name='author-update'),

    # URLs para VideoGameModel
    path('videogames/', VideoGameListView.as_view(), name='videogame-list'),
    path('videogames/create/', VideoGameCreateView.as_view(), name='videogame-create'),
    path('videogames/<int:pk>/update/', VideoGameUpdateView.as_view(), name='videogame-update'),
    path('videogames/<int:pk>/delete/', VideoGameDeleteView.as_view(), name='videogame-delete'),
 ]
