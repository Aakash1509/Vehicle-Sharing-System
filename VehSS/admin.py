from django.contrib import admin

# Register your models here.
from .models import Owner
from .models import Summary
# from .models import Traveller
# from .models import Manager
# from .models import Traveller

admin.site.register(Owner)
admin.site.register(Summary)

