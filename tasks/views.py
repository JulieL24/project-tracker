from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from tasks.models import Task

# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["name", "start_date", "due_date", "project", "assignee"]
    template_name = "tasks/create_task.html"

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.project.pk])
