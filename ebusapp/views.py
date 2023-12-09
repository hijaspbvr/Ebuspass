from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import pymysql
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from io import BytesIO
from django.http import HttpResponse


db = pymysql.connect(host="localhost", user="root",
                     password="", database="dbebuspass")
c = db.cursor()


# def sendsms(ph, msg):
#     sendToPhoneNumber = "+91"+ph
#     userid = "2000022557"
#     passwd = "54321@lcc"
#     url = "http://enterprise.smsgupshup.com/GatewayAPI/rest?method=sendMessage&send_to=" + sendToPhoneNumber + \
#         "&msg=" + msg + "&userid=" + userid + "&password=" + \
#         passwd + "&v=1.1&msg_type=TEXT&auth_scheme=PLAIN"
#     # contents = urllib.request.urlopen(url)
#     webbrowser.open(url)

######################################################################
#                           LOAD INDEX PAGE
######################################################################


def index(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    return render(request, "index.html")
######################################################################
#                           LOGIN
######################################################################


def login(request):
    """ 
        The function for login process
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        email = request.POST.get("txtEmail")
        pwd = request.POST.get("txtPassword")
        s = "select count(*) from tbllogin where uname='"+email+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[0] > 0):
            request.session["email"] = email
            s = "select * from tbllogin where uname='"+email+"'"
            c.execute(s)
            i = c.fetchone()
            if(i[1] == pwd):
                request.session['email'] = email
                if(i[3] == "1"):
                    if(i[2] == "admin"):
                        return HttpResponseRedirect("/adminhome")
                    elif(i[2] == "depo"):
                        return HttpResponseRedirect("/depohome")
                    elif(i[2] == "institute"):
                        return HttpResponseRedirect("/institutehome")
                    elif(i[2] == "student"):
                        return HttpResponseRedirect("/studenthome")
                else:
                    msg = "You are not authenticated to login"
            else:
                msg = "Incorrect password"
        else:
            msg = "User doesnt exist"
    return render(request, "login.html", {"msg": msg})
######################################################################
#                           ADMIN HOME
######################################################################


def adminhome(request):
    """ 
        The function to load home page of the admin. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    return render(request, "adminhome.html")
######################################################################
#                           ADMIN DEPO
######################################################################


def admindepo(request):
    """ 
        The function for adding depo details 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    s = "select count(*) from tbldepo where depoEmail in(select uname from tbllogin where status='1')"
    c.execute(s)
    data = c.fetchall()
    if(request.POST):
        place = request.POST["txtPlace"]
        email = request.POST["txtEmail"]
        contact = request.POST["txtContact"]
        pin = request.POST["txtPin"]
        dist = request.POST["dist"]
        s = "insert into tbldepo (depoPlace,depoEmail,depoContact) values('" + \
            place+"','"+email+"','"+contact+"')"
        print(s)
        try:
            c.execute(s)
            db.commit
        except:
            msg = "Sorry registration error"
        else:
            s = "insert into tbllogin(uname,pwd,utype,status) values('" + \
                email+"','"+email+"','depo','1')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry login error"
            else:
                msg = "Depo added successfully"
    s = "select * from tbldepo where depoEmail in(select uname from tbllogin where status='1')"
    c.execute(s)
    data = c.fetchall()
    return render(request, "admindepo.html", {"data": data, "msg": msg})
######################################################################
#                           ADMIN DELETE DEPO
######################################################################


def admindepodelete(request):
    """ 
        The function to delete depo
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.GET.get("id")
    s = "update tbllogin set status='0' where uname='"+email+"'"
    try:
        c.execute(s)
        db.commit()
    except:
        msg = "Sorry some error occured"
    else:
        return HttpResponseRedirect("/admindepo")
    return render(request, "admindepo.html", {"msg": msg})
######################################################################
#                           ADMIN COURSE
######################################################################


def admincourse(request):
    """ 
        The function for adding course details 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    s = "select count(*) from tblcourse where status='1'"
    c.execute(s)
    data = c.fetchall()
    if(request.POST):
        course = request.POST["txtCourse"]
        s = "insert into tblcourse (courseName,status) values('" + \
            course+"','1')"
        try:
            c.execute(s)
            db.commit
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Depo added successfully"
    s = "select * from tblcourse where status='1'"
    c.execute(s)
    data = c.fetchall()
    return render(request, "admincourse.html", {"data": data, "msg": msg})
######################################################################
#                           ADMIN DELETE COURSE
######################################################################


def admincoursedelete(request):
    """ 
        The function to delete course
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.GET.get("id")
    s = "update tblcourse set status='0' where courseId='"+email+"'"
    try:
        c.execute(s)
        db.commit()
    except:
        msg = "Sorry some error occured"
    else:
        return HttpResponseRedirect("/admincourse")
    return render(request, "admincourse.html", {"msg": msg})
######################################################################
#                       ADMIN VIEW INSTITUTE
######################################################################


def admininstitute(request):
    """ 
        The function to view and approve institute
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    s = "select * from tblinstitute where inEmail in(select uname from tbllogin where status='0')"
    c.execute(s)
    data = c.fetchall()
    s = "select * from tblinstitute where inEmail in(select uname from tbllogin where status='1')"
    c.execute(s)
    data1 = c.fetchall()
    return render(request, "admininstitute.html", {"data": data, "data1": data1})
######################################################################
#                           ADMIN INSTITUTE
######################################################################


def admininstitutedelete(request):
    """ 
        The function to delete course
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.GET.get("id")
    status = request.GET.get("status")
    s = "update tbllogin set status='"+status+"' where uname='"+email+"'"
    try:
        c.execute(s)
        db.commit()
    except:
        msg = "Sorry some error occured"
    else:
        # msg="Sorry some error occured"
        return HttpResponseRedirect("/admininstitute")
    return render(request, "admininstitute.html", {"msg": msg})
######################################################################
#                           ADMIN CARD TYPE
######################################################################


def admincardtype(request):
    """ 
        The function to add card type
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    s = "select * from tblcard where status='1'"
    c.execute(s)
    data = c.fetchall()
    if(request.POST):
        card = request.POST["txtCardType"]
        days = request.POST["txtDays"]
        s = "insert into tblcard(cardType,noDays,status) values('" + \
            card+"','"+days+"','1')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            return HttpResponseRedirect("/admincardtype")
    s = "select * from tblcard where status='1'"
    c.execute(s)
    data = c.fetchall()
    return render(request, "admincardtype.html", {"msg": msg, "data": data})
######################################################################
#                           ADMIN CARD DELETE
######################################################################


def admincarddelete(request):
    """ 
        The function to delete card type
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    cid = request.GET.get("id")
    s = "update tblcard set status='0' where cardId='"+cid+"'"
    try:
        c.execute(s)
        db.commit()
    except:
        msg = "Sorry some error occured"
    else:
        return HttpResponseRedirect("/admincardtype")
    return render(request, "admincardtype.html", {"msg": msg})
######################################################################
#                           ADMIN STOP
######################################################################


def adminstop(request):
    """ 
        The function to add stop
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    s = "select * from tblstop where status='1'"
    c.execute(s)
    data = c.fetchall()
    s = "select depoEmail,depoPlace from tbldepo where depoEmail in(Select uname from tbllogin where status='1')"
    c.execute(s)
    data1 = c.fetchall()
    if(request.POST):
        stop = request.POST["txtStop"]
        depo = request.POST["depo"]
        s = "insert into tblstop(stopName,depoEmail,status) values('" + \
            stop+"','"+depo+"','1')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            return HttpResponseRedirect("/adminstop")
    s = "select * from tblstop where status='1'"
    c.execute(s)
    data = c.fetchall()
    return render(request, "adminstop.html", {"msg": msg, "data": data, "data1": data1})
######################################################################
#                           ADMIN STOP DELETE
######################################################################


def adminstopdelete(request):
    """ 
        The function to delete stop
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    cid = request.GET.get("id")
    s = "update tblstop set status='0' where stopId='"+cid+"'"
    try:
        c.execute(s)
        db.commit()
    except:
        msg = "Sorry some error occured"
    else:
        return HttpResponseRedirect("/adminstop")
    return render(request, "adminstop.html", {"msg": msg})
######################################################################
#                           ADMIN RATE
######################################################################


def adminrate(request):
    """ 
        The function to add rate
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    s = "select * from tblroute where status='1'"
    c.execute(s)
    data = c.fetchall()
    s = "select * from tblstop where status='1'"
    c.execute(s)
    stop = c.fetchall()
    if(request.POST):
        sfrom = request.POST["txtFrom"]
        sto = request.POST["txtTo"]
        charge = request.POST["txtCharge"]
        s = "insert into tblroute (rFrom,rTo,charge,status) values('" + \
            sfrom+"','"+sto+"','"+charge+"','1')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            return HttpResponseRedirect("/adminrate")
    s = "select * from tblroute where status='1'"
    c.execute(s)
    data = c.fetchall()
    return render(request, "adminrate.html", {"msg": msg, "data": data, "stop": stop})
######################################################################
#                           ADMIN RATE DELETE
######################################################################


def adminratedelete(request):
    """ 
        The function to delete rate
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    cid = request.GET.get("id")
    s = "update tblroute set status='0' where rId='"+cid+"'"
    try:
        c.execute(s)
        db.commit()
    except:
        msg = "Sorry some error occured"
    else:
        return HttpResponseRedirect("/adminrate")
    return render(request, "adminrate.html", {"msg": msg})
######################################################################
#                           DEPO HOME
######################################################################


def depohome(request):
    """ 
        The function to load depo home
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    email = request.session["email"]
    s = "select * from tbldepo where depoEmail='"+email+"'"
    c.execute(s)
    data = c.fetchall()
    if(request.POST):
        place = request.POST["txtPlace"]
        email = request.POST["txtEmail"]
        contact = request.POST["txtContact"]
        s = "update tbldepo set depoPlace='"+place + \
            "',depoContact='"+contact+"' where depoEmail='"+email+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            return HttpResponseRedirect("/depohome")
    return render(request, "depohome.html", {"msg": msg, "data": data})
######################################################################
#                           DEPO APPLICATION
######################################################################


def depoapplications(request):
    """ 
        The function to load depo applications
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    s = "select tblstudentregistration.*,tblstudentdetails.*,tblinstitute.inName,tblcard.cardType from tblstudentregistration,tblcard,tblstudentdetails,tblinstitute,tblstop where tblstudentdetails.sEmail in(select uname from tbllogin where status='1') and tblstudentdetails.sEmail=tblstudentregistration.sEmail and tblstudentdetails.cardId=tblcard.cardId and tblstudentregistration.inId=tblinstitute.inId and tblstudentdetails.status='requested' and tblstop.depoEmail='" + \
        email+"' and tblstop.stopName=tblstudentdetails.placeFrom"
    c.execute(s)
    data = c.fetchall()
    s = "select tblstudentregistration.*,tblstudentdetails.*,tblinstitute.inName,tblcard.cardType from tblstudentregistration,tblcard,tblstudentdetails,tblinstitute,tblstop where tblstudentdetails.sEmail in(select uname from tbllogin where status='1') and tblstudentdetails.sEmail=tblstudentregistration.sEmail and tblstudentdetails.cardId=tblcard.cardId and tblstudentregistration.inId=tblinstitute.inId and (tblstudentdetails.status='approved' or tblstudentdetails.status='paid') and tblstop.depoEmail='"+email+"' and tblstop.stopName=tblstudentdetails.placeFrom"
    c.execute(s)
    data1 = c.fetchall()
    return render(request, "depoapplications.html", {"data": data, "data1": data1})
######################################################################
#                           DEPO APPLICATION APPROVE
######################################################################


def depoapplicationapprove(request):
    """ 
        The function to approve depo applications
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    did = request.GET.get('id')
    status = request.GET.get('s')
    phn = request.GET.get('phone')
    if(status == "approved"):

        s = "select * from tblstudentdetails where sdId='"+did+"'"
        c.execute(s)
        i = c.fetchone()
        sfrom = i[2]
        to = i[3]
        s = "select rId from tblroute where (rFrom='"+sfrom + \
            "' and rTo='"+to+"') or (rTo='"+sfrom+"' and rFrom='"+to+"')"
        print(s)
        c.execute(s)
        i = c.fetchone()
        rid = i[0]
        if(rid != ""):
            c.execute("select charge from tblroute where rId='"+str(rid)+"'")
            i = c.fetchone()
            amt = i[0]

            c.execute(
                "select * from tblcard where cardId in(select cardId from tblstudentdetails where sdId='"+did+"')")
            i = c.fetchone()
            # cardid=i[0]
            no = i[2]

            tot = int(amt)*int(no)
            s = "insert into tblconcession (sdId,from_date,to_date,amount,status) values ('"+str(
                did)+"',(select sysdate()),(select date_add((select sysdate()),interval '" + str(no)+"' day)),'"+str(tot)+"','approved')"
            print(s)
            c.execute(s)
            db.commit()

    c.execute("update tblstudentdetails set status='" +
              status+"' where sdId='"+did+"'")
    db.commit()

    msg = "Your application for concession has been "+str(status)
    # sendsms(phn, msg)

    return HttpResponseRedirect("/depoapplications")
######################################################################
#                           DEPO PAYMENTS
######################################################################


def depopayments(request):
    """ 
        The function to load payments
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    s = "select tblstudentregistration.*,tblstudentdetails.*,tblinstitute.inName,tblcard.cardType,tblconcession.amount from tblstudentregistration,tblcard,tblstudentdetails,tblinstitute,tblconcession,tblstop where tblstudentdetails.sEmail in(select uname from tbllogin where status='1') and tblstudentdetails.sEmail=tblstudentregistration.sEmail and tblstudentdetails.cardId=tblcard.cardId and tblstudentregistration.inId=tblinstitute.inId and tblconcession.sdId=tblstudentdetails.sdId and tblstudentdetails.status='paid' and tblstop.depoEmail='"+email+"' and tblstop.stopName=tblstudentdetails.placeFrom"
    c.execute(s)
    data = c.fetchall()
    return render(request, "depopayments.html", {"data": data})
######################################################################
#                           DEPO CHANGE PASSWORD
######################################################################


def depochangepassword(request):
    """ 
        The function to change password
        --------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    msg = ""
    if(request.POST):
        current = request.POST["txtCurrent"]
        new = request.POST["txtNew"]
        s = "select * from tbllogin where uname='"+email+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[1] == current):
            s = "update tbllogin set pwd='"+new+"' where uname='"+email+"'"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Data updated successfully"
        else:
            msg = "Incorrect password"
    return render(request, "depochangepassword.html", {"msg": msg})
######################################################################
#                           INSTITUTE HOME
######################################################################


def institutehome(request):
    """ 
        The function to load institute home
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    email = request.session["email"]
    s = "select * from tblinstitute where inEmail='"+email+"'"
    c.execute(s)
    data = c.fetchall()
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        email = request.POST["txtEmail"]
        contact = request.POST["txtNumber"]
        s = "update tblinstitute set inName='"+name+"',inAddress='" + \
            address+"',inContact='"+contact+"' where inEmail='"+email+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            return HttpResponseRedirect("/institutehome")
    return render(request, "institutehome.html", {"msg": msg, "data": data})
######################################################################
#                           INSTITUTE COURSE
######################################################################


def institutecourse(request):
    """ 
        The function to load institute courses
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    email = request.session["email"]
    s = "select * from tblcourse where courseId not in(select courseId from tblinstitutecourse where inEmail='"+email+"')"
    c.execute(s)
    course = c.fetchall()
    s = "select * from tblcourse where courseId  in(select courseId from tblinstitutecourse where inEmail='"+email+"')"
    c.execute(s)
    data = c.fetchall()
    if(request.POST):
        course = request.POST["crs"]
        s = "insert into tblinstitutecourse (inEmail,courseId,status) values('" + \
            email+"','"+course+"','1')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            return HttpResponseRedirect("/institutecourse")
    return render(request, "institutecourse.html", {"msg": msg, "data": data, "course": course})
######################################################################
#                           INSTITUTE affiliation
######################################################################


def instituteaffiliation(request):
    """ 
        The function to load institute affiliation
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    email = request.session["email"]
    s = "select * from tblaffiliation where inId in(select inId from tblinstitute where inEmail='"+email+"')"
    c.execute(s)
    data = c.fetchall()
    if(request.POST):
        atype = request.POST["txtType"]
        fname = request.FILES["txtFile"]
        fs = FileSystemStorage()
        filename = fs.save(fname.name, fname)
        uploaded_file_url = fs.url(filename)
        s = "insert into tblaffiliation (inId,affType,affPath,status) values((select inId from tblinstitute where inEmail='" + \
            email+"'),'"+atype+"','"+uploaded_file_url+"','1')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            return HttpResponseRedirect("/instituteaffiliation")
    return render(request, "instituteaffiliation.html", {"msg": msg, "data": data})
######################################################################
#                           INSTITUTE STUDENT
######################################################################


def institutestudents(request):
    """ 
        The function to approve institute students
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    s = "select tblstudentregistration.* from tblstudentregistration where  inId in(select inId from tblinstitute where inEmail='" + \
        email + \
        "') and tblstudentregistration.sEmail in(select uname from tbllogin where status='0')"
    c.execute(s)
    data = c.fetchall()
    email = request.session["email"]
    s = "select tblstudentregistration.* from tblstudentregistration where  inId in(select inId from tblinstitute where inEmail='" + \
        email + \
        "') and tblstudentregistration.sEmail in(select uname from tbllogin where status='1')"
    c.execute(s)
    data1 = c.fetchall()
    return render(request, "institutestudents.html", {"data": data, "data1": data1})
######################################################################
#                      INSTITUTE STUDENT APPROVE
######################################################################


def institutestudentapprove(request):
    """ 
        The function to approve institute students
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.GET.get("id")
    s = "update tbllogin set status='1' where uname='"+email+"'"
    try:
        c.execute(s)
        db.commit()
    except:
        msg = "Sorry some error occured"
    else:
        return HttpResponseRedirect("/institutestudents")
    return render(request, "institutestudents.html", {"msg": msg})
def institutestudentreject(request):
    """ 
        The function to approve institute students
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.GET.get("id")
    s = "update tbllogin set status='2' where uname='"+email+"'"
    try:
        c.execute(s)
        db.commit()
    except:
        msg = "Sorry some error occured"
    else:
        return HttpResponseRedirect("/institutestudents")
    return render(request, "institutestudents.html", {"msg": msg})

######################################################################
#                      STUDENT HOME
######################################################################


def studenthome(request):
    """ 
        The function to load student home
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    s = "select * from tblstudentregistration where sEmail='"+email+"'"
    c.execute(s)
    data = c.fetchall()
    return render(request, "studenthome.html", {"data": data})
######################################################################
#                      STUDENT DETAILS
######################################################################


def studentdetails(request):
    """ 
        The function to load student details
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    if(request.POST):
        start = request.POST["txtFrom"]
        to = request.POST["txtTo"]
        card = request.POST["txtCard"]
        aadhar = request.POST["txtAadhar"]

        fname = request.FILES["txtFile"]
        fs = FileSystemStorage()
        filename = fs.save(fname.name, fname)
        uploaded_file_url = fs.url(filename)

        s = "insert into tblstudentdetails(sEmail,placeFrom,placeTo,cardId,aadharNo,photo,status) values('" + \
            email+"','"+start+"','"+to+"','"+card+"','" + \
            aadhar+"','"+uploaded_file_url+"','requested')"
        c.execute(s)
        db.commit()

    s = "select * from tblstop where status='1'"
    c.execute(s)
    stop = c.fetchall()
    s = "select * from tblcard where status='1'"
    c.execute(s)
    card = c.fetchall()
    s = "select tblstudentdetails.*,tblcard.cardType from tblstudentdetails,tblcard where tblstudentdetails.sEmail='" + \
        email+"' and tblstudentdetails.cardId=tblcard.cardId"
    c.execute(s)
    data = c.fetchall()
    return render(request, "studentdetails.html", {"data": data, "stop": stop, "card": card})
######################################################################
#                      STUDENT PAYMENT
######################################################################


def payment(request):
    """ 
        The function to load student payment
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    cid = request.GET.get("id")
    email = request.session['email']
    amt = 0
    s = "select count(*) from tblconcession where cardId='"+cid+"'"
    c.execute(s)
    i = c.fetchone()
    if(i[0] == 0):
        return HttpResponseRedirect("/studentpayment")
    s = "select * from tblconcession where cardId='"+cid+"'"
    c.execute(s)
    i = c.fetchone()
    if(i[5] == "paid"):
        return HttpResponseRedirect("/studentgeneratecard")
    else:
        amt = i[4]
    if(request.POST):
        s = "update tblconcession set status='paid' where cardId='"+cid+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            s = "update tblstudentdetails set status='paid' where sEmail='"+email+"'"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry some error occured"
            else:
                return HttpResponseRedirect("/studentpayment")
    return render(request, "payment.html", {"amt": amt, "msg": msg})
######################################################################
#                      PAYMENT
######################################################################

def studentpayment(request):
    """ 
        The function to load  payment
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    s = "select tblconcession.*,tblcard.cardType from tblstudentdetails,tblconcession,tblcard where tblstudentdetails.sEmail='" + \
        email+"' and tblstudentdetails.cardId=tblcard.cardId and tblconcession.sdId=tblstudentdetails.sdId"
    c.execute(s)
    data = c.fetchall()
    return render(request, "studentpayment.html", {"data": data})
######################################################################
#                      STUDENT REGISTRATION
######################################################################


def studentreg(request):
    """ 
        The function to register student
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST["txtName"]
        age = request.POST["txtAge"]
        gender = request.POST["gender"]
        address = request.POST["txtAddress"]
        father = request.POST["txtFather"]
        email = request.POST["txtEmail"]
        number = request.POST["txtNumber"]
        pwd = request.POST["txtPassword"]
        inst = request.POST["inst"]
        s = "select inId from tblinstitute where inName='"+inst+"'"
        c.execute(s)
        i = c.fetchone()
        inid = i[0]
        admn = request.POST["txtAdmn"]
        q = "select count(*) as count from tblstudentregistration where sName='"+name+"'and sAge='"+age+"' and sAddress='"+address+"' and sGender='" + \
            gender+"' and sFather='"+father+"' and sEmail='"+email + \
            "' and sContact='"+number+"' and inId='"+inst+"' and admnNo='"+admn+"'"
        c.execute(q)
        i = c.fetchone()
        if(i[0] == 0):

            q = "select count(*) as count from tbllogin where uname='"+email+"'"
            c.execute(q)
            i = c.fetchone()
            if(i[0] == 0):
                q = "insert into tblstudentregistration(sName,sAge,sAddress,sGender,sFather,sEmail,sContact,inId,admnNo) values('"+str(name)+"','"+str(
                    age)+"','"+str(gender)+"','"+str(address)+"','"+str(father)+"','"+str(email)+"','"+str(number)+"','"+str(inid)+"','"+str(admn)+"')"
                c.execute(q)
                db.commit()
                q = "insert into tbllogin(uname,pwd,utype,status) values('" + \
                    email+"','"+pwd+"','student','0')"
                c.execute(q)
                db.commit()
        else:
            msg = "Already registered"
    s = "select * from tblinstitute where inEmail in (select uname from tbllogin where status='1')"
    c.execute(s)
    data = c.fetchall()
    return render(request, "studentreg.html", {"data": data, "msg": msg})
######################################################################
#                      INSTITUTE REGISTRATION
######################################################################


def institutereg(request):
    """ 
        The function to register institute
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        email = request.POST["txtEmail"]
        number = request.POST["txtNumber"]
        pwd = request.POST["txtPassword"]
        q = "select count(*) as count from tbllogin where uname='"+email+"'"
        c.execute(q)
        i = c.fetchone()
        if(i[0] == 0):
            q = "insert into tblinstitute(inName,inAddress,inContact,inEmail) values('" + \
                name+"','"+address+"','"+number+"','"+email+"')"
            c.execute(q)
            db.commit()
            q = "insert into tbllogin(uname,pwd,utype,status) values('" + \
                email+"','"+pwd+"','institute','0')"
            c.execute(q)
            db.commit()
    return render(request, "institutereg.html")


def studentcardgenerator(request):
    cid = request.GET.get("id")
    email = request.session["email"]
    q = "SELECT tblconcession.*, tblcard.cardType, tblstudentdetails.placeFrom, tblstudentdetails.placeTo, tblstudentregistration.sName, tblstudentregistration.sAge FROM tblstudentdetails, tblstudentregistration, tblconcession, tblcard WHERE tblstudentdetails.sEmail='" + \
        email+"' AND tblstudentdetails.cardId=tblcard.cardId AND tblconcession.sdId=tblstudentdetails.sdId AND tblconcession.cardId='"+cid+"' AND tblstudentregistration.sEmail='"+email+"'"
    c.execute(q)
    i = c.fetchone()

    # Create the PDF object using ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="concession_card_{cid}.pdf"'

    # Create a buffer to store the PDF
    buffer = BytesIO()

    # Create the PDF object using ReportLab with a specified buffer
    p = SimpleDocTemplate(buffer, pagesize=letter)

    # Set styles for the PDF
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    header_style = styles['Heading2']
    normal_style = styles['Normal']

    # Define custom styles
    custom_title_style = ParagraphStyle(
        'CustomTitle',
        parent=title_style,
        textColor=colors.darkblue,
        fontSize=18,
        spaceAfter=12,
    )

    # Define custom styles with colors and fonts
    custom_heading_style = ParagraphStyle(
        'CustomHeading',
        parent=header_style,
        textColor=colors.red,
        fontSize=14,
        spaceAfter=10,
    )
    custom_normal_style = ParagraphStyle(
        'CustomNormal',
        parent=normal_style,
        textColor=colors.black,
        fontSize=12,
        spaceAfter=8,
    )

    # Add content to the PDF
    content = [
        Paragraph("Kerala State Road Transport Cooperation Limited", custom_title_style),
        Paragraph("Student Concession Card", custom_heading_style),
        Paragraph("-----------------------------------------------", normal_style),
        Paragraph(f"<b>Student Full Name:</b> {i[9]}", custom_normal_style),
        Paragraph(f"<b>Concession Card ID:</b> RX-{i[0]}", custom_normal_style),
        Paragraph(f"<b>Student Registration Id:</b> {i[1]}", custom_normal_style),
        Paragraph(f"<b>Concession Valid From(Date):</b> {i[2]}", custom_normal_style),
        Paragraph(f"<b>Valid Upto(Date):</b> {i[3]}", custom_normal_style),
        Paragraph(f"<b>Payment Status:</b> {'Paid' if i[5] else 'Unpaid'}", custom_normal_style),
        Paragraph(f"<b>Concession Type:</b> {i[6]}", custom_normal_style),
        Paragraph(f"<b>From:</b> {i[7]}", custom_normal_style),
        Paragraph(f"<b>To:</b> {i[8]}", custom_normal_style),
        Paragraph(f"<b>Concession Amount:</b> {i[4]}", custom_normal_style),
        Paragraph(f"<b>Age:</b> {i[10]}", custom_normal_style),
        # Footer
        Paragraph("Computer Generated Card, No Digital Signature Required, Issued by MD KSRTC", custom_normal_style),
    ]

    # Build the PDF
    p.build(content)

    # Seek to the beginning of the buffer
    buffer.seek(0)

    # Set the response content type and read from the buffer
    response = HttpResponse(content=buffer.read(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="concession_card_{cid}.pdf"'

    return response
def studentgeneratecard(request):
    email = request.session["email"]
    s = "select tblconcession.*,tblcard.cardType from tblstudentdetails,tblconcession,tblcard where tblstudentdetails.sEmail='" + \
        email+"' and tblstudentdetails.cardId=tblcard.cardId and tblconcession.sdId=tblstudentdetails.sdId"
    c.execute(s)
    data = c.fetchall()
    return render(request, "studentgeneratecard.html", {"data": data})
    