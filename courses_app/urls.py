from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('process_course', views.process_course),
    path('courses/destroy_page/<int:course_id>', views.destroy_page),
    path('courses/destroy/<int:course_id>', views.destroy),	   
]