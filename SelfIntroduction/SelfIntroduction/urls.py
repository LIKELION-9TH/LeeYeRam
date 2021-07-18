"""SelfIntroduction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from yeram import views 

urlpatterns = [
    path('scrap/admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('hobby/', views.hobby, name="hobby"),
    path('place/', views.place, name="place"),
    path('music/', views.music, name="music"),
    path('photo/', views.photo, name="photo"),
    path('scrap/', views.scrap, name="scrap"),
    path('scrap/<int:yeram_id>/', views.scrapdetail, name="scrapdetail"),
    path('scrap/scrapnew/', views.scrapnew, name="scrapnew"),
    path('scrap/scrapcreate/', views.scrapcreate, name="scrapcreate"),
    path('scrap/<int:yeram_id>/scrapedit/', views.scrapedit, name="scrapedit"),
    path('scrap/<int:yeram_id>/scrapupdate/ ', views.scrapupdate, name='scrapupdate'),
    path('scrap/<int:yeram_id>/scrapdelete/ ',
         views.scrapdelete, name='scrapdelete'),

]

