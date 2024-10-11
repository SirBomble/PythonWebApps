from django.contrib import admin
from django.urls import path, include
from hero.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hero.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
]