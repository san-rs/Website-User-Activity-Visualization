from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from flask import jsonify 
from flask import request
import json
from bson import ObjectId 
from flask_pymongo import PyMongo 
from flask_cors import CORS, cross_origin
import datetime
from random import randint

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
 
app = Flask(__name__)
CORS(app)
app.config['MONGO_DBNAME'] = 'aw1' 
app.config['MONGO_URI'] = 'mongodb://localhost:27017/aw1'

mongo = PyMongo(app)
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return "Hello! Welcome back!<a href='/logout'> Logout</a>"

@app.route('/signup',methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/login',methods=['GET'])
def login():
    return render_template('index.html')  

@app.route('/signupsubmit',methods=['POST'])
def signupsubmit():
    db_name = mongo.db.users
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    username = request.form['username']
    password = request.form['password']
    temp = db_name.find_one({'username':username})
    if (temp == None):
        db_name.insert({'firstname':firstname,'lastname':lastname,'username':username,'password':password,'logintime':[]})
        return render_template('index.html')
    else:
        result = "USER ALREADY EXISTS"
        return JSONEncoder().encode(result)     

@app.route('/loginsubmit',methods=['POST'])
def loginsubmit():
    db_name = mongo.db.users
    username = request.form['username']
    password = request.form['password']
    temp = db_name.find_one({'username':username})
    if ( temp == None):
        result = "ERROR IN USERNAME OR PASSWORD"
        return JSONEncoder().encode(result)
    if ( temp['password'] == password):
        result = "OK"
        session['logged_in'] = True
        session['username'] = username
        db_name.update_one({'username':temp['username']}, { '$push': {'logintime':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}})
        return render_template('home.html',temp=JSONEncoder().encode(temp))
    else:
        result = "ERROR IN USERNAME OR PASSWORD"
        return JSONEncoder().encode(result)

@app.route('/sohome',methods=['GET'])
def sohome():
    return render_template('sohome.html')

@app.route('/s11',methods=['GET'])
def s11():
    return render_template('s11.html')

@app.route('/s12',methods=['GET'])
def s12():
    return render_template('s12.html')

@app.route('/s13',methods=['GET'])
def s13():
    return render_template('s13.html') 

@app.route('/s14',methods=['GET'])
def s14():
    return render_template('s14.html') 

@app.route('/s15',methods=['GET'])
def s15():
    return render_template('s15.html') 

@app.route('/s16',methods=['GET'])
def s16():
    return render_template('s16.html') 

@app.route('/s17',methods=['GET'])
def s17():
    return render_template('s17.html')

@app.route('/s19',methods=['GET'])
def s19():
    return render_template('s19.html') 

@app.route('/s110',methods=['GET'])
def s110():
    return render_template('s110.html') 

@app.route('/s111',methods=['GET'])
def s111():
    return render_template('s111.html') 

@app.route('/s112',methods=['GET'])
def s112():
    return render_template('s112.html') 

@app.route('/s113',methods=['GET'])
def s113():
    return render_template('s113.html') 

@app.route('/s114',methods=['GET'])
def s114():
    return render_template('s114.html') 

@app.route('/s115',methods=['GET'])
def s115():
    return render_template('s115.html')    

@app.route('/jspost', methods = ['POST'])
def jspost():
    db_name = mongo.db.useractionlogs
    jsdata = request.get_json(silent=True)
    if 'username' in session:
        user = session['username']
    temp = db_name.find_one({'user':user})
    if ( temp == None):
        #db_name.insert({'user':user,'user_actions':[{'time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'action':jsdata['data']}]})
        db_name.insert({'user':user,'user_actions':[{'action':jsdata['data']}]})
    else:
        #db_name.update_one({'user':user}, { '$push': {'user_actions':{'time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'action':jsdata['data']}}})
        db_name.update_one({'user':user}, { '$push': {'user_actions':{'action':jsdata['data']}}})
    return jsonify('Success')

@app.route('/visualize',methods=['GET'])
def visualize():
    db_name = mongo.db.useractionlogs
    if 'username' in session:
        user = session['username']
    temp = db_name.find_one({'user':user})
    temp1 = [i['action'] for i in temp['user_actions'] if 'action' in i]#temp['user_actions'][0]['action']
    #myvalues = [i['d'] for i in mylist if 'd' in i]
    #Counter(temp1)
    #print temp1
    #print temp1.count("Scroll Up")
    #return jsonify(temp1=JSONEncoder().encode(temp1))
    temp2 = {'SU':temp1.count("Scroll Up"),'SD':temp1.count("Scroll Down"),'MU':temp1.count("Mouse Up"),'MD':temp1.count("Mouse Down"),'TS':temp1.count("Text Select"),'BC':temp1.count("Button Click"),'LC':temp1.count("Link Click")}
    
    if(user=='aaa'):
        temp3=db_name.find_one({'user':'bbb'})
        temp4=[i['action'] for i in temp3['user_actions'] if 'action' in i]
        temp5=db_name.find_one({'user':'ccc'})
        temp6=[i['action'] for i in temp5['user_actions'] if 'action' in i]
        temp9 = {'q1':randint(0, 8),'q2':randint(0, 8),'q3':randint(0, 8),'q4':randint(0, 8),'q5':randint(0, 8),'q6':randint(0, 8),'q7':randint(0, 8),'q8':randint(0, 8),'q9':randint(0, 8),'q10':randint(0, 8),'q11':randint(0, 8),'q12':randint(0, 8),'q13':10,'q14':randint(0, 8)}

    if(user=='bbb'):
        temp3=db_name.find_one({'user':'aaa'})
        temp4=[i['action'] for i in temp3['user_actions'] if 'action' in i]
        temp5=db_name.find_one({'user':'ccc'})
        temp6=[i['action'] for i in temp5['user_actions'] if 'action' in i]
        temp9 = {'q1':randint(0, 8),'q2':10,'q3':randint(0, 8),'q4':randint(0, 8),'q5':randint(0, 8),'q6':randint(0, 8),'q7':randint(0, 8),'q8':randint(0, 8),'q9':randint(0, 8),'q10':randint(0, 8),'q11':randint(0, 8),'q12':randint(0, 8),'q13':randint(0, 8),'q14':randint(0, 8)}

    if(user=='ccc'):
        temp3=db_name.find_one({'user':'bbb'})
        temp4=[i['action'] for i in temp3['user_actions'] if 'action' in i]
        temp5=db_name.find_one({'user':'aaa'})
        temp6=[i['action'] for i in temp5['user_actions'] if 'action' in i]
        temp9 = {'q1':randint(0, 8),'q2':randint(0, 8),'q3':randint(0, 8),'q4':randint(0, 8),'q5':randint(0, 8),'q6':randint(0, 8),'q7':randint(0, 8),'q8':10,'q9':randint(0, 8),'q10':randint(0, 8),'q11':randint(0, 8),'q12':randint(0, 8),'q13':randint(0, 8),'q14':randint(0, 8)}
        
    t1=temp1.count("Scroll Up")+temp4.count("Scroll Up")+temp6.count("Scroll Up")
    t2=temp1.count("Scroll Down")+temp4.count("Scroll Down")+temp6.count("Scroll Down")
    t3=temp1.count("Mouse Up")+temp4.count("Mouse Up")+temp6.count("Mouse Up")
    t4=temp1.count("Mouse Down")+temp4.count("Mouse Down")+temp6.count("Mouse Down")
    t5=temp1.count("Text Select")+temp4.count("Text Select")+temp6.count("Text Select")
    t6=temp1.count("Button Click")+temp4.count("Button Click")+temp6.count("Button Click")
    t7=temp1.count("Link Click")+temp4.count("Link Click")+temp6.count("Link Click")

    temp7 = {'SU':t1,'SD':t2,'MU':t3,'MD':t4,'TS':t5,'BC':t6,'LC':t7}

    temp8 = {'q1':randint(1, 8),'q2':10,'q3':randint(1, 8),'q4':randint(1, 8),'q5':randint(1, 8),'q6':randint(1, 8),'q7':randint(1, 8),'q8':9,'q9':randint(1, 8),'q10':randint(1, 8),'q11':randint(1, 8),'q12':randint(1, 8),'q13':8,'q14':randint(1, 8)}
    
    return render_template('visualize.html',temp2=JSONEncoder().encode(temp2),temp7=JSONEncoder().encode(temp7),temp8=JSONEncoder().encode(temp8),temp9=JSONEncoder().encode(temp9),user=JSONEncoder().encode(user))

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()

@app.route("/pic",methods=['POST'])
def picture():
    modes = ['Happy','Neutral']
    modeId = 2
    if(request.method== 'POST'):
        content = request.get_json()["data"]
        data = content.split(',')[1].decode("base64")
        file1=open('pic.png','wb')
        file1.write(data)
        file1.close()
        img = Image.open('pic.png').convert('L')
        numpyArray = numpy.array(img)
        backupValidX[0] = numpyArray.flatten()
        valid_set_x.set_value(backupValidX)
        predictedList = getPofYGivenX(0)
        predictedMoods = predictedList[0].tolist()
        returnList = [predictedMoods.index(max(predictedMoods)),max(predictedMoods)]
        os.remove('pic.png')
        mood = modes[returnList[0]]
    print ("Mood = " + str(mood))
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('songs')
    response = table.scan(
        FilterExpression=Attr('type').eq(mood)
    )
    item = response['Items']
    num= random.randrange(0,len(item))
    res={}
    res['mood']=mood
    res['url']=item[num]['url']
    res['song']=item[num]['song']
    res['artist']=item[num]['artist']
    return str(json.dumps(res))

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0',port=5000,threaded=True)