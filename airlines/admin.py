from django.contrib import admin
from .models import AirCompany, Rotating, Command, Food, Image, Flight,HotFood


class AirCompanyInline(admin.TabularInline):
    model = Flight.air_company.through

class CommandInline(admin.TabularInline):
    model = Flight.command.through

class RotatingInline(admin.TabularInline):
    model = Flight.rotating.through

class FoodInline(admin.TabularInline):
    model = Flight.food.through

class HotFoodLine(admin.TabularInline):
    model = Flight.hotfood.through

class ImageInline(admin.TabularInline):
    model = Flight.image.through

class FlightAdmin(admin.ModelAdmin):
    inlines = [AirCompanyInline, CommandInline, RotatingInline, FoodInline,HotFoodLine, ImageInline]
    exclude = ('air_company', 'command', 'rotating','food', 'hotfood','image')
    list_display = ('flight_number', 'air_companies_list')

    def flight_number(self, obj):
        return f"Flight {obj.pk}"

    def air_companies_list(self, obj):
        return ', '.join([str(ac) for ac in obj.air_company.all()])

    air_companies_list.short_description = 'Air Companies'

admin.site.register(AirCompany)
admin.site.register(Command)
admin.site.register(Rotating)
admin.site.register(Food)
admin.site.register(HotFood)
admin.site.register(Image)
admin.site.register(Flight, FlightAdmin)
