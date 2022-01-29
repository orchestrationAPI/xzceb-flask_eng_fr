from machinetranslation import translator
from flask import Flask, render_template, request
import json

from machinetranslation.translator import english_to_french, french_to_english

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    trans_text_to_french = english_to_french(textToTranslate)
    return trans_text_to_french

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    trans_text_to_english = french_to_english(textToTranslate)
    return trans_text_to_english

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')
  

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
