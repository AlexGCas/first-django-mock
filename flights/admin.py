from django.contrib import admin
from .models import Airport, Flight, Passenger
# Register your models here.
'''class AirportAdmin(admin.ModelAdmin):
    pass'''
class Flightadmin(admin.ModelAdmin):
    list_display = ('__str__', 'duration')
    pass
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ('flights',)
    pass
admin.site.register(Airport)
admin.site.register(Flight, Flightadmin)
admin.site.register(Passenger, PassengerAdmin)
