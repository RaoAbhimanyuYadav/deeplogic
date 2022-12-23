# INSTALLATION STEPS

1. Create a virtual environment for installing following dependencies

   - python -m venv env

2. Install following packages using pip

   - pip install django
   - pip install psycopg2-binary
   - pip install pillow
   - pip install pytesseract
   - pip install pdf2image

3. Install this software in your system
   - sudo apt-get install tesseract-ocr

Documentation

Approach
Firstly I have to connect my django app with Postgresql.
then i started out finding for a library that can convert pdf to text then i understand they work with typed character now i have started finding library that uses OCR for conversion.
Now i have my basic functional app now I added authorization
Now a basic working app is ready
Now i started modifing app in such a way that it can fullfill the instruction
Finally working is fine. Now i started working on styling

Challenges faced
installation and intial set up for postgresql and pgadmin4
finding out better library for converting images to text using OCR

Learned from assignment
POSTGRES
pdf/jpeg/png to text using OCR

Link
