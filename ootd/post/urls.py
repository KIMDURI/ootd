from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'list_board'),
    path('new/', views.create_board, name = 'create_board'),
    path('update/<int:id>/', views.update_board, name = 'update_board'),
    path('show/<int:id>/', views.show_board, name = 'show_board'),
    path('delete/<int:id>/', views.delete_board, name = 'delete_board'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
