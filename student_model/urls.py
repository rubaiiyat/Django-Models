
from django.urls import include, path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:roll>',views.delete_student,name='delete_student')
]
