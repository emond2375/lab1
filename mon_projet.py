from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def fct1():
	if request.method=='GET':
		return render_template('accueil.tpl')
	elif request.method=='POST':
		return render_template('bonjour.tpl', name=request.form['nom'], ville=request.form['ville'])
	
@app.errorhandler(404)
def page_not_found(error):
	return render_template('erreur404.tpl', URL=request.url)
