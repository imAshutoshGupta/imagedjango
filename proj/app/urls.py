from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from app.views import FormData


urlpatterns = [
    path('image', views.image),
    path('upload', views.upload),
    path('showimage', views.showimage),
    path('classview',FormData.as_view()),
]

if settings.DEBUG:

    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)