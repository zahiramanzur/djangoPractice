from django.views.generic.base import TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class CreateNewTask(FormView, LoginRequiredMixin):
    template_name = 'index.html'

