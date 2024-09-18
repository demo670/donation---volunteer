from django.shortcuts import redirect, render
from django.views import View
from .models import  Donor, Volunteer
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import Userform, DonorSignupForm, VolunteerSignupForm
# Create your views here.
def index(request):
    return render(request, "index.html")


def gallery(request):
    return render(request, "gallery.html")


def login_admin(request):
    return render(request, "login-admin.html")


def login_donor(request):
    return render(request, "login-donor.html")


def login_volunteer(request):
    return render(request, "login-volunteer.html")


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
        form2 = VolunteerSignupForm(request.POST, request.FILES)  # Make sure to include FILES for uploads

        if form1.is_valid() and form2.is_valid():  # Use 'and' instead of '&'
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
                return redirect('success_page')  # Redirect to a success page after creation
            except Exception as e:
                messages.warning(request, 'Profile Not Created: ' + str(e))
        else:
            messages.error(request, 'Please correct the errors below.')

        return render(request, "signup_volunteer.html", {'form1': form1, 'form2': form2})  # Return forms even if invalid
            


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


def logout(request):
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


def changepwd_donor(request):
    return render(request, "changepwd-donor.html")


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
