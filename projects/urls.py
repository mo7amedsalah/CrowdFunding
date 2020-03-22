from django.urls import path
from projects import views
urlpatterns = [
    path('',views.index, name="projects.all"),
    path('<int:project_id>',views.show, name="projects.show"),
    path('create',views.create, name="projects.create"),
]
