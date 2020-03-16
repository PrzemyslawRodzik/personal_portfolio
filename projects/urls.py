

from django.urls import path
from projects import views


urlpatterns = [
    #path('dodaj/', views.dodaj_bazy_view),
    path('', views.project_index, name='project_index'),
    path('<int:id>/', views.project_detail, name='project_detail')
]
