from flask import Flask, request, jsonify, render_template
from textsummarizer import *
from ocr import *

app = Flask(__name__)

# verbose:off code
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def home():
    return render_template('index.html', passage = '')

@app.route('/summarize',methods=['POST'])
def summarize():
    
    if request.method == 'POST':
        
        text = request.form['originalText']
        if not request.form['numOfLines']:
            numOfLines = 3
        else:
            numOfLines = int(request.form['numOfLines'])
            
        summary, original_length = generate_summary(text, numOfLines)
        
        return render_template('result.html',
                               text_summary = summary,
                               lines_original = original_length,
                               lines_summary = numOfLines)
@app.route('/extract')
def extract():
    name = request.cookies.get('name');
    extpassage, conf = extractpassage('C:/Users/Midan/Major Project/test-images/' + name);
    return render_template('index.html', passage = extpassage);

    
    
if __name__ == '__main__':
    app.run(debug=True)