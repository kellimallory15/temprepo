import stripe as stripe
from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView

from .forms import OrderForm
from .models import PhotographySession, Booking
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


def index(request):

    context = {

    }

    return render(request, 'index.html', context=context)


def senior_about(request):
    return render(request, 'senior_about.html')


def family_about(request):
    return render(request, 'family_about.html')


def couples_engagements_about(request):
    return render(request, 'couples_engagements_about.html')


def calendar(request):
    return render(request, 'calendar.html')


class CalendarView(generic.DetailView):
    model = Booking


def view_cart(request):
    cart = request.session.get('cart', [])  # Get the cart from the session
    sessions_in_cart = PhotographySession.objects.filter(id__in=cart)

    return render(request, 'shopping_cart.html', {'sessions_in_cart': sessions_in_cart})


stripe.api_key = settings.STRIPE_SECRET_KEY


def create_booking(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            amount = form.cleaned_data['amount'] * 100  # Convert to cents

            # Create a Stripe PaymentIntent
            payment_intent = stripe.PaymentIntent.create(
                amount=int(amount),
                currency='usd',
                description=product_name
            )

            return render(request, 'payment.html', {'client_secret': payment_intent.client_secret})

    else:
        form = OrderForm()

    return render(request, 'order_information_input.html', {'form': form})
