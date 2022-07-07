from django.urls import path
from site_podcast import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'podcasturi'

urlpatterns = [
    path('', views.PodcastView.as_view(), name='listare'),
    path('cautare', views.cautare, name='cautare'),
    path('<int:pk>/displayphoto', views.podcast_detail_view, name='displayphoto'),
    path('categories', views.categories, name='categories'),
]

urlpatterns += staticfiles_urlpatterns()
