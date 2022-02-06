from flask import Flask,render_template,request,redirect
from flask.wrappers import Request
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql
import pandas as pd
from twilio.rest import Client

app = Flask(__name__)#syntax to initialize app
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///MentorDetails.db"
app.config['SQLALCHEMY_BINDS']={'MenteeDetails':"sqlite:///MenteeDetails.db"}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

#Mentor DETAILS TABLE
class MentorDetails(db.Model): #table column defination
    name= db.Column(db.String(200))
    email=db.Column(db.String(200),primary_key = True)
    pronouns= db.Column(db.String(200))
    AD= db.Column(db.String(200))
    AI= db.Column(db.String(200))
    coding= db.Column(db.String(200)) 
    CS=db.Column(db.String(200))
    CyS= db.Column(db.String(200))
    DS= db.Column(db.String(200))
    IT= db.Column(db.String(200))
    IOS=db.Column(db.String(200))
    robotics= db.Column(db.String(200))
    SE= db.Column(db.String(200))
    UI=db.Column(db.String(200))
    WD= db.Column(db.String(200))
    dropdownMenuButton1= db.Column(db.String(200))
    Bio=db.Column(db.String(200))
    Availability=db.Column(db.Integer)

    
#returns an object which prints details
    def __repr__(self) ->str:
        return f'{self.email} - {self.name}'



class MenteeDetails(db.Model):
    __bind_key__ = 'MenteeDetails'
    name2= db.Column(db.String(200))
    email2=db.Column(db.String(200),primary_key = True)
    pronouns2= db.Column(db.String(200))
    AD2= db.Column(db.String(200))
    AI2= db.Column(db.String(200))
    coding2= db.Column(db.String(200)) 
    CS2=db.Column(db.String(200))
    CyS2= db.Column(db.String(200))
    DS2= db.Column(db.String(200))
    IT2= db.Column(db.String(200))
    IOS2=db.Column(db.String(200))
    robotics2= db.Column(db.String(200))
    SE2= db.Column(db.String(200))
    UI2=db.Column(db.String(200))
    WD2= db.Column(db.String(200))
    dropdownMenuButton2= db.Column(db.String(200))
    goals2=db.Column(db.String(200))
    Bio2=db.Column(db.String(200))
    Availability2=db.Column(db.Integer)
    

#returns an object which prints details
    def __repr__(self) ->str:
        return f'{self.email2} - {self.name2}'

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/MentorD')
def mentorD():
    return render_template('MentorDetails.html')

@app.route('/MenteeD')
def menteeD():
    return render_template('MenteeDetails.html')

#MENTOR DETAILS
@app.route('/MentorDetails',methods=['GET','POST'])
def MentorDetailsPage():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        pronouns=request.form['pronouns']
        AD=request.form.get('AD',False)
        AI=request.form.get('AI',False)
        coding=request.form.get('coding',False)
        CS=request.form.get('CS',False)
        CyS=request.form.get('CyS',False)
        DS=request.form.get('DS',False)
        IT=request.form.get('IT',False)
        IOS=request.form.get('IOS',False)
        robotics=request.form.get('robotics',False)
        SE=request.form.get('SE',False)
        UI=request.form.get('UI',False)
        WD=request.form.get('WD',False)
        dropdownMenuButton1=request.form.get('dropdownMenuButton1')
        Bio=request.form['Bio']
        Availability=request.form['Availability']
        insert = MentorDetails(name=name,email=email,pronouns=pronouns,AD=AD,AI=AI,coding=coding,CS=CS,CyS=CyS,DS=DS,IT=IT,IOS=IOS,robotics=robotics,SE=SE,UI=UI,WD=WD,dropdownMenuButton1=dropdownMenuButton1,Bio=Bio,Availability=Availability)
        db.session.add(insert)
        db.session.commit()
    allMentorDetails=MentorDetails.query.all()
    list()
    return render_template('MentorDetails.html',allMentorDetails=allMentorDetails)



''' @app.route('/MentorDetailsview')
def MentorDetailsview():
    allMentorDetails = MentorDetails.query.all()#Displays repr function
    return render_template('MentorDetailsview.html',allMentorDetails=allMentorDetails)


@app.route('/DeleteMentorDetails/<int:sno>')
def deleteMentorDetails(sno):
    delete = MentorDetails.query.filter_by(sno=sno).first()
    db.session.delete(delete)
    db.session.commit()
    return redirect("/MentorDetailsview") '''





#EDUCATION DETAILS 
@app.route('/MenteeDetails',methods=['GET','POST'])
def MenteeDetailsPage():
    if request.method=='POST':
        name2=request.form['name2']
        email2=request.form['email2']
        pronouns2=request.form['pronouns2']
        AD2=request.form.get('AD2',False)
        AI2=request.form.get('AI2',False)
        coding2=request.form.get('coding2',False)
        CS2=request.form.get('CS2',False)
        CyS2=request.form.get('CyS2',False)
        DS2=request.form.get('DS2',False)
        IT2=request.form.get('IT2',False)
        IOS2=request.form.get('IOS2',False)
        robotics2=request.form.get('robotics2',False)
        SE2=request.form.get('SE2',False)
        UI2=request.form.get('UI2',False)
        WD2=request.form.get('WD2',False)
        dropdownMenuButton2=request.form.get('dropdownMenuButton2')
        goals2=request.form['goals2']
        Bio2=request.form['Bio2']
        Availability2=request.form['Availability2']
    
        insert = MenteeDetails(name2=name2,email2=email2,pronouns2=pronouns2,AD2=AD2,AI2=AI2,coding2=coding2,CS2=CS2,CyS2=CyS2,DS2=DS2,IT2=IT2,IOS2=IOS2,robotics2=robotics2,SE2=SE2,UI2=UI2,WD2=WD2,dropdownMenuButton2=dropdownMenuButton2,goals2=goals2,Bio2=Bio2,Availability2=Availability2)

        db.session.add(insert)
        db.session.commit()
        
    allMenteeDetails=MenteeDetails.query.all()
    return render_template('MenteeDetails.html',allMenteeDetails=allMenteeDetails)




''' @app.route('/MenteeDetailsview')
def MenteeDetailsview():
    allMenteeDetails = MenteeDetails.query.all()#Displays repr function
    return render_template('MenteeDetailsview.html',allMenteeDetails=allMenteeDetails)

@app.route('/DeleteMenteeDetails/<int:sno>')
def deleteMenteeDetails(sno):
    delete = MenteeDetails.query.filter_by(sno=sno).first()
    db.session.delete(delete)
    db.session.commit()
    return redirect("/MenteeDetailsview.html")   '''

@app.route('/DataDownloadLogin',methods=['GET','POST'])
def MentorResult():
    if request.method=='POST':
        print('inner')
        username=request.form['username']
        password=request.form['password']
        if username=='geshita' and password == 'geshita':
            print('inner if')
            name=[]
            email=[]
            pronouns=[]
            AD=[]
            AI=[]
            coding=[]
            CS=[]
            CyS=[]
            DS=[]
            IT=[]
            IOS=[]
            robotics=[]
            SE=[]
            UI=[]
            WD=[]
            dropdownMenuButton=[]
            Bio=[]
            Availability=[]
            
            con = sql.connect("MentorDetails.db")
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute("select * from mentor_details")
            rows = cur.fetchall();
        
            for row in rows:
                name.append(row["name"])
                email.append(row["email"])
                pronouns.append(row["pronouns"])
        
                AD.append(row["AD"])
                AI.append(row["AI"])
                coding.append(row["coding"])
                CS.append(row["CS"])
                CyS.append(row["CyS"])
                DS.append(row["DS"])
                IT.append(row["IT"])
                IOS.append(row["IOS"])
                robotics.append(row["robotics"])
                SE.append(row["SE"])
                UI.append(row["UI"])
                WD.append(row["WD"])
        
                dropdownMenuButton.append(row["dropdownMenuButton1"])
                Bio.append(row["Bio"])
                Availability.append(row["Availability"])
            
            MentorDataframe={'name':name,'email':email,'pronouns':pronouns,'AD':AD,'AI':AI,'coding':coding,'CS':CS,'CyS':CyS,'DS':DS,'IT':IT,'IOS':IOS,'robotics':robotics,'SE':SE,'UI':UI,'WD':WD,'dropdownMenuButton':dropdownMenuButton,'Bio':Bio,'Availability':Availability}
            df=pd.DataFrame(MentorDataframe)
            df.to_csv('MentorDataframe.csv')
            print(name)
            print(dropdownMenuButton)
            print(Availability)
            return render_template('index.html')
        else :
            return render_template('DataDownloadLogin.html')
    return render_template('DataDownloadLogin.html')

@app.route('/DataDownloadLogin2',methods=['GET','POST'])
def MenteeResult():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        if username=='geshita' and password == 'geshita':
            con = sql.connect("MenteeDetails.db")
            con.row_factory = sql.Row
            
            cur = con.cursor()
            cur.execute("select * from mentee_details")
            
            rows = cur.fetchall();
            name2=[]
            email2=[]
            pronouns2=[]
            AD2=[]
            AI2=[]
            coding2=[]
            CS2=[]
            CyS2=[]
            DS2=[]
            IT2=[]
            IOS2=[]
            robotics2=[]
            SE2=[]
            UI2=[]
            WD2=[]
            dropdownMenuButton2=[]
            goals2=[]
            Bio2=[]
            Availability2=[]
        
            for row in rows:
                name2.append(row["name2"])
                email2.append(row["email2"])
                pronouns2.append(row["pronouns2"])
        
                AD2.append(row["AD2"])
                AI2.append(row["AI2"])
                coding2.append(row["coding2"])
                CS2.append(row["CS2"])
                CyS2.append(row["CyS2"])
                DS2.append(row["DS2"])
                IT2.append(row["IT2"])
                IOS2.append(row["IOS2"])
                robotics2.append(row["robotics2"])
                SE2.append(row["SE2"])
                UI2.append(row["UI2"])
                WD2.append(row["WD2"])
        
                dropdownMenuButton2.append(row["dropdownMenuButton2"])
                goals2.append(row["goals2"])
                Bio2.append(row["Bio2"])
                Availability2.append(row["Availability2"])
        
            MenteeDataframe={'name2':name2,'email2':email2,'pronouns2':pronouns2,'AD2':AD2,'AI2':AI2,'coding2':coding2,'CS2':CS2,'CyS2':CyS2,'DS2':DS2,'IT2':IT2,'IOS2':IOS2,'robotics2':robotics2,'SE2':SE2,'UI2':UI2,'WD2':WD2,'dropdownMenuButton2':dropdownMenuButton2,'Bio2':Bio2,'Availability2':Availability2,'goals2':goals2}
            df=pd.DataFrame(MenteeDataframe)
            df.to_csv('MenteeDataframe.csv')
            print(name2)
            print(dropdownMenuButton2)
            print(Availability2)
        
            return render_template('DataDownloadLogin2.html')
        else :
            return render_template('DataDownloadLogin2.html')
    return render_template('DataDownloadLogin2.html')

@app.route('/TwilioForm',methods=['GET','POST'])
def TwilioForm():
    if request.method=="POST":
        account_sid=request.form['sid']
        auth_token=request.form['token']
        twwpfrom=request.form['wpfrom']
        twwpto=request.form['wpto']
        twmsg=request.form['msg']


        client = Client(account_sid, auth_token)

        message = client.messages \
        .create(
            body=twmsg,
            from_='whatsapp:'+twwpfrom,
            to='whatsapp:'+twwpto
        )

        print(message.sid)
        

    return render_template('TwilioForm.html')

if __name__=="__main__":
    app.run(debug=True)
    
