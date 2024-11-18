import os
import time
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set on the server. 
                                     #To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    session["start"] = time.time()
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    session["firstName"]=request.form['firstName']
    session["lastName"]=request.form['lastName']
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    session["favoriteColor"]=request.form['favoriteColor']
    session["end"] = time.time()
    score=0
    if session["firstName"] == "4":
        q1="Incorrect"
    else:  
        q1="Correct"
        score=score+1
        
    if session["lastName"] == "6":
        q2="Incorrect"
    else:
        q2="Correct"
        score=score+1
    
    if session["favoriteColor"] == "Ms. Adams" or session["favoriteColor"] == "ms. adams" or session["favoriteColor"] == "ms adams":
        q3="Incorrect"
    else:
        q3="Correct"
        score=score+1
        
       # Import the time library
   

    # Calculate the start time
   

    # Code here

    # Calculate the end time and time taken
    
    length = session["end"] - session["start"]
    
    
        
    return render_template('page3.html', answer1=q1, answer2=q2, answer3=q3, score=score, length=length)
    
if __name__=="__main__":
    app.run(debug=False)
