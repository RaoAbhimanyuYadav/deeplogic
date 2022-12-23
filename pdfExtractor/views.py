from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import platform
from tempfile import TemporaryDirectory
from pathlib import Path

import pytesseract
from pdf2image import convert_from_path
from PIL import Image

from .forms import UploadFileForm
from .models import Text


@login_required(login_url='login')
def index(request):
    user = request.user
    context = user.text_set.all()
    return render(request, "pdfExtractor/index.html", {'context': context})


@login_required(login_url='login')
def desciption(request, id):
    user = request.user
    context = user.text_set.get(id=id)
    return render(request, 'pdfExtractor/description.html', {'context': context})


@login_required(login_url='login')
def upload_file(request):
    user = request.user
    message = ""
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES["file"]

        if file.content_type == 'application/pdf':
            inst = Text.objects.create(filename=str(file), file=file, owner=user)
            inst.save()

            if platform.system() == "Windows":
                path_to_poppler_exe = Path(r"C:\.....")
                pytesseract.pytesseract.tesseract_cmd = (
                    r"C:\ProgramFiles\Tesseract-OCR\tesseract.exe")

            PDF_file = Path(f"media/pdf/{inst.filename}")
            image_file_list = []

            with TemporaryDirectory() as tempdir:
                if platform.system() == "Windows":
                    pdf_pages = convert_from_path(PDF_file, 500, poppler_path=path_to_poppler_exe)
                else:
                    pdf_pages = convert_from_path(PDF_file, 500)
                for page_enumeration, page in enumerate(pdf_pages, start=1):
                    filename = f"{tempdir}\page_{page_enumeration:03}.jpg"
                    page.save(filename, "JPEG")
                    image_file_list.append(filename)
                ocr_text = ""
                for image_file in image_file_list:
                    text = str(((pytesseract.image_to_string(Image.open(image_file)))))
                    ocr_text += text
                inst.des = ocr_text
                inst.save()
            message = f'{inst.filename} uploaded succesfully'
        elif file.content_type == 'image/jpeg' or 'image/png':
            text = str(((pytesseract.image_to_string(Image.open(file)))))
            inst = Text.objects.create(filename=str(file), file=file, des=text, owner=user)
            inst.save()
            message = f"{inst.filename} uploaded successfully"
        else:
            message = "Please upload JPEG or PNG or PDF file only"
    else:
        form = UploadFileForm()
    context = {"form": form, "message": message}
    return render(request, "pdfExtractor/upload.html", context)
