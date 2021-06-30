from django.conf import settings
import json
from django.http import JsonResponse
from django.shortcuts import render
from ..forms import SignUpFormStore
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


