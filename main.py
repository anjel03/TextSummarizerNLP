from flask import Flask, render_template, request
from text_summary import summarizer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        rawText = request.form['rawText']
        summary, original_text, len_origi, len_summ = summarizer(rawText)
        return render_template('summary.html', summary=summary, orginal_txt=original_text, len_ori_txt=len_origi,
                               len_summ_txt=len_summ)

    return render_template('summary.html', summary="", orginal_txt="", len_ori_txt=0, len_summ_txt=0)


if __name__ == '__main__':
    app.run(debug=True)
