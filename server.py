from flask import Flask, render_template, redirect, session, request  #render_template displays the html files, redirect will be used to change the route, session is to put things in session, request is used to handle input from forms
from env import KEY


app = Flask(__name__)
#My secret key from the env file.
app.secret_key = KEY
thePets= []

# Landing page -  this should be seen in the address bar of the browser
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/createUser/', methods=['POST'])
def createUser():
    session['user']= request.form['user']
    # request.form['user'] is what's coming from our html index.html page, more specifically in our name input.
    return redirect('/pets/')

@app.route('/pets/')
def pets():
    if 'user' not in session:
        print('Route reached but you not logged in')
        return redirect('/')
    if 'petName' not in session:
        return render_template('pets.html')
    else:
        data= session['petName']
        thePets.append(data)
        return render_template('pets.html', petList = thePets)

@app.route('/createPet/', methods=['POST'])
def createPet():
    session['petName']= request.form['petName']
    # request.form['user'] is what's coming from our html index.html page, more specifically in our name input.
    return redirect('/pets/')

@app.route('/reset/')
def reset():
    session.pop('petName')
    return redirect('/pets')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
