import PyPDF2
from flask import Flask, request, jsonify
from flasgger import Swagger
import PyPDF2 
import os
import RAKE
import textract
import docx2txt



app = Flask(__name__)
swagger = Swagger(app)
port = int(os.environ.get("PORT", 5000))

# r = Rake(max_length=3) # Uses stopwords for english from NLTK, and all puntuation characters.


@app.route('/')
def lading_page():

	return "Go to https://kewpyp.herokuapp.com/apidocs"

@app.route('/predict_pdf_file', methods=["POST"])
def read_file_pdf():
	"""pdf files
	---
	parameters:
	  - name: input_file
	    in: formData
	    type: file
	    required: true
	responses:
	    200:
	    	description: Output
	"""
	pdfReader = PyPDF2.PdfFileReader(request.files.get("input_file"))
	text = ""

	for page in range(pdfReader.numPages):
		text = text + pdfReader.getPage(page).extractText()

	# r.extract_keywords_from_text(text)
	# print(r.get_ranked_phrases_with_scores())
	
	stop_dir = "stopwordlist.txt"
	rake = RAKE.Rake(stop_dir) #takes stopwords as list of strings

	output = rake.run(text, minCharacters = 3, maxWords = 3, minFrequency = 1)
	return str(output)

@app.route('/predict_doc_file', methods=["POST"])
def read_file_doc():
	""".doc/.docx files
	---
	parameters:
	  - name: input_file
	    in: formData
	    type: file
	    required: true
	responses:
	    200:
	    	description: Output
	"""
	# text = textract.process(request.files.get("input_file"))

	text = docx2txt.process(request.files.get("input_file"))	

	stop_dir = "stopwordlist.txt"
	rake = RAKE.Rake(stop_dir) #takes stopwords as list of strings

	output = rake.run(text, minCharacters = 3, maxWords = 3, minFrequency = 1)
	return str(output)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port)