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
