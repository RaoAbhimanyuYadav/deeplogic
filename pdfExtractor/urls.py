
from django.urls import path
from .views import index, upload_file, desciption


urlpatterns = [
    path("", index, name="index"),
    path("file/<str:id>/", desciption, name="description"),
    path("upload/", upload_file, name="upload"),
]
