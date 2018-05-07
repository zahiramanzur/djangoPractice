# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# class CreateTask(, ):


@login_required
def index(request):
    # import ipdb; ipdb.set_trace()
    return render(request, 'task/index.html')


def profile(request):
    username = None
    if request.user.is_staff:
        return redirect('/admin/')
    else:
        return render(request, 'accounts/profile/index.html', {})
