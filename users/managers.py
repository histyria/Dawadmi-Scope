from django.db import models
from django.db.models import Q
from django.shortcuts import render , get_object_or_404
from home.models import *
class Support_TeamManager(models.Manager):

    def get_section(self , section_id):
        dep_id = get_object_or_404(DEPARTEMNTS, id=section_id.id)
        print(dep_id)
        return dep_id