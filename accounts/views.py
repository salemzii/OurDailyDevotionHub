
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import LoginForm, SignUpForm, UserProfileUpdateForm
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import account_activation_token
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from .models import Profile
from django.views.generic import UpdateView


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            mail = form.cleaned_data.get('email')
            form.save()

            userr = User.objects.get(username=username)
            userr.is_active = True
            userr.save()
            userr_profile = Profile.objects.create(
                user = userr,
                bio = 'profile created!'
            )
            userr_profile.save()

            uidb64 = urlsafe_base64_encode(force_bytes(userr.pk))

            domain = get_current_site(request).domain
            link = reverse('activate',kwargs={'uidb64': uidb64, 'token': account_activation_token.make_token(userr)})
            activate_url = 'http://' + domain + link
            email_subject = 'Activate your account'
            email_body = 'Hello {0} thanks for signing up with us, please use this link to verify your account \n {1}'.format(
                username, activate_url)

            email = send_mail(email_subject, email_body, 'Noreply@FX.com', [mail], fail_silently= True)
            messages.success(request, f'Congrats {username}, Your account was created successfully')

            return redirect('verify')
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})



def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})


def home(request):
    return render(request, 'accounts/home.html')


def verify(request):
    return render(request, 'accounts/verify.html')


@login_required
def profile(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def update_profile(request):

    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile', args=[request.user.id]))
    else:
        form = UserProfileUpdateForm(instance=user_profile)
    return render(request, 'accounts/updateprofile.html', {'form': form})


class verification(View):
    def get(self, request, uidb64, token):

        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login' + '?message' + 'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')
        except Exception as e:
            pass
        return redirect('login')
