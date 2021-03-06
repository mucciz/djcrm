from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, CreateView
)
from django.urls import reverse
from .models import Lead, Agent
from .forms import LeadModelForm, LeadForm, CustomUserCreationForm


class SignUpView(CreateView):
    template_name = 'registration/sign_up.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')


class LandingPageView(TemplateView):
    template_name = 'landing_page.html'


class LeadListView(LoginRequiredMixin,ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadDetailView(LoginRequiredMixin,DetailView):
    template_name = 'leads/lead_detail.html'
    model = Lead
    context_object_name = 'lead'


class LeadCreateView(LoginRequiredMixin,CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead_list')

    def form_valid(self, form):
        send_mail(
            subject='A lead has been created',
            message='Go to the site to check it out',
            from_email='test@testUser.com',
            recipient_list=['test@testAdmin.com'],
            fail_silently=False
        )
        return super().form_valid(form)


class LeadUpdtaeView(LoginRequiredMixin,UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    model = Lead


class LeadDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'leads/lead_delete.html'
    model = Lead

    def get_success_url(self):
        return reverse('leads:lead_list')
