from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import DatasetUploadForm
from .models import Dataset
import pandas as pd

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

def dataset_detail(request: HttpRequest, dataset_id) ->HttpResponse:
    dataset = Dataset.objects.get(id=dataset_id)
    dataframe = pd.read_csv(dataset.file.path)
    columns = dataframe.columns.tolist()
    records = dataframe.values.tolist()

    context: dict = {
        "dataset": dataset,
        "columns": columns,
        "records": records
    }
    return render(request, "vault/dataset_detail.html", context)

