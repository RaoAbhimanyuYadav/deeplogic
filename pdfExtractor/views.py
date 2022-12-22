from django.shortcuts import render
from django.http import HttpResponse

# from PyPDF2 import PdfReader

from .forms import UploadFileForm
from .models import Text

# reader = PdfReader("example.pdf")
# page = reader.pages[0]
# print(page.extract_text())


def index(request):
    context = Text.objects.all()
    return render(request, "pdfExtractor/index.html", {'context': context})


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES["file"]
        # file = request.FILES.getlist('file')[1]
        # reader = PdfReader(file)
        # page = reader.pages[0]
        # print(page.extract_text())
        # pdf = PDF.objects.create(file=file)
        # pdf.save()
        return HttpResponse(str(file))
    else:
        form = UploadFileForm()
    context = {"form": form}
    return render(request, "pdfExtractor/upload.html", context)
