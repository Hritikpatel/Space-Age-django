from datetime import date
from django.shortcuts import *
from django.http import HttpResponse
from django.template import loader
from .models import *
import smtplib
import ssl

# Create your views here.

def mail():
    smtp_port = 587                 # Standard secure SMTP port
    smtp_server = "smtp.gmail.com"  # Google SMTP Server

    email_from = "customer.service@gmail.com"
    email_to = "dummy@gmail.com"

    pswd = "frlgqyzzqdddsaxcehkjr"

    # content of message

    message = "\
        Subject: testin'\
        Dear god, please help!!!"

    # Create context
    simple_email_context = ssl.create_default_context()


    try:
        # Connect to the server
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls(context=simple_email_context)
        TIE_server.login(email_from, pswd)
        print("Connected to server :-)")
        
        # Send the actual email
        print()
        print(f"Sending email to - {email_to}")
        TIE_server.sendmail(email_from, email_to, message)
        print(f"Email successfully sent to - {email_to}")

    # If there's an error, print it out
    except Exception as e:
        print(e)

    # Close the port
    finally:
        TIE_server.quit()




def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
def account(request):
    template = loader.get_template('LogIn.html')
    login_data = login.objects.all().values()
    if request.method == 'POST':
        username = request.POST["User Id"]
        password = request.POST["Password"]
        for index,data in enumerate(login_data):
            if data["email"] == username and data["password"] == password:
                return dashboard(request,data["id"])
    return HttpResponse(template.render())
def tour(request):
    template = loader.get_template('tour.html')
    return HttpResponse(template.render())
def gallery(request):
    template = loader.get_template('gallery.html')
    return HttpResponse(template.render())
def dashboard(request,loggeduser):
    data = personalinfo.objects.all().values()
    for _, info in enumerate(data):
        if info["id"] == loggeduser:
            data = info
    booking_data = booking.objects.all().values()
    usrtravelinfo = []
    for _, info in enumerate(booking_data):
        if int(loggeduser) == int(info["User_id"]):
            usrtravelinfo.append(info)
    context = {
    "data": data,
    "booking_data": usrtravelinfo,
    }
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render(context))
def blog(request):

    template = loader.get_template('Blog.html')
    blog_data = blogpost.objects.all().values()
    context = {
        "blog_data" : blog_data
        }
    return HttpResponse(template.render(context))
def f_pass(request):
    template = loader.get_template('fpass.html')
    return HttpResponse(template.render())
def sign_in(request):
    template = loader.get_template('joinus.html')
    return HttpResponse(template.render())
def signup(request):
    if request.method == 'POST':
        email=request.POST['email']
        pas=request.POST['pass']
        name=request.POST['name']
        gender = request.POST["gender"]
        phn = request.POST["phn"]
        adds = request.POST["adds"]
        login_data = login(email = email,password = pas)
        login_data.save()
        info = personalinfo(fullname = name, gender = gender, email = email, phn_no = phn, address = adds)
        info.save()
        
        return redirect("/account/")
def req(request):
    template = loader.get_template('LogIn.html')
    if request.method == "POST":
        action = request.POST.get("SubmitBtn")
        print(action)
        if action == "profupdate":
            id = request.POST["id"]
            name = request.POST["usrname"]
            gender = request.POST["gender"]
            email = request.POST["email"]
            phone = request.POST["phone"]
            address = request.POST["address"]
            contact = request.POST["emrcontact"]
            govid = request.POST["govid"]

            user_data = personalinfo.objects.filter(id=id).update(fullname = name, gender = gender, email = email, phn_no = phone, address = address, emergency_number = contact, gov_id = govid)
            return HttpResponse(template.render())
        elif action == "passupdate":
            id = request.POST["id"]
            CurrentPass = request.POST["CurrentPass"]
            user_id = request.POST["user_id"]
            pas = request.POST["pas"]

            login_data = login.objects.all().values()

            for _, data in enumerate(login_data):
                if data["email"] == user_id and data["password"] == CurrentPass:
                    login.objects.filter(id=id).update(email = user_id, password = pas)
                    return HttpResponse(template.render())
            else:
                return HttpResponse("Invaild input")
        elif action == "tour":
            template = loader.get_template('LogIn.html')

            user_id = request.POST["id"]
            email = request.POST["email"]
            name = request.POST["name"]
            contactinfo = request.POST["contactinfo"]
            pkgname = request.POST["package"]
            level = request.POST["level"]
            trans_id = request.POST["trans_id"]
            cost = request.POST["cost"]
            date = request.POST["date"]

            tour_data = booking(date = date, email = email,User_id = user_id, name = name, contactinfo = contactinfo, pkgname = pkgname, level = level, trans_id = trans_id, cost = cost)
            tour_data.save()
            return HttpResponse(template.render())
        elif action == "blog":
            title = request.POST["title"]
            body = request.POST["body"]
            username = request.POST["username"]
            # if body.isalnum() and title.isalnum():
            blog_data = blogpost(title = title, body = body, username = username)
            blog_data.save()
            return redirect("Blog")
        elif action == "contact":
            return HttpResponse("working")
        elif action == "f_pass":
            otp = 1234
            mail()
