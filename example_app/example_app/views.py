from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
import pandas as pd
import numpy as np
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime
from tablib import Dataset
from django.contrib.auth.decorators import login_required

from comcaan.decorators import unauthenticated_user, allowed_users

# Create your views here.
@login_required(login_url="/accounts/login/")
@allowed_users(allowed_roles=['casino analyst'])
def base(request):
    print('testing example_app')
    return render(request, "example_app/base.html", {"my_var":"Tableau Example"})
