from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def accueil_call(name=None):
    return render_template('accueil.tpl', name=name)

#app.route('/static/<name>')
#def static_call(name=None):
#    return render_template('accueil.tpl', name=name)

