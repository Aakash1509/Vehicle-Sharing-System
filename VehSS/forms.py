from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
from django import forms
# from django.contrib.auth.models import User
# from .models import Article
from .models import Owner
from .models import Traveller
from .models import Summary
# from .models import Traveller
# from .models import Manager

class OwnerForm(ModelForm):
    class Meta:
        model=Owner
        fields=('name','email','location','carname','seats','phone','date_time','image')

class TravellerForm(ModelForm):
    class Meta:
        model=Traveller
        fields=('name','email','location','phone','date_time')

class SummaryForm(ModelForm):
    class Meta:
        model=Summary
        fields=('traveller_name','owner_name','email','location','phone','date_time')

