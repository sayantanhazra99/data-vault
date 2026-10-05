from django.urls import path
from . import views

urlpatterns =[
    path("upload/", views.upload_dataset, name="upload_dataset"),
    path("datasets/", views.dataset_list, name="dataset_list"),
    path("datasets/<int:dataset_id>/", views.dataset_detail, name="dataset_detail"),
    path("datasets/<int:dataset_id>/delete/", views.delete_dataset, name="delete_dataset"),
]
