import tabula

pdf_path = "C:/Users/hide/Dropbox/Python/scrapy-tt-data/downloads/2019-annual-economic-survey_0.pdf"

print(tabula.read_pdf(pdf_path, pages=52, stream=True)[0])
