from django.urls import path, include

from accounts import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('account/<int:pk>/<str:status>', views.AccountView.as_view(), name='account'),
    path('account/favorites/<int:pk>', views.FavoritesView.as_view(), name='favorites'),
]
