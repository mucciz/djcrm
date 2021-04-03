from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
    )
from django.urls import reverse
from .models import Lead, Agent
from .forms import LeadModelForm, LeadForm


class LandingPageView(TemplateView):
    template_name = 'landing_page.html'


class LeadListView(ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadDetailView(DetailView):
    template_name = 'leads/lead_detail.html'
    model = Lead
    context_object_name = 'lead'


class LeadCreateView(CreateView):
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


class LeadUpdtaeView(UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    model = Lead


class LeadDeleteView(DeleteView):
    template_name = 'leads/lead_delete.html'
    model = Lead
    
    def get_success_url(self):
        return reverse('leads:lead_list')
