from flask import Flask, render_template, request
# import 

app = Flask(__name__)

@app.route('/')
def index():
    ascii_data = [
        {"prompt": '''System Biology Architect Conduct an analysis of the response of {gene2} as a result of changes in {gene1}, using the KEGG Pathway Database. Communicate clearly the relationship between {gene1} and {gene2} using "activation", "inhibition", "phosphorylation" or "no information" when there is no known relation.''', "ascii": "\{ggr9?Rp**1$H31"},
        {"prompt": "Prompt 2", "ascii": "ASCII2"},
        {"prompt": "Prompt 3", "ascii": "ASCII3"},
    ]
    return render_template('index.html', ascii_data=ascii_data)

@app.route('/submit', methods=['POST'])
def submit():
    gene1 = request.form.get('gene1')
    gene2 = request.form.get('gene2')
    prompt = request.form.get('prompt')
    ascii_encoding = request.form.get('ascii')
    options = [option for option in request.form if option.startswith('option')]
    custom_llms = [value for key, value in request.form.items() if key.startswith('custom_llm')]
    return f"Gene 1: {gene1}, Gene 2: {gene2}, Prompt: {prompt}, ASCII Encoding: {ascii_encoding}, Options: {', '.join(options)}, Custom LLMs: {', '.join(custom_llms)}"

if __name__ == '__main__':
    app.run(debug=True)
