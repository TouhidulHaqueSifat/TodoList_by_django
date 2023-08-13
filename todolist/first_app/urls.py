from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.store_task, name = 'store_task'),
    path('show_task/',views.show_task, name = 'show_task'),
    path('edit/<int:id>',views.edit, name = 'edit'),
    path('complete/',views.completed1, name = 'complete1'),
   
    path('show_complete/<int:id>',views.complete, name = 'complete'),
    path('delete/<int:id>',views.delete, name = 'delete')
]