from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Application, Subscription, Category


@login_required
def subscription_page(request):
    all_applications = Application.objects.all()
    user_subscriptions = Subscription.objects.filter(user=request.user)
    subscribed_applications = [sub.application for sub in user_subscriptions]

    context = {
        'all_applications': all_applications,
        'subscribed_applications': subscribed_applications
    }
    return render(request, 'subscriptions/subscription_page.html', context)


@login_required
def subscribe(request, app_id):
    application = get_object_or_404(Application, id=app_id)
    Subscription.objects.get_or_create(user=request.user, application=application)
    return redirect('subscription_page')

@login_required
def unsubscribe(request, app_id):
    subscription = Subscription.objects.filter(user=request.user, application_id=app_id)
    if subscription.exists():
        subscription.delete()
    return redirect('subscription_page')

def signup(request):
    if request.user.is_authenticated:
        # Redirect logged-in users directly to the subscription page
        return redirect('subscription_page')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            return redirect('subscription_page')  # Redirect to subscription page
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
