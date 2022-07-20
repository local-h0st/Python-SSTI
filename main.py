from flask import Flask, request, config, render_template_string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flag{python-ssti}'


@app.route('/')
def index():
    return '<h1>Hello</h1>'


@app.errorhandler(404)
def page_not_found(e):
    template = '''
    {%% block body %%}
        <div class="center-content error">
            <h1>Oops! That page doesn't exist.</h1>
            <h3>%s</h3>
        </div> 
    {%% endblock %%}
    ''' % (request.args.get('evil'))
    return render_template_string(template), 404


if __name__ == '__main__':
    app.run(debug=True)
