from django.shortcuts import redirect, render
from django.views import View
from .models import  Donor, Volunteer, Donation
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import Userform, DonorSignupForm, VolunteerSignupForm, Loginform, MyPasswordChangeForm, DonateNowForm
from datetime import date, datetime
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


class changepwd_admin(View):
    def get(self,request):
        form = MyPasswordChangeForm(request.user)
        return render(request, "changepwd-admin.html", locals())
    def post(self,request):
        form = MyPasswordChangeForm(request.user, request.POST)
        if not request.user.is_authenticated:
            return redirect('login_volunteer')
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
        return render(request, "changepwd-admin.html", locals())


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
    if not request.user.is_authenticated:
        return redirect('/login-donor')
    user = request.user
    donor = Donor.objects.get(user=user)
    donationcount = Donation.objects.filter(donor=donor).count()
    acceptedcount = Donation.objects.filter(donor=donor,status="accept").count()
    rejectedcount = Donation.objects.filter(donor=donor,status="reject").count()
    pendingcount = Donation.objects.filter(donor=donor,status="pending").count()
    deliveredcount = Donation.objects.filter(donor=donor,status="Donation Delivered Successfully").count()
    return render(request, "index-donor.html",locals())


class donate_now(View):
    def get(self,request):
        form = DonateNowForm()
        return render(request, "donate-now.html",locals())
    def post(self, request):
        print("POST request received.")
        
        if not request.user.is_authenticated:
            print("User not authenticated, redirecting to login.")
            return redirect('/login-donor')

        form = DonateNowForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid. Processing donation...")
            user = request.user
            donor = Donor.objects.get(user=user)

            donationname = form.cleaned_data['donationname']
            donationpic = request.FILES['donationpic']
            collectionloc = form.cleaned_data['collectionloc']
            description = form.cleaned_data['description']

            try:
                Donation.objects.create(
                    donor=donor,
                    donationname=donationname,
                    donationpic=donationpic,
                    collectionloc=collectionloc,
                    description=description,
                    status="pending",
                    donationdate=date.today()
                )
                messages.success(request, 'Donation successful!')
                print("Donation created successfully.")
            except Exception as e:
                messages.warning(request, f'Failed to make a donation: {str(e)}')
                print(f"Error occurred: {e}")
        else:
            print("Form is not valid.")
            messages.error(request, 'Please correct the errors below.')

        print("Rendering form with errors.")
        return render(request, 'donate-now.html', {'form': form})


def donation_history(request):
    if not request.user.is_authenticated:
        return redirect('/login-donor')
    user = request.user
    donor = Donor.objects.get(user=user)
    donation = Donation.objects.filter(donor=donor)
    return render(request, "donation-history.html", locals())


class profile_donor(View):
    def get(self,request):
        form1 = Userform()
        form2 = DonorSignupForm()
        user = request.user
        donor = Donor.objects.get(user=user)
        return render(request, "profile-donor.html",locals())
    def post(self,request):
        if not request.user.is_authenticated:
            return redirect('/login-donor')
        form1 = Userform(request.POST)
        form2 = DonorSignupForm(request.POST)
        
        user = request.user
        donor = Donor.objects.get(user=user)
        
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        contact = request.POST['contact']
        address = request.POST['address']
        
        donor.user.first_name = fn
        donor.user.last_name = ln
        donor.contact = contact
        donor.address = address
        
        try:
            userpic = request.FILES['userpic']
            donor.userpic = userpic
            donor.save()
            donor.user.save()
            messages.success(request,'Profile Updated Successfully')
        except Exception as e:
            messages.warning(request, 'Profile Update Failed'+e)
        return render(request,"profile-donor.html",locals())
        


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


class changepwd_volunteer(View):
    def get(self,request):
        form = MyPasswordChangeForm(request.user)
        return render(request, "changepwd-volunteer.html", locals())
    def post(self,request):
        form = MyPasswordChangeForm(request.user, request.POST)
        if not request.user.is_authenticated:
            return redirect('login_volunteer')
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
        return render(request, "changepwd-volunteer.html", locals())


# view details
def donationdetail_donor(request, pid):
    if not request.user.is_authenticated:
        return redirect('/login-donor')
    donation = Donation.objects.get(id=pid)
    return render(request, "donationdetail-donor.html", locals())


def donationcollection_detail(request, pid):
    return render(request, "donationcollection-detail.html")


def donationrec_detail(request, pid):
    return render(request, "donationrec-detail.html")
