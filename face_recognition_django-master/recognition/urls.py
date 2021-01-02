from django.urls import path, include
from recognition import views


urlpatterns = [
    path('', views.index, name='index'),
    path('facecam_feed', views.facecam_feed, name='facecam_feed'),
    # path('facecam_data', views.facecam_data, name='facecam_data'),
    ]
