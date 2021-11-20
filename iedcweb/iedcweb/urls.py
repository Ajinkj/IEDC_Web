"""iedcweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web import views
from django.conf import settings
from django.conf.urls.static import static
from web.models import events


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('view', views.iedc, name='iedc'),
    path('view/Gallery',views.gallery, name='gallery'),
    path('view/detail/IEDC-JECC', views.detail, name='detail'),
    path('view/Events/<int:id>', views.event, name='event'),
    path('view/Events/all', views.all_events, name='events'),
    path('view/detail/IEDC-JECC/Images/<int:id>', views.image, name='image'),
    path('view/detail/IEDC-JECC/Event_Images/<int:id>', views.event_image, name='event_image')
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

