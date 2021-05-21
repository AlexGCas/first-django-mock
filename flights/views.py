from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Airport, Flight, Passenger
from .forms import NewPassengerForm
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        'flights': Flight.objects.all()
    })
def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights=flight)
    choices = set([(non_passengers[i].id, non_passengers[i]) for i in range(len(non_passengers))])
    kwargs = {'choices': choices}
    form = NewPassengerForm(**kwargs)
    return render(request, "flights/flight.html",
                  {'flight': flight,
                   'passengers': passengers,
                   'non_passengers': non_passengers,
                   'form': form})
def book(request, flight_id):
    if request.method == "POST":
        passenger_id = request.POST.get('passenger')
        flight = Flight.objects.get(pk=flight_id)
        Passenger.objects.get(pk=passenger_id).flights.add(flight)
        return HttpResponseRedirect(reverse('flight', args=(flight_id,)))

