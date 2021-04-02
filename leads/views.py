from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Lead, Agent
from .forms import LeadModelForm, LeadForm


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads,
    }

    return render(request, 'leads/lead_list.html', context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        'lead': lead,
    }
    # print(reverse('leads:lead_detail', args=[pk]))
    return render(request, 'leads/lead_detail.html', context)


def lead_create(request):
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')

    else:
        form = LeadModelForm()

    context = {
        'form': form
    }
    return render(request, 'leads/lead_create.html', context)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    else:
        form = LeadModelForm(instance=lead)
    context = {
        'form': form,
        'lead': lead
    }

    return render(request, 'leads/lead_update.html', context)

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')
