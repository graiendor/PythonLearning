import os

from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from .models import Roll, Attributes
from .scripts.roll import __roll__, __dices__
from .scripts.attributes import __attributes__
from django.core import serializers
from .forms import AttributesForm, RollForm
import json


class Roller(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.renderer_classes = [TemplateHTMLRenderer]
        self.template_name = "dice/dice_page.html"
        self.roll = Roll()
        self.attributes = AttributesForm()

    def get(self, request):
        return Response({'roll': self.roll, 'attributes': self.attributes})

    def post(self, request):
        self.attributes = AttributesForm(request.POST)

        if self.attributes.is_valid():
            self.attributes.save()
        dices = __dices__(self.attributes.cleaned_data)
        if 'roll_btn' in request.POST:
            __roll__(self.roll, dices)
        return Response({'roll': self.roll, 'attributes': self.attributes})



