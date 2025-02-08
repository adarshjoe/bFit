import random
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import Flask, render_template,request,redirect,session
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from DBConnection import Db
import demjson3 as demjson

app = Flask(__name__)
static_path="C:\\Users\\ADARSH\\Desktop\\ai_fitness_center\\static\\"
app.secret_key="123"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/logout')
def logout():
    session.clear()
    session['lg']=""
    return redirect('/')


@app.route('/login_post',methods=['post'])
def login_post():
    u=request.form['textfield']
    p=request.form['textfield2']
    db=Db()
    res=db.selectOne("select * from login where username='"+u+"' and password='"+p+"'")
    if res is not None:
        session['lid']=res['login_id']
        if res['usertype']=='admin':
            session['lg']='lin'
            return redirect('/admin_home')

        elif res['usertype'] == 'instructor':
            session['lg']='lin'

            return redirect('/gyminstructor_home')

        elif res['usertype'] == 'physician':
            session['lg']='lin'

            session['lid'] = res['login_id']

            return redirect('/physician_home')

        elif res['usertype'] == 'doctor':
            session['lid'] = res['login_id']
            session['lg']='lin'


            return redirect('/doctor_home')

        elif res['usertype'] == 'user':
            session['lid'] = res['login_id']
            session['lg']='lin'


            return redirect('/user_home')
        else:
            return "invalid"
    else:
        return "invalid"



@app.route('/admin_home')
def admin_home():
    if session['lg']!='lin':
        return redirect('/')
    return render_template("admin/index.html")
    # return render_template("admin/admin_home.html")



@app.route('/add_batch')
def add_batch():
    if session['lg'] != 'lin':
        return redirect('/')
    return render_template("admin/add_batches.html")

@app.route('/add_batch_post',methods=['post'])
def add_batch_post():
    if session['lg'] != 'lin':
        return redirect('/')
    dj=request.form['textfield']
    tf=request.form['textfield2']
    tt=request.form['textfield3']
    bn=request.form['textfield4']
    db=Db()
    db.insert("insert into batches VALUES('','"+dj+"','"+tf+"','"+tt+"','"+bn+"')")
    return '<script>alert("success");window.location="/add_batch"</script>'






@app.route('/add_competition')
def add_competition():
    if session['lg'] != 'lin':
        return redirect('/')
    return render_template("admin/add_competition.html")

@app.route('/add_competition_post',methods=['post'])
def add_competition_post():
    if session['lg'] != 'lin':
        return redirect('/')
    cn=request.form['textfield']
    da=request.form['textfield2']
    de=request.form['textarea']
    db=Db()
    db.insert("insert into competition VALUES('','" + cn + "','" + da + "','" + de + "')")
    return '<script>alert("success");window.location="/add_competition"</script>'












@app.route('/add_employee')
def add_employee():
    if session['lg'] != 'lin':
        return redirect('/')
    return render_template("admin/add_employee.html")

@app.route('/add_employee_post',methods=['post'])
def add_employee_post():
    if session['lg'] != 'lin':
        return redirect('/')
    n=request.form['textfield']
    e=request.form['textfield2']
    pn=request.form['textfield3']
    dob=request.form['textfield4']
    g=request.form['radio']
    ex=request.form['textarea']
    pswd=random.randint(1000, 9999)
    db=Db()
    lid=db.insert("insert into login(username, password, usertype) values('"+e+"' ,'"+str(pswd)+"', 'instructor')")
    db.insert("insert into employee VALUES('"+str(lid)+"','"+n+"','"+e+"','"+pn+"','"+dob+"','"+g+"','"+ex+"')")
    import smtplib
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("bfit0924@gmail.com", "jmivfzvrkbrlzave")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "bfit0924@gmail.com"
    msg['To'] = e
    msg['Subject'] = "Your Password for BFIT Website"
    body = "Your Password is:- - " + str(pswd)
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    return '<script>alert("success");window.location="/add_employee"</script>'










@app.route('/add_physician')
def add_physician():
    if session['lg'] != 'lin':
        return redirect('/')
    return render_template("admin/Add_physician.html")


@app.route('/add_physician_post',methods=['post'])
def add_physician_post():
    if session['lg'] != 'lin':
        return redirect('/')
    n=request.form['textfield']
    em=request.form['textfield2']
    pn=request.form['textfield3']
    dob=request.form['textfield4']
    g=request.form['radio']
    qu=request.form['textarea']
    pswd = random.randint(1000, 9999)
    db=Db()
    qry=db.selectOne("select * from login where username='"+em+"'")
    if qry is not None:
        return '<script>alert("Email already exist!!");window.location="/add_physician"</script>'
    else:
        lid = db.insert("insert into login(username, password, usertype) values('" + em + "' ,'" + str(pswd) + "', 'physician')")
        db.insert("insert into physician VALUES('"+str(lid)+"','"+n+"','"+em+"','"+pn+"','"+dob+"','"+g+"','"+qu+"')")
        import smtplib
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("bfit0924@gmail.com", "jmivfzvrkbrlzave")
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = "bfit0924@gmail.com"
        msg['To'] = em
        msg['Subject'] = "Your Password for BFIT Website"
        body = "Your Password is:- - " + str(pswd)
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)

        return '<script>alert("success");window.location="/add_physician"</script>'




@app.route('/gym_requirements')
def gym_requirements():
    if session['lg'] != 'lin':
        return redirect('/')
    return render_template("admin/gym_requirements.html")


@app.route('/gym_requirements_post',methods=['post'])
def gym_requirements_post():
    if session['lg'] != 'lin':
        return redirect('/')
    en=request.form['textfield']
    ed=request.form['textarea']
    ph=request.files['fileField']
    dt=time.strftime("%Y%m%d-%H%M%S")
    ph.save(static_path + "equipments\\" + dt + '.jpg')
    path="/static/equipments/" + dt + '.jpg'
    db = Db()
    db.insert( "insert into equipment_details VALUES('','" + en + "','" + ed + "','" + str(path) + "')")
    return '<script>alert("success");window.location="/gym_requirements"</script>'






@app.route('/allocate_batch/<userid>')
def allocate_batch(userid):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()

    res=db.select("select * from batches")
    res1=db.select("select * from employee")
    return render_template("admin/allocate_batch.html",data=res,data2=res1,u=userid)


@app.route('/allocate_batch_post',methods=['post'])
def allocate_batch_post():
    if session['lg'] != 'lin':
        return redirect('/')
    userid=request.form['uid']
    b=request.form['select']
    i=request.form['select2']
    db = Db()
    qry=db.selectOne("select * from allocate_user where user_id='"+userid+"' and batch_id='"+b+"' and instructor_id='"+i+"' ")
    if qry is not None:
        return '<script>alert("Already Allocated");window.location="/view_user"</script>'
    else:
        db.insert("insert into allocate_user VALUES('','"+userid+"','" + b + "','" + i + "')")
        return '<script>alert("success");window.location="/view_user"</script>'





@app.route('/approve_doctor')
def approve_doctor():
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    res = db.select("select * from doctor,login where doctor.doctor_id=login.login_id and login.usertype='pending' ")

    return render_template("admin/approve_Doctor.html",data=res)

@app.route('/adapprove_doctor/<d>')
def adapprove_doctor(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.update("update login set usertype='doctor' where login_id='"+d+"' ")
    return '<script>alert("approved");window.location="/approve_doctor"</script>'
@app.route('/reject_doctor/<d>')
def reject_doctor(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.delete("delete from login where login_id='"+d+"' ")
    db.delete("delete from doctor  where doctor_id='"+d+"' ")
    return '<script>alert("rejected");window.location="/approve_doctor"</script>'





@app.route('/view_applicants')
def view_applicants():
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from applicants,user,competition where applicants.user_id = user.user_id and applicants.competition_id = competition.competition_id")


    return render_template("admin/view_applicants.html", data=res)
@app.route('/delete_applicants/<d>')
def delete_applicants(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.delete("delete from applicants where applicant_id='"+d+"' ")
    return '<script>alert("deleted");window.location="/view_applicants"</script>'



@app.route('/View_attendance')
def View_attendance():
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from attendance,user where attendance.user_id=user.user_id")
    return render_template("admin/View_attendence.html", data=res)


@app.route('/delete_attendance/<d>')
def delete_attendance(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.delete("delete from attendance where attendance_id='"+d+"' ")
    return '<script>alert("deleted");window.location="/View_attendance"</script>'



@app.route('/view_batches')
def view_batches():
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from batches")
    return render_template("admin/view_batches.html", data=res)

@app.route('/delete_batches/<d>')
def delete_batches(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.delete("delete from batches where batch_id='"+d+"' ")
    return '<script>alert("deleted");window.location="/view_batches"</script>'




@app.route('/view_competition')
def view_competition():
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from competition")
    return render_template("admin/view_competition.html", data=res)
@app.route('/delete_competition/<d>')
def delete_competition(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.delete("delete from competition where competition_id='"+d+"' ")
    return '<script>alert("deleted");window.location="/view_competition"</script>'




@app.route('/view_complaints')
def view_complaints():
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from complaints,user where complaints.user_id = user.user_id ")
    return render_template("admin/view_complaints.html", data=res)
@app.route('/send_reply/<d>', methods=['get', 'post'])
def delete_complaints(d):
    if session['lg'] != 'lin':
        return redirect('/')
    if request.method=="POST":
        rep=request.form['textarea']
        db=Db()
        db.update("update complaints set reply='"+rep+"' where complaint_id='"+d+"'")
        return redirect("/view_complaints")
    else:
        return render_template("admin/send_reply.html")





@app.route('/view_doctor')
def view_doctor():
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from doctor,login where doctor.doctor_id=login.login_id and login.usertype='doctor'")
    return render_template("admin/view_doctor.html", data=res)

@app.route('/view_doctor_review/<g>')
def view_doctor_review(g):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from review,user,doctor where review.user_id = user.user_id and review.doctor_id = doctor.doctor_id and review.doctor_id='"+g+"' ")
    return render_template("admin/view_doctor_review.html", data=res)
@app.route('/delete_doctor_review/<d>')
def delete_doctor_review(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.delete("delete from review where review_id='"+d+"' ")
    return '<script>alert("deleted");window.location="/view_doctor_review"</script>'



@app.route('/view_employee')
def view_employee():
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from employee")
    return render_template("admin/view_employee.html",data=res)
@app.route('/delete_employee/<d>')
def delete_employee(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.delete("delete from employee where employee_id='"+d+"' ")
    return '<script>alert("deleted");window.location="/view_employee"</script>'



@app.route('/View_feedback')
def View_feedback():
    if session['lg'] != 'lin':
        return redirect('/')

    db=Db()
    res=db.select("select * from feedback,user where feedback.user_id=user.user_id")
    return render_template("admin/View_feedback.html", data=res)

@app.route('/delete_feedback/<d>')
def delete_feedback(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.delete("delete from feedback where feedback_id='"+d+"' ")
    return '<script>alert("deleted");window.location="/View_feedback"</script>'




@app.route('/view_gym_requirements')
def view_gym_requirements():
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from equipment_details")
    return render_template("admin/view_gym_requirement.html",data=res)
@app.route('/delete_gym_requirements/<d>')
def delete_gym_requirements(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.delete("delete from equipment_details where equipment_id='"+d+"' ")
    return '<script>alert("deleted");window.location="/view_gym_requirements"</script>'






@app.route('/view_performer')
def view_performer():
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from performer,applicants,competition,user where performer.applicant_id = applicants.applicant_id and applicants.competition_id=competition.competition_id and applicants.user_id=user.user_id")
    return render_template("admin/view_performer.html", data=res)
@app.route('/delete_performer/<d>')
def delete_performer(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.delete("delete from performer where performer_id='"+d+"' ")
    return '<script>alert("deleted");window.location="/view_performer"</script>'




@app.route('/view_physician')
def view_physician():
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from physician")
    return render_template("admin/view_physician.html",data=res)
@app.route('/delete_physician/<d>')
def delete_physician(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.delete("delete from physician where physician_id='"+d+"' ")
    return '<script>alert("deleted");window.location="/view_physician"</script>'




@app.route('/view_user')
def view_user():
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from user,login where user.user_id=login.login_id and login.usertype='user' ")
    return render_template("admin/view_user.html",data=res)
@app.route('/approve_user/<d>')
def approve_user(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.update("update login set usertype='user' where login_id='"+d+"' ")
    return '<script>alert("approved");window.location="/view_user"</script>'
@app.route('/reject_user/<d>')
def reject_user(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.delete("delete from login where login_id='"+d+"' ")
    db.delete("delete from user  where user_id='"+d+"' ")
    return '<script>alert("rejected");window.location="/view_user"</script>'







# ###################################################################################### INSTRUCTOR    ###############################################################################################3

@app.route('/gyminstructor_home')
def gyminstructor_home():
    if session['lg']!='lin':
        return redirect('/')
    return render_template("instructor/gyminstructor_home.html")






@app.route('/add_gyattendance/<uid>')
def add_gyattendance(uid):
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.selectOne("select* from attendance where date=CURDATE() AND user_id='"+uid+"'")
    if res is None:
        db.insert("insert into attendance VALUES('','"+uid+"',curdate(), curtime(), 'pending')")
    else:
        db.update("update attendance set check_out=curtime() where attendance_id='"+str(res['attendance_id'])+"'")
    return '<script>alert("success");window.location="/view_gybatches"</script>'












@app.route('/add_gydiet/<uid>')
def add_gydiet(uid):
    if session['lg']!='lin':
        return redirect('/')

    return render_template("instructor/add_gydiet.html", uid=uid)


@app.route('/add_gydiet_post',methods=['post'])
def add_gydiet_post():
    if session['lg']!='lin':
        return redirect('/')
    uid=request.form['hid']
    b=request.form['textfield']
    l=request.form['textfield2']
    pow=request.form['textfield3']
    prew=request.form['textfield4']
    ap=request.form['textfield5']
    c=request.form['textfield6']
    db=Db()
    db.insert("insert into diet VALUES('', '"+uid+"','"+b+"','"+l+"','"+pow+"','"+prew+"','"+ap+"','"+c+"')")
    return '<script>alert("success");window.location="/view_gybatches"</script>'






@app.route('/view_gybatches')
def view_gybatches():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res = db.select("select batches.* from allocate_user,batches where allocate_user.batch_id=batches.batch_id  and allocate_user.instructor_id='"+str(session['lid'])+"' group by allocate_user.batch_id")
    return render_template("instructor/view_gybatches.html",data=res)



@app.route('/view_gyuser/<bid>')
def view_gyuser(bid):
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res = db.select("select * from user ,allocate_user where allocate_user.user_id=user.user_id and allocate_user.batch_id='"+bid+"' and allocate_user.instructor_id='"+str(session['lid'])+"' ")
    return render_template("instructor/view_gyuser.html",data=res)








@app.route('/view_applicant')
def view_applicant():
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from applicants,user,competition where applicants.user_id = user.user_id and applicants.competition_id = competition.competition_id")

    return render_template("instructor/view_applicant.html", data=res)


@app.route('/approve_applicant/<d>')
def approve_applicant(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.update("update applicants set status='approved' where applicant_id='"+d+"' ")
    db.insert("insert into performer VALUES ('','"+d+"')")
    return '<script>alert("approved");window.location="/view_applicant#content"</script>'

@app.route('/reject_applicant/<d>')
def reject_applicants(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.update("update applicants set status='rejected' where applicant_id='"+d+"' ")
    return '<script>alert("rejected");window.location="/view_applicant#content"</script>'





@app.route('/view_performers')
def view_performers():
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from performer,applicants,competition,user where performer.applicant_id = applicants.applicant_id and applicants.competition_id=competition.competition_id and applicants.user_id=user.user_id")
    return render_template("instructor/view_performers.html", data=res)

@app.route('/delete_performers/<d>')
def delete_performers(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.delete("delete from performer where performer_id='"+d+"' ")
    return '<script>alert("deleted");window.location="/view_performers"</script>'



@app.route("/rr")
def rr():
    return render_template("reg_index.html")









@app.route('/view_gycompetition')
def view_gycompetition():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res = db.select("select * from competition ")

    return render_template("instructor/view_gycompetition.html",data=res)
@app.route('/delete_gycompetition/<d>')
def delete_gycompetition(d):
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    db.delete("delete from competition where competition_id='"+d+"' ")
    return '<script>alert("deleted");window.location="/view_gycompetition"</script>'








@app.route('/view_gyupdateuser/<k>')
def view_gyupdateuser(k):
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    r=db.selectOne("select * from allocate_user,user where allocate_user.user_id=user.user_id and allocate_user.user_id='"+k+"'  ")
    return render_template("instructor/view_gyupdateuser.html",data=r)




@app.route('/add_gyupdateuser_post', methods=['post'])
def add_gyupdateuser_post():
    if session['lg'] != 'lin':
        return redirect('/')
    w=request.form['textfield7']
    h=request.form['textfield8']
    uid=request.form['hid']
    height=int(h)/100
    bmi=int(w)/int(height)*int(height)
    db=Db()
    db.update("update user set weight='"+w+"',height='"+h+"',bmi='"+str(bmi)+"' where user_id='"+uid+"' ")
    return '<script>alert("success");window.location="/view_gybatches#content";</script>'









@app.route('/view_gymedicine')
def view_gymedicine():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from medicine")
    return render_template("instructor/view_gymedicine.html", data=res)

















#######################################################################    PHYSICIAN         ##############################################################################################################################################




@app.route('/physician_home')
def physician_home():
    if session['lg']!='lin':
        return redirect('/')
    return render_template("Physician/physician_home.html")








@app.route('/add_stock/<mid>')
def add_stock(mid):
    if session['lg']!='lin':
        return redirect('/')
    return render_template("Physician/add_stock.html",mid=mid)



@app.route('/add_stock_post',methods=['post'])
def add_stock_post():
    if session['lg']!='lin':
        return redirect('/')
    r=request.form['textfield']
    mid = request.form['hid']



    db=Db()
    res=db.selectOne(" select * from stock where physician_id='"+str(session['lid'])+"' and medicine_id='"+mid+"'")
    if res is None:
        db.insert("insert into stock VALUES('','"+str(session['lid'])+"','" + mid + "','"+r+"' )")
    else:
        db.update("update stock set stock=stock+'"+r+"' where stock_id='"+str(res['stock_id'])+"'")
    return '<script>alert("success");window.location="/view_medicine"</script>'





@app.route('/send_doubt_reply/<did>')
def send_doubt_reply(did):
    if session['lg']!='lin':
        return redirect('/')
    return render_template("Physician/send_doubt_reply.html", did=did)


@app.route('/send_doubt_reply_post',methods=['post'])
def send_doubt_reply_post():
    if session['lg']!='lin':
        return redirect('/')
    r=request.form['textarea']
    did=request.form['hid']


    db=Db()
    db.update("update doubts set reply='"+r+"' where doubt_id='"+did+"' ")
    return '<script>alert("success");window.location="/view_doubts"</script>'







@app.route('/view_booking')
def view_booking():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.select(" select * from booking ,user  where booking.user_id = user.user_id and booking.physician_id='"+str(session['lid'])+"'")
    return render_template("Physician/view_booking.html", data=res)




@app.route('/view_items/<bid>')
def view_items(bid):
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.select(" SELECT * FROM booking_sub ,medicine WHERE booking_sub.medicine_id = medicine.medicine_id and booking_id='"+bid+"'")
    return render_template("Physician/view_items.html", data=res)







@app.route('/view_medicine')
def view_medicine():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from medicine")
    return render_template("Physician/view_medicine.html", data=res)






@app.route('/view_doubts')
def view_doubts():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from doubts,user where doubts.user_id = user.user_id")
    return render_template("Physician/view_doubts.html", data=res)





@app.route('/view_payment')
def view_itemview_payments():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from booking,payment,user where booking.booking_id=payment.booking_id and booking.user_id=user.user_id and booking.physician_id='"+str(session['lid'])+"'")
    return render_template("Physician/view_payment.html", data=res)









@app.route('/phys_view_user')
def phys_view_user():
    db=Db()
    res=db.select("select * from user")
    return render_template("Physician/view_user.html", data=res)







######################################              DOCTOR     ############################################################################################################3
@app.route('/doctor_home')
def doctor_home():
    if session['lg']!='lin':
        return redirect('/')
    return render_template("doctor/doctor_home.html")



@app.route('/doctor_register')
def doctor_register():
    return render_template("doctor/register.html")

@app.route('/doctor_register_post',methods=['post'])
def doctor_register_post():
    n=request.form['textfield']
    ex=request.form['textfield2']
    q=request.form['textfield3']
    em=request.form['textfield4']
    ph=request.form['textfield5']
    dob=request.form['textfield6']
    pas = request.form['textfield7']
    g = request.form['radio']
    db=Db()
    lid=db.insert("insert into login values(null,'"+em+"', '"+pas+"', 'pending')")
    db.insert("insert into doctor VALUES('"+str(lid)+"','"+n+"','"+ex+"','"+q+"','"+em+"','"+ph+"','"+dob+"','"+g+"')")
    return '<script>alert("success");window.location="/"</script>'












@app.route('/view_doctor_profile')
def view_doctor_profile():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.selectOne("select * from doctor where doctor_id='"+str(session['lid'])+"'")
    return render_template("doctor/view_profile.html", data=res)


@app.route('/update_doctor_post',methods=['post'])
def update_doctor_post():
    if session['lg']!='lin':
        return redirect('/')
    n=request.form['textfield']
    ex=request.form['textfield2']
    q=request.form['textfield3']
    ph=request.form['textfield5']
    dob=request.form['textfield6']
    g = request.form['radio']
    db=Db()
    lid=db.update("update doctor set doctor_name='"+n+"',experience='"+ex+"',qualification='"+q+"',phone_no='"+ph+"',dob='"+dob+"',gender='"+g+"' where doctor_id='"+str(session['lid'])+"'")
    return '<script>alert("success");window.location="/view_doctor_profile"</script>'









@app.route('/change_password')
def change_password():
    if session['lg']!='lin':
        return redirect('/')
    return render_template("doctor/change_password.html")

@app.route('/change_password_post',methods=['post'])
def change_password_post():
    if session['lg']!='lin':
        return redirect('/')
    np=request.form['textfield']
    cp=request.form['textfield2']
    if cp==np:
        db=Db()
        db.update("update login set password='"+np+"' where login_id='"+str(session['lid'])+"'")
        return '<script>alert("success");window.location="/"</script>'
    else:

        return '<script>alert("Password mismatch");window.location="/change_password"</script>'



@app.route('/add_schedule')
def add_schedule():
    if session['lg']!='lin':
        return redirect('/')
    return render_template("doctor/add_schedule.html")


@app.route('/add_schedule_post',methods=['post'])
def add_schedule_post():
    if session['lg']!='lin':
        return redirect('/')
    d=request.form['textfield']
    ft=request.form['textfield2']
    tt=request.form['textfield3']
    tk=request.form['textfield4']
    db=Db()
    qry=db.selectOne("select * from schedule where date='"+d+"' and time_from='"+ft+"' and time_to='"+tt+"' ")
    if qry is not None:
        return '<script>alert("Already added");window.location="/add_schedule"</script>'
    else:
        db.insert("insert into schedule VALUES('','"+str(session['lid'])+"','" + d + "','" + ft + "','" + tt + "','"+tk+"')")
        return '<script>alert("success");window.location="/add_schedule"</script>'



@app.route('/view_schedule')
def View_schedule():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from schedule where doctor_id='"+str(session['lid'])+"'")
    return render_template("doctor/view_schedule.html", data=res)

@app.route('/delete_schedule/<d>')
def delete_schedule(d):
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    db.delete("delete from schedule where schedule_id='"+d+"' ")
    return '<script>alert("deleted");window.location="/view_schedule"</script>'







@app.route('/view_appointment')
def view_appointment():
    if session['lg'] != 'lin':
        return redirect('/')
    db = Db()
    res = db.select("select * from appointment,schedule,user where appointment.schedule_id=schedule.schedule_id and appointment.user_id=user.user_id and doctor_id='"+str(session['lid'])+"'")
    return render_template("doctor/view_appointment.html", data=res)







@app.route('/view_review')
def view_review():
    if session['lg'] != 'lin':
        return redirect('/')
    db = Db()
    lid=session['lid']
    print(lid)
     # res = db.select("select * from review,user where review.user_id=user.user_id and review.doctor_id='"+str(session['lid'])+"'")
    res = db.select("select * from review,user where review.user_id=user.user_id and review.doctor_id='"+str(lid)+"'")
    print(res)
    return render_template("doctor/view_review.html", data=res)



# -----------------------doctor chat-----------------------

@app.route('/ph_user_chat/<uid>')
def ph_user_chat(uid):
    if session['lg']=="lin":

        return render_template("doctor/doctor_user_chat.html",u=uid)
    else:
        return redirect('/')


@app.route('/chatsnd/<u>',methods=['post'])
def chatsnd(u):
    if session['lg']=="lin":

        db=Db()
        c = session['lid']
        b=request.form['n']
        print(b)
        m=request.form['m']

        q2="insert into chat values('','"+str(c)+"','"+str(u)+"','"+m+"',curdate())"
        res=db.insert(q2)
        v = {}
        if int(res) > 0:
            v["status"] = "ok"

        else:
            v["status"] = "error"

        r = demjson.encode(v)

        return r
    # else:
    #     return redirect('/')


@app.route('/chatrply',methods=['post'])
def chatrply():
    # if session['lg']=="lin":

        print("...........................")
        c = session['lid']
        t = Db()
        qry2 = "select * from chat ORDER BY chat_id ASC ";
        res = t.select(qry2)
        print(res,)

        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
            v['id']=c
        else:
            v["status"] = "error"

        rw = demjson.encode(v)
        return rw
    # else:
    #     return redirect('/')





















###########################################            USER            ##################################################################################


@app.route('/user_home')
def user_home():
    if session['lg']!='lin':
        return redirect('/')

    return render_template("user/user_home.html")



@app.route('/add_registration1')
def add_registration1():
    return render_template("user/registration1.html")

@app.route('/add_registration1_post',methods=['post'])
def add_registration1_post():
    n=request.form['textfield']
    e=request.form['textfield2']
    pn=request.form['textfield3']
    dob=request.form['textfield4']
    g = request.form['radio']
    ph=request.files['fileField']
    dt=time.strftime("%Y%m%d-%H%M%S")
    ph.save(static_path + "profile_photo\\" + dt + '.jpg')
    path="/static/profile_photo/" + dt + '.jpg'
    h = request.form['textfield5']
    w = request.form['textfield6']
    psw = request.form['textfield7']

    session['n']=n
    session['e'] = e
    session['pn'] = pn
    session['dob'] = dob
    session['g'] = g
    session['path'] = str(path)
    session['h'] = h
    session['w'] = w
    session['psw'] = psw

    return render_template("user/registration2.html")


@app.route('/add_registration2_post',methods=['post'])
def add_registration2_post():
    # if session['lg']!='lin':
    #     return redirect('/')
    am=request.form['textfield']
    b = request.form['select']
    ac=request.form['textfield2']
    ifsc=request.form['textfield3']
    db=Db()

    res=db.selectOne("select * from bank where bank_name='"+b+"' and account_no='"+ac+"' and ifsc='"+ifsc+"'")
    if res is None:
        return '<script>alert("Invalid Bank details");window.location="/"</script>'
    else:
        if float(am)>float(res['balance']):
            return '<script>alert("Insufficient balance");window.location="/add_registration1"</script>'
        else:
            n=session['n']
            e=session['e']
            pn= session['pn']
            dob=session['dob']
            g= session['g']
            path = session['path']
            h= session['h']
            w=session['w']

            h_m=int(h)/100
            w_kg=int(w)
            bmi=w_kg/(h_m*h_m)
            bmi=round(bmi, 2)
            psw=session['psw']
            print("aaaaaaaaaaaaaa",path)
            lid=db.insert("insert into login values(null, '"+e+"', '"+psw+"','user')")
            db.insert("insert into user VALUES('"+str(lid)+"','" + n + "','" + e + "','" + pn + "','" + dob + "','" + g + "','"+ str(path) +"','" + w + "','" + h + "', '"+str(bmi)+"')")
            db.update("update bank set balance=balance-'"+am+"' where bank_id='"+str(res['bank_id'])+"'")
            db.update("update bank set balance=balance+'"+am+"' where bank_id='1'")
            return '<script>alert("success");window.location="/"</script>'



@app.route('/send_complaints')
def send_complaints():
    if session['lg']!='lin':
        return redirect('/')
    return render_template("user/send_complaints.html")


@app.route('/send_complaints_post',methods=['post'])
def send_complaints_post():
    if session['lg']!='lin':
        return redirect('/')
    c=request.form['textarea']

    db=Db()
    db.insert("insert into complaints VALUES('','"+str(session['lid'])+"', curdate(),'"+ c +"','pending')")
    return '<script>alert("success");window.location="/send_complaints"</script>'




@app.route('/send_doubts')
def send_doubts():
    if session['lg']!='lin':
        return redirect('/')
    return render_template("user/send_doubts.html")


@app.route('/send_doubts_post',methods=['post'])
def send_doubts_post():
    if session['lg']!='lin':
        return redirect('/')
    d=request.form['textarea']

    db=Db()
    db.insert("insert into doubts VALUES('','"+str(session['lid'])+"', curdate(),'"+ d +"','pending')")
    return '<script>alert("success");window.location="/send_doubts"</script>'


@app.route('/send_feedback')
def send_feedback():
    if session['lg']!='lin':
        return redirect('/')
    return render_template("user/send_feedback.html")


@app.route('/send_feedback_post',methods=['post'])
def send_feedback_post():
    if session['lg']!='lin':
        return redirect('/')
    f=request.form['textarea']

    db=Db()
    db.insert("insert into feedback VALUES('','"+str(session['lid'])+"', curdate(),'"+ f +"')")
    return '<script>alert("success");window.location="/send_feedback"</script>'




@app.route('/view_complaint')
def view_complaint():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from complaints where user_id = '"+str(session['lid'])+"' ")
    return render_template("user/view_complaints.html", data=res)
@app.route('/delete_complaint/<d>')
def delete_complaint(d):
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    db.delete("delete from complaints where complaint_id='"+d+"' ")
    return '<script>alert("deleted");window.location="/view_complaint"</script>'




@app.route('/view_doubt')
def view_doubt():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from doubts,user where doubts.user_id = user.user_id")
    return render_template("user/view_doubts.html", data=res)




@app.route('/view_gym_equipment')
def view_gym_equipment():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from equipment_details")
    return render_template("user/view_gym_equipments.html",data=res)

@app.route('/delete_gym_equipment/<d>')
def delete_gym_equipment(d):
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    db.delete("delete from equipment_details where equipment_id='"+d+"' ")
    return '<script>alert("deleted");window.location="/view_gym_equipments"</script>'






@app.route('/view_profile')
def view_profile():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res = db.selectOne("select * from user where user_id='"+str(session['lid'])+"' ")
    return render_template("user/view_profile.html",data=res)



@app.route('/drop_gym')
def drop_gym():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    db.delete("delete from allocate_user where user_id='"+str(session['lid'])+"' ")
    return '<script>alert("Batch dropped");window.location="/user_home";</script>'


@app.route('/view_competitions')
def view_competitions():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from competition")
    return render_template("user/view_competition.html", data=res)


@app.route('/apply_competition/<cid>')
def apply_competition(cid):
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    qry=db.selectOne("select * from applicants WHERE user_id='"+str(session['lid'])+"' and competition_id='"+cid+"'")
    if qry is not None:
        return '<script>alert("already applied");window.location="/view_competitions";</script>'
    res=db.insert("insert into applicants value('','"+str(session['lid'])+"','"+str(cid)+"',curdate(),'pending')")
    return '<script>alert("successfully applied");window.location="/view_competitions";</script>'


@app.route('/view_doctors')
def view_doctors():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from doctor,login where doctor.doctor_id=login.login_id and login.usertype='doctor'")
    return render_template("user/view_doctor.html", data=res)


@app.route('/view_doctor_schedule/<did>')
def view_doctor_schedule(did):
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from schedule where doctor_id='"+did+"'")
    return render_template("user/view_doctor_schedule.html", data=res)

@app.route('/book_appointment/<d>')
def book_appointment(d):
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    qry1=db.selectOne("select * from appointment where schedule_id='"+d+"' and user_id='"+str(session['lid'])+"'")
    if qry1 is not None:
        return '<script>alert("Already Booked!!");window.location="/view_doctors"</script>'
    else:
        qry=db.selectOne("select * from appointment where schedule_id='"+d+"'")
        if qry is not None:
            tocken=qry['token_no']
            res=db.selectOne("select max(token_no) as tkn from appointment where schedule_id='"+d+"'")
            tkn=int(res['tkn'])+1
            if tkn == tocken:
                return '<script>alert("Bookinf full");window.location="/view_doctors"</script>'
            else:
                db.insert("insert into appointment VALUES('', curdate(),'"+str(session['lid'])+"','"+d+"','"+str(tkn)+"')")
                return '<script>alert("success");window.location="/view_doctors"</script>'

        else:
            db.insert("insert into appointment VALUES('', curdate(),'"+str(session['lid'])+"','"+d+"','1')")
            return '<script>alert("success");window.location="/view_doctors"</script>'





@app.route('/send_review/<did>')
def send_review(did):
    if session['lg']!='lin':
        return redirect('/')
    return render_template("user/send_review.html",d=did)


@app.route('/send_review_post',methods=['post'])
def send_review_post():
    if session['lg']!='lin':
        return redirect('/')
    did=request.form['did']
    r=request.form['textarea']

    db=Db()
    db.insert("insert into review VALUES('', curdate(),'"+str(session['lid'])+"','"+did+"','"+r+"')")
    return '<script>alert("success");window.location="/view_doctors"</script>'


@app.route('/view_appointments')
def view_appointments():
    if session['lg'] != 'lin':
        return redirect('/')
    db = Db()
    res = db.select("select * from appointment,schedule,doctor where appointment.schedule_id=schedule.schedule_id and schedule.doctor_id=doctor.doctor_id and user_id='"+str(session['lid'])+"'")
    return render_template("user/view_appointments.html", data=res)





@app.route('/view_medicines')
def view_medicines():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from medicine")
    return render_template("user/view_medicines.html", data=res)

@app.route('/user_view_physician/<medicineid>')
def user_view_physician(medicineid):
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from physician,stock where physician.physician_id=stock.physician_id and stock.medicine_id='"+medicineid+"'")
    return render_template("user/view_physician.html", data=res)


@app.route('/buy_medicine/<pid>/<mid>/<sid>')
def buy_medicine(pid,mid,sid):
    if session['lg']!='lin':
        return redirect('/')

    return render_template("user/enter_quantity.html",p=pid,m=mid,s=sid)

@app.route('/buy_medicine_post',methods=['post'])
def buy_medicine_post():
    if session['lg']!='lin':
        return redirect('/')
    pid=request.form['pid']
    mid=request.form['mid']
    sid=request.form['sid']
    print("SS  ", pid, mid, sid)
    q=request.form['textfield']
    db=Db()
    qry=db.selectOne("select * from booking where physician_id='"+pid+"' and user_id='"+str(session['lid'])+"' and status='add_to_cart'")
    if qry is not None:
        bkid=qry['booking_id']
        qry1 = db.selectOne("select * from booking_sub where medicine_id='" + mid + "' and booking_id='"+str(bkid)+"'")
        if qry1 is not None:
            bid=qry1['sub_id']
            db.update("update booking_sub set quantity=quantity+'"+q+"' where sub_id='"+str(bid)+"' ")
            db.update("update stock set stock=stock-'"+q+"' where stock_id='"+str(sid)+"' ")
            return '<script>alert("Add to cart");window.location="/view_medicines"</script>'

        else:
            db.insert("insert into booking_sub VALUES ('','"+str(bkid)+"','"+mid+"','"+q+"')")
            db.update("update stock set stock=stock-'" + q + "' where stock_id='" +str(sid) + "' ")
            return '<script>alert("Add to cart");window.location="/view_medicines"</script>'

    else:
        qry3=db.insert("insert into booking VALUES ('','" + str(session['lid']) + "','" + pid + "',curdate(),'0','add_to_cart')")
        db.insert("insert into booking_sub VALUES ('','" + str(qry3) + "','" + mid + "','" + q + "')")
        db.update("update stock set stock=stock-'" + q + "' where stock_id='" + str(sid) + "' ")
        return '<script>alert("Add to cart");window.location="/view_medicines"</script>'


@app.route('/view_diet')
def view_diet():
    if session['lg']!='lin':
        return redirect('/')
    db=Db()
    res=db.select("select * from diet where diet.user_id = '"+str(session['lid'])+"' ")
    return render_template("user/view_diet.html", data=res)







@app.route('/view_cart')
def view_cart():
        if session['lg'] != 'lin':
            return redirect('/')
        db = Db()
        res = db.select("select booking_sub.quantity*medicine.medicine_price as price,medicine.*,booking_sub.*,booking.* from booking,booking_sub,stock,medicine where booking.booking_id=booking_sub.booking_id and booking.physician_id=stock.physician_id and booking_sub.medicine_id=stock.medicine_id and stock.medicine_id=medicine.medicine_id and booking.status='add_to_cart' and booking.user_id='"+str(session['lid'])+"' and booking.status='add_to_cart'")
        # res1 = db.selectOne("select sum(booking_sub.quantity*medicine.medicine_price) as gt,medicine.*,booking_sub.*,booking.* from booking,booking_sub,stock,medicine where booking.booking_id=booking_sub.booking_id and booking_sub.medicine_id=stock.medicine_id and stock.medicine_id=medicine.medicine_id and booking.user_id='"+str(session['lid'])+"' and booking.status='add_to_cart'")
        print(res)
        tot=0
        for i in res:
            p=i['price']
            tot=tot+float(i['price'])
            print(p)
        return render_template("user/view_cart.html", data=res, tot=tot)



@app.route('/delete_cart/<d>')
def delete_cart(d):
    if session['lg'] != 'lin':
        return redirect('/')
    db=Db()
    db.delete("delete from booking_sub where sub_id='"+d+"' ")
    return '<script>alert("deleted");window.location="/view_cart"</script>'




@app.route('/heart')
def heart():
    return render_template("heart.html")


@app.route('/heart_post',methods=['post'])
def heart_post():
    a=request.form['textfield']
    g=request.form['radio2']
    cpt=request.form['select']
    rbp=request.form['textfield2']
    sc=request.form['textfield3']
    fbs=request.form['textfield4']
    rer = request.form['textfield5']
    mhr = request.form['textfield6']
    eia = request.form['textfield7']
    ar=[]
    ar.append(int(a))
    ar.append(int(g))
    ar.append(int(cpt))
    ar.append(int(rbp))
    ar.append(int(sc))
    ar.append(int(fbs))
    ar.append(int(rer))
    ar.append(int(mhr))
    ar.append(int(eia))
    print(ar)

    import pandas as pd
    data=pd.read_csv(static_path + "heart_new.csv")
    attributes=data.values[:, :9]
    labels=data.values[:, 9]

    X_train, X_test, Y_train, Y_test =train_test_split(attributes, labels, test_size=0.3)
    obj=RandomForestClassifier()
    obj.fit(X_train, Y_train)
    rf_pred=obj.predict(X_test)
    accuracy=accuracy_score(Y_test, rf_pred)
    acc=round(accuracy *100, 2)

    rf=RandomForestClassifier()
    rf.fit(attributes, labels)
    pred=rf.predict([ar])
    prediction=pred[0]
    print(prediction)
    if prediction == 1:
        msg="Be Careful. There is a chance for having heart disease.\nConsult a doctor"
        stat="not safe"
    elif prediction ==0:
        msg="You are safe now. Heart disease occurance rate is low."
        stat="safe"
    return render_template("heart.html", msg=msg, acc=acc, stat=stat)


@app.route('/payment_mode/<tot>')
def payment_mode(tot):
    if session['lg']!='lin':
        return redirect('/')
    session['tot']=tot
    return render_template("user/payment_mode.html")


@app.route('/payment_mode_post',methods=['post'])
def payment_mode_post():
    if session['lg']!='lin':
        return redirect('/')

    mode=request.form['radio2']
    db=Db()
    if mode =='Offline':
        res = db.select("select * from booking where user_id='"+str(session['lid'])+"' and booking.status='add_to_cart'")
        for i in res:
            print(i)
            bid=i['booking_id']
            db=Db()
            db.update("update booking set status='Offline payment' where booking_id='"+str(bid)+"'")
        return "<script>alert('Order placed');window.location='/user_home'</script>"

    else:
        tot=session['tot']
        return render_template('user/bank_payment2.html', tot=tot)

@app.route('/add_bank_payment2_post', methods=['get', 'post'])
def add_bank_payment2_post():
    if request.method=="POST":
        # if session['lg']!='lin':
        #     return redirect('/')
        am = request.form['textfield']
        b = request.form['select']
        ac = request.form['textfield2']
        ifsc = request.form['textfield3']
        db = Db()

        res = db.selectOne(
            "select * from bank where bank_name='" + b + "' and account_no='" + ac + "' and ifsc='" + ifsc + "'")
        if res is None:
            return '<script>alert("Invalid Bank details");window.location="/add_bank_payment2_post"</script>'
        else:
            if float(am) > float(res['balance']):
                return '<script>alert("Insufficient balance");window.location="/add_bank_payment2_post"</script>'
            else:
                resd=db.select("select * from booking where user_id='"+str(session['lid'])+"' and status='add_to_cart'")
                for i in resd:
                    db.update("update bank set balance=balance-'" + am + "' where bank_id='" + str(res['bank_id']) + "'")
                    db.update("update booking set status='Paid', amount='"+am+"' where booking_id='"+str(i['booking_id'])+"'")
                return '<script>alert("success");window.location="/user_home"</script>'

    else:
        tot=session['tot']
        return render_template("user/bank_payment.html", tot=tot)

# @app.route('/payment_mode_post',methods=['post'])
# def payment_mode_post():
#     if session['lg']!='lin':
#         return redirect('/')
#     uid=request.form['hid']
#     b=request.form['textfield']
#     l=request.form['textfield2']
#     pow=request.form['textfield3']
#     prew=request.form['textfield4']
#     ap=request.form['textfield5']
#     c=request.form['textfield6']
#     db=Db()
#     db.insert("insert into diet VALUES('', '"+uid+"','"+b+"','"+l+"','"+pow+"','"+prew+"','"+ap+"','"+c+"')")
#     return '<script>alert("success");window.location="/view_gybatches"</script>'
#
#
#

# -----------------------user chat-----------------------

@app.route('/ph_user_chat1/<uid>')
def ph_user_chat1(uid):
    if session['lg']=="lin":

        return render_template("user/user_doctor_chat.html",u=uid)
    else:
        return redirect('/')


@app.route('/chatsnd1/<u>',methods=['post'])
def chatsnd1(u):
    if session['lg']=="lin":

        db=Db()
        c = session['lid']
        b=request.form['n']
        print(b)
        m=request.form['m']

        q2="insert into chat values('','"+str(c)+"','"+str(u)+"','"+m+"',curdate())"
        res=db.insert(q2)
        v = {}
        if int(res) > 0:
            v["status"] = "ok"

        else:
            v["status"] = "error"

        r = demjson.encode(v)

        return r
    # else:
    #     return redirect('/')


@app.route('/chatrply1',methods=['post'])
def chatrply1():
    # if session['lg']=="lin":

        print("...........................")
        c = session['lid']
        t = Db()
        qry2 = "select * from chat ORDER BY chat_id ASC ";
        res = t.select(qry2)
        print(res,)

        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
            v['id']=c
        else:
            v["status"] = "error"

        rw = demjson.encode(v)
        return rw
    # else:
    #     return redirect('/')




@app.route('/public_view_gym_equipment')
def public_view_gym_equipment():
    db=Db()
    res=db.select("select * from equipment_details")
    return render_template("view_gym_equipments.html",data=res)












if __name__ == '__main__':
    app.run(debug=True)
