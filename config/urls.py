from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('creatures/', include('apps.creatures.urls', namespace='creatures')),
    path('', RedirectView.as_view(pattern_name='creatures:list', permanent=False)),
]
