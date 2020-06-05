from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artist/', views.artist, name='artist'),
    path('place/', views.place, name='place'),
    path('museum/', views.museum, name='museum'),
    path('artmovement/', views.art_movement, name='art_movement'),

    path('artifact/', views.artifact, name='artifact'),
    path("signup/", views.sign_up, name='sign_up'),
    path('anmelden/', views.login, name='login'),
    path('<str:name>/works/', views.works, name='works'),
    path('logout/', views.logout_view, name='logout'),
    path('aut/', views.auth, name='auth'),
    path('<str:name>/museum_artifacts/', views.museum_artifacts, name='museum_artifacts'),
    path('<str:title>/details/', views.details, name='details'),
    path('user/', views.user_view, name='user_view'),
    path('useredit/', views.user_edit, name='user_edit'),

    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('<str:model>/create/', views.create, name='create'),
    path('<str:model>/update/', views.update, name='update'),


]