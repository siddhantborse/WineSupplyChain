import os
import MySQLdb import smtplib import random import string
from datetime import datetime
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash, send_file from database import db_connect,owner_reg,owner_login,ac_act1,c_login1,cvp1,cvp_act,con_act # from cloud import uploadFile,downloadFile,close
From database import db_connect,ap_act,p_login,ad_act,d_login,ar_act,r_login,addp_act,dvp1,dvp3,rvp1,rvp3,s_act
from sendmail import sendmail
from main import generateblockchain # def db_connect():
#	_conn = MySQLdb.connect(host="localhost", user="root", #	passwd="root", db="assigndb")
#	c = _conn.cursor() #	return c, _conn
app = Flask( name ) app.secret_key = os.urandom(24) @app.route("/")
def FUN_root():
return render_template("index.html") @app.route("/producer.html")
def producer():
return render_template("producer.html") @app.route("/search.html")
def search():
# -------------------------------Registration-----------------------------------------------------------------    





@app.route("/oregact", methods = ['GET','POST'])
def oregact():
   if request.method == 'POST':    
      
      status = owner_reg(request.form['username'],request.form['password'],request.form['email'],request.form['address'])
      
      if status == 1:
       return render_template("owner.html",m1="sucess")
      else:
       return render_template("ownerreg.html",m1="failed")


@app.route("/apact", methods = ['GET','POST'])
def apact():
   if request.method == 'POST':    
      
      status = ap_act(request.form['username'],request.form['password'],request.form['email'],request.form['address'])
      
      if status == 1:
       return render_template("ap.html",m1="sucess")
      else:
       return render_template("ap.html",m1="failed")
      
@app.route("/addpact", methods = ['GET','POST'])
def addpact():
   if request.method == 'POST':
    
      pid = request.form['pid'] 
      pname = request.form['pname'] 
      price = request.form['price'] 
      image = request.form['image'] 
      username = session['username']
      atas,key=generateblockchain(username,username)
      print("blockchain")
      print(key)  
      key2  = key
       
      
      status = addp_act(pid,pname,price,image,request,username,key2)
      
      if status == 1:
       return render_template("addp.html",m1="sucess")
      else:
       return render_template("addp.html",m1="failed")
      

@app.route("/searchact", methods = ['GET','POST'])
def searchact():
   if request.method == 'POST':
    
      pid = request.form['pid']
      
      data = s_act(pid)
      return render_template("search1.html",m1="sucess",data=data)

      
@app.route("/aract", methods = ['GET','POST'])
def aract():
   if request.method == 'POST':    
      
      status = ar_act(request.form['username'],request.form['password'],request.form['email'],request.form['address'])
      
      if status == 1:
       return render_template("ar.html",m1="sucess")
      else:
       return render_template("ar.html",m1="failed")

@app.route("/adact", methods = ['GET','POST'])
def adact():
   if request.method == 'POST':    
      
      status = ad_act(request.form['username'],request.form['password'],request.form['email'],request.form['address'])
      
      if status == 1:
       return render_template("ad.html",m1="sucess")
      else:
       return render_template("ad.html",m1="failed")





      
# #-------------------------------ADD_END---------------------------------------------------------------------------
# # -------------------------------Loginact-----------------------------------------------------------------


@app.route("/ologin", methods=['GET', 'POST'])       
def ologin():
    if request.method == 'POST':
        status = owner_login(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("ohome.html", m1="sucess")
        else:
            return render_template("owner.html", m1="Login Failed")

@app.route("/plogin", methods=['GET', 'POST'])       
def plogin():
    if request.method == 'POST':
        status = p_login(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("phome.html", m1="sucess")
        else:
            return render_template("producer.html", m1="Login Failed")

@app.route("/rlogin", methods=['GET', 'POST'])       
def rlogin():
    if request.method == 'POST':
        status = r_login(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("rhome.html", m1="sucess")
        else:
            return render_template("re.html", m1="Login Failed")

@app.route("/dlogin", methods=['GET', 'POST'])       
def dlogin():
    if request.method == 'POST':
        status = d_login(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("dhome.html", m1="sucess")
        else:
            return render_template("distb.html", m1="Login Failed")


        


# # -------------------------------Loginact End-----------------------------------------------------------------

if __name__ == "__main__":
app.run(debug=True, host='127.0.0.1', port=5000)
