from flask import Flask,render_template,request
import pymysql as sql
app=Flask(__name__,)
@app.route('/')
def home():
    return render_template("HOME.html")

@app.route('/hrlogin',methods=['GET','POST'])
def hrlogin():
    return render_template("hrlogin.html")

@app.route('/emplogin',methods=['get','POST'])
def index():
    return render_template("emplogin.html")

@app.route("/")
def close():
    return render_template('HOME.html')
@app.route("/signup",methods=['GET','POST'])
def signup():
    return render_template("register.html")
@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/contact")
def con():
    return render_template('contact.html')
@app.route("/cont")
def cont():
    fname=request.args.get("firstname")
    lname= request.args.get("lastname")
    country = request.args.get("country")
    tex = request.args.get("subject")
    conn = sql.connect(host="localhost", user="root", password="annu", db="hrportal")
    curs = conn.cursor()
    curs.execute("Insert into contact(fname,lname,country,tex)"
                 "values('%s','%s','%s','%s')"%(fname,lname,country,tex))
    conn.commit()
    conn.close()
    return render_template('HOME.html')

@app.route("/save_info")
def save_info():
    EmpID=request.args.get("EmpID")
    psw = request.args.get("psw")
    conn = sql.connect(host="localhost", user="root", password="annu", db="hrportal")
    curs = conn.cursor()
    curs.execute("Insert into register(EmpID,psw)"
                 "values('%s','%s')"%(EmpID,psw))
    conn.commit()
    conn.close()
    return render_template('HOME.html')
@app.route("/hr_login")
def hr_login():
    hr_id=request.args.get("hrid")
    password=request.args.get("psw")
    if ((hr_id=='admin') and (password=='admin')):
        return render_template('hr_page.html')
    else:
        return render_template('error.html')
@app.route("/emlogin")
def emlogin():
    EmpId=int(request.args.get("EmpId"))
    psw=str(request.args.get("psw"))
    conn = sql.connect(host="localhost", user="root", password="annu", db="hrportal")
    curs = conn.cursor()
    curs.execute("select * from register where EmpId='%s' and psw='%s'" %(EmpId,psw))
    result=curs.fetchall()
    if len(result)>0:
        return render_template('em.html')
    else:
        return render_template('error.html')
@app.route("/fills")
def fills():
    return render_template("fill.html")

@app.route("/fill")
def fill():
    empid=request.args.get("empid")
    name = request.args.get("name")
    email = request.args.get("email")
    no= request.args.get("no")
    pos = request.args.get("pos")
    conn = sql.connect(host="localhost", user="root", password="annu", db="hrportal")
    curs = conn.cursor()
    curs.execute("Insert into details(empid,name,email,mno,desig)values('%s','%s','%s','%s','%s')"% (empid,name,email,no,pos))
    conn.commit()
    conn.close()
    return render_template('em.html')
@app.route("/show")
def show():
    conn = sql.connect(host="localhost", port=3306, user="root", password="annu", db="hrportal")
    curs = conn.cursor()
    curs.execute("select * from details")
    results=curs.fetchall()
    return render_template('table1.html', results=results)
@app.route("/assigns")
def assignment():
    return render_template("emp_proj.html")
@app.route("/assign")
def assign():
    empid=request.args.get("id")
    pro = request.args.get("project")
    start= request.args.get("stdate")
    end= request.args.get("enddate")


    conn = sql.connect(host="localhost", user="root", password="annu", db="hrportal")
    curs = conn.cursor()
    curs.execute("Insert into project(empid,proj,start,end)values('%s','%s','%s','%s')"% (empid,pro,start,end))
    conn.commit()
    conn.close()
    return render_template('hr_page.html')
@app.route("/subrep")
def subrep():
    return render_template('subrep.html')
@app.route("/proj")
def proj():
       empid=request.args.get("empid")
       title = request.args.get("title")
       data = request.args.get("pro")
       conn = sql.connect(host="localhost", user="root", password="annu", db="hrportal")
       curs = conn.cursor()
       curs.execute("insert into report(empid,title,data)values('%s','%s','%s')" %(empid,title,data))
       conn.commit()
       conn.close()
       return render_template('em.html')
@app.route("/show_report")
def show_report():


    conn = sql.connect(host="localhost", user="root", password="annu", db="hrportal")
    curs = conn.cursor()
    curs.execute("select * from report")
    results=curs.fetchall()
    return render_template('report.html', results=results)
@app.route("/show_assign")
def show_assign():


    conn = sql.connect(host="localhost", user="root", password="annu", db="hrportal")
    curs = conn.cursor()
    curs.execute("select * from project")
    results=curs.fetchall()
    return render_template('pro_assign.html', results=results)

if __name__=='__main__':
    app.run(debug=True)

