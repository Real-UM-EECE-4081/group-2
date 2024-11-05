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
