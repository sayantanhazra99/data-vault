from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import DatasetUploadForm
from .models import Dataset

def upload_dataset(request:HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = DatasetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DatasetUploadForm()
    return render(request, "vault/upload_dataset.html", {"form": form})

def dataset_list(request: HttpResponse) -> HttpResponse:
    datasets = Dataset.objects.all()
    return render(request, "vault/dataset_list.html", {"datasets": datasets})