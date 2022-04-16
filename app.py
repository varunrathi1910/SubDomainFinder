import os
import shutil,time
import random
from flask import Flask, flash, redirect, render_template, request,url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug.utils import secure_filename
import socket

app = Flask(__name__)

#routes
@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/uploader', methods = ['POST'])
def uploader():	
	listPrefix=[]
	resultSet=[]
	domainName = request.form.get("url")
	with open('static/db/wordlist.txt') as f:
		listPrefix=[i.strip() for  i in f.readlines()]
	for prefix in listPrefix:
		url=prefix+'.'+domainName
		try:
			# print(url)
			result = socket.getaddrinfo(url, None, 0, socket.SOCK_STREAM)
			# print(url)
			resultSet.append(url)
		except Exception as e:
			pass
	print(resultSet)
	return render_template('helloWorld.html',resultSet=resultSet)


# main code to run
app.secret_key="InternProject"
app.run(debug = True)