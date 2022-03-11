from django.contrib import admin

# Register your models here.
from .models import daily
from .models import reminder
from .models import objective
from .models import done

admin.site.register(daily)
admin.site.register(reminder)
admin.site.register(objective)
admin.site.register(done)
