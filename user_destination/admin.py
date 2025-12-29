from django.contrib import admin

from .models import user_journey_record



@admin.register(user_journey_record)
class userJourneyRecord(admin.ModelAdmin):
    list_display =(
        'id',
        'user',
        'destination_from',
        'destination_to'
    )