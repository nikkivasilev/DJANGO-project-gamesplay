from django.urls import path, include

from gamesplay_app.gamesplay.views import index, create_profile, details_profile, edit_profile, delete_profile, \
    dashboard, create_game, details_game, edit_game, delete_game

urlpatterns = (
    path('', index, name='index'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
    path('dashboard/', dashboard, name='dashboard'),
    path('game/', include([
        path('create/', create_game, name='create game'),
        path('details/<int:pk>/', details_game, name='details game'),
        path('edit/<int:pk>/', edit_game, name='edit game'),
        path('delete/<int:pk>/', delete_game, name='delete game'),
    ])),

)
