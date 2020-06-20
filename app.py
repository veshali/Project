from __future__ import unicode_literals
from flask import Flask,render_template,url_for,request
import shutil
import keras
import tensorflow
import keras.models
from keras.models import load_model
import numpy as np
from predict import find
import re
import sys 
import os

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/analyze',methods=['GET','POST'])
def analyze():
	result=None
	if request.method == 'POST':
		x1=request.form['raw']
		a1 = request.form['a']
		b1 = request.form['b']
		c1 = request.form['c']
		d1 = request.form['d']
		e1 = request.form['e']
		f1 = request.form['f']
		g1 = request.form['g']
		h1 = request.form['h']
		#result=find(6,142,72,35,0,33.6,0.627,50)
		result = find(a1,b1,c1,d1,e1,f1,g1,h1)
	return render_template('index.html',ans=result,a=x1,c=c1,d=d1,e=e1,f=f1)



@app.route('/about')
def about():
	return render_template('index.html')


if __name__ == '__main__':
	#model = load_model('weights.h5')
	app.run(port=4000, threaded= False)
