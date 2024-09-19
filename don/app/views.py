from django.shortcuts import redirect, render
from django.views import View
from .models import  Donor, Volunteer
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import Userform, DonorSignupForm, VolunteerSignupForm, Loginform, MyPasswordChangeForm
# Create your views here.
def index(request):
    return render(request, "index.html")


def gallery(request):
    return render(request, "gallery.html")


class login_admin(View):
    def get(self,request):
        form = Loginform()
        return render(request, "login-admin.html", locals())
    def post(self, request):
        form = Loginform(request.POST)
        us = request.POST['username']
        pwd = request.POST['password']
        try:
            user = authenticate(username=us, password=pwd)
            if user:
                if user.is_staff:
                    login(request, user)
                    return redirect('/index-admin')
                else:
                    messages.warning(request,'Invalid Admin User')
            else:
                messages.warning(request,'Invalid username and password')
        except:
            messages.warning(request,'Login Failed')
        return render(request, "login-admin.html", locals())



class login_donor(View):
    def get(self,request):
        form = Loginform()
        return render(request, "login-donor.html", locals())
    def post(self, request):
        form = Loginform(request.POST)
        us = request.POST['username']
        pwd = request.POST['password']
        try:
            user = authenticate(username=us, password=pwd)
            if user:
                donor_user = Donor.objects.filter(user_id=user.id)
                if donor_user:
                    login(request, user)
                    return redirect('/index-donor')
                else:
                    messages.warning(request,'Invalid Donor User')
            else:
                messages.warning(request,'Invalid username and password')
        except:
            messages.warning(request,'Login Failed')
        return render(request, "login-donor.html", locals())
                


class login_volunteer(View):
    def get(self,request):
        form = Loginform()
        return render(request, "login-volunteer.html", locals())
    def post(self, request):
        form = Loginform(request.POST)
        us = request.POST['username']
        pwd = request.POST['password']
        try:
            user = authenticate(username=us, password=pwd)
            if user:
                vol_user =Volunteer.objects.filter(user_id=user.id)
                if vol_user:
                    login(request, user)
                    return redirect('/index-volunteer')
                else:
                    messages.warning(request,'Invalid Donor User')
            else:
                messages.warning(request,'Invalid username and password')
        except:
            messages.warning(request,'Login Failed')
        return render(request, "login-volunteer.html", locals())


class signup_donor(View):
    def get(self,request):
        form1 = Userform()
        form2 = DonorSignupForm()
        return render(request, "signup_donor.html",locals())
    def post(self,request):
        form1 = Userform(request.POST)
        form2 = DonorSignupForm(request.POST)
        if form1.is_valid() & form2.is_valid():
            fn = request.POST["first_name"]
            ln = request.POST["last_name"]
            em = request.POST["email"]
            us = request.POST["username"]
            pwd = request.POST["password1"]
            contact = request.POST["contact"]
            userpic = request.FILES["userpic"]
            address = request.POST["address"]
            
            try:
                user=User.objects.create_user(first_name=fn, last_name=ln, email=em, username=us, password=pwd)
                Donor.objects.create(user=user , contact=contact , userpic=userpic , address=address)
                messages.success(request, 'Congratulations!! Donor Profile Created ')
            except:
                messages.warning(request, 'Profile Not Created')
            
        return render(request, "signup_donor.html", locals())


class  signup_volunteer(View):
    def get(self, request):
        form1 = Userform()
        form2 = VolunteerSignupForm()
        return render(request, "signup_volunteer.html", {'form1': form1, 'form2': form2})

    def post(self, request):
        form1 = Userform(request.POST)
        form2 = VolunteerSignupForm(request.POST, request.FILES) 

        if form1.is_valid() and form2.is_valid():  
            fn = request.POST['first_name']
            ln = request.POST["last_name"]
            em = request.POST["email"]
            us = request.POST["username"]
            pwd = request.POST["password1"]
            contact = request.POST["contact"]
            userpic = request.FILES["userpic"]
            idpic = request.FILES['idpic']
            address = request.POST["address"]
            aboutme = request.POST['aboutme']
            
            try:
                user = User.objects.create_user(first_name=fn, last_name=ln, email=em, username=us, password=pwd)
                Volunteer.objects.create(user=user, contact=contact, userpic=userpic, idpic=idpic, address=address, aboutme=aboutme, status='pending')
                messages.success(request, 'Congratulations!! Volunteer Profile Created ')
                return redirect('login_volunteer')
            except Exception as e:
                messages.warning(request, 'Profile Not Created: ' + str(e))
        else:
            messages.error(request, 'Please correct the errors below.')

        return render(request, "signup_volunteer.html", {'form1': form1, 'form2': form2}) 
            


def index_admin(request):
    return render(request, "index-admin.html")



# admin dashboard
def pending_donation(request):
    return render(request, "pending-donation.html")


def accepted_donation(request):
    return render(request, "accepted-donation.html")


def rejected_donation(request):
    return render(request, "rejected-donation.html")


def volunteerallocated_donation(request):
    return render(request, "volunteerallocated-donation.html")


def donationrec_admin(request):
    return render(request, "donationrec-admin.html")


def donationnotrec_admin(request):
    return render(request, "donationnotrec-admin.html")


def donationdelivered_admin(request):
    return render(request, "donationdelivered-admin.html")


def all_donations(request):
    return render(request, "all-donations.html")


def manage_donor(request):
    return render(request, "manage-donor.html")


def new_volunteer(request):
    return render(request, "new-volunteer.html")


def accepted_volunteer(request):
    return render(request, "accepted-volunteer.html")


def rejected_volunteer(request):
    return render(request, "rejected-volunteer.html")


def all_volunteer(request):
    return render(request, "all-volunteer.html")


def add_area(request):
    return render(request, "add-area.html")


def edit_area(request, pid):
    return render(request, "edit-area.html")


def manage_area(request):
    return render(request, "manage-area.html")


def changepwd_admin(request):
    return render(request, "changepwd-admin.html")


def logoutview(request):
    logout(request)
    return redirect("index")


# admin view details
def accepted_donationdetail(request, pid):
    return render(request, "accepted-donationdetail.html")


def view_volunteerdetail(request, pid):
    return render(request, "view-volunteerdetail.html")


def view_donordetail(request, pid):
    return render(request, "view-donordetail.html")


def view_donationdetail(request, pid):
    return render(request, "view-donationdetail.html")


# donor dashboard
def index_donor(request):
    return render(request, "index-donor.html")


def donate_now(request):
    return render(request, "donate-now.html")


def donation_history(request):
    return render(request, "donation-history.html")


def profile_donor(request):
    return render(request, "profile-donor.html")


class changepwd_donor(View):
    def get(self,request):
        form = MyPasswordChangeForm(request.user)
        return render(request, "changepwd-donor.html", locals())
    def post(self,request):
        form = MyPasswordChangeForm(request.user, request.POST)
        if not request.user.is_authenticated:
            return redirect('/login-donor')
        old = request.POST['old_password']
        newpass = request.POST['new_password1']
        confirmpass = request.POST['new_password2']
        try:
            if newpass == confirmpass:
                user = User.objects.get(id=request.user.id)
                if user.check_password(old):
                    user.set_password(newpass)
                    user.save()
                    messages.success(request, 'Change Password Successfully')
                else:
                    messages.warning(request, 'Old Password not matched')
            else:
                messages.warning(request, 'Old Password and New Password are different')
        except:
            messages.warning(request, 'Failed to Change Password')
        return render(request, "changepwd-donor.html", locals())


# volunteer dashboard
def index_volunteer(request):
    return render(request, "index-volunteer.html")


def collection_req(request):
    return render(request, "collection-req.html")


def donationrec_volunteer(request):
    return render(request, "donationrec-volunteer.html")


def donationnotrec_volunteer(request):
    return render(request, "donationnotrec-volunteer.html")


def donationdelivered_volunteer(request):
    return render(request, "donationdelivered-volunteer.html")


def profile_volunteer(request):
    return render(request, "profile-volunteer.html")


def changepwd_volunteer(request):
    return render(request, "changepwd-volunteer.html")


# view details
def donationdetail_donor(request, pid):
    return render(request, "donationdetail-donor.html")


def donationcollection_detail(request, pid):
    return render(request, "donationcollection-detail.html")


def donationrec_detail(request, pid):
    return render(request, "donationrec-detail.html")
