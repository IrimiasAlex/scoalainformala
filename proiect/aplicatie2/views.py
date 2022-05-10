from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from aplicatie2.models import Companies


class CompanyView(ListView):
    model = Companies
    template_name = 'aplicatie2/Companies_index.html'

    def get_context_data(self, *args, **kwargs):
        data = super(CompanyView, self).get_context_data()
        data['companies_list'] = self.model.objects.filter(active=1)
        return data


class CreateCompanyView(LoginRequiredMixin, CreateView):
    model = Companies
    fields = ['name', 'company_type', 'website', 'active']
    template_name = 'aplicatie2/Companies_form.html'

    def get_success_url(self):
        return reverse('companies:listare')


class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    model = Companies
    fields = ['name', 'company_type', 'website', 'active']
    template_name = 'aplicatie2/Companies_form.html'

    def get_success_url(self):
        return reverse('companies:listare')


@login_required
def delete_company(request, pk):
    Companies.objects.filter(id=pk).update(active=0)
    return redirect('companies:listare')


@login_required
def activate_company(request, pk):
    Companies.objects.filter(id=pk).update(active=1)
    return redirect('companies:listare')


class CompanyInactiveViews(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'aplicatie2/Companies_index.html'

    def get_context_data(self, *args, **kwargs):
        data = super(CompanyInactiveViews, self).get_context_data()
        data['companies_list'] = self.model.objects.filter(active=0)
        return data


@login_required
def activate_company(request, pk):
    Companies.objects.filter(id=pk).update(active=1)
    return redirect('companies:companii_inactive')
