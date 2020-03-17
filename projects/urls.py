

from django.urls import path
from projects import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #path('dodaj/', views.dodaj_bazy_view),
    path('', views.project_index, name='project_index'),
    path('<int:id>/', views.project_detail, name='project_detail'),


            # CRUD #

    path('create', views.create_view, name='create_view'),
    path('edit/<int:id>', views.edit_view, name='edit_view'),
    path('update/<int:id>', views.update_view, name='update_view'),
    path('delete/<int:id>', views.destroy_view, name='destroy_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
