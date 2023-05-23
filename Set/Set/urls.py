from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    #path('auth/password/reset/', djoser_views.PasswordResetView.as_view(), name='password_reset'),
    #path('auth/password/reset/confirm/', djoser_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('auth/password/reset/complete/', djoser_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
