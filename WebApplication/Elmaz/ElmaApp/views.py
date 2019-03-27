
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
from django.views.generic import TemplateView
from .models import Messages

# class HomeView(TemplateView,):
#     template_name = 'ElmaApp/index.html'


DEFAULT_TO = 'info@elmaztechnologies.co.zw'

class HomeView(TemplateView):

    def get(self, request):
        return render(self.request, 'ElmaApp/index.html')

    @staticmethod
    def post(request):

        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            send_mail(
                subject,
                message + '\n\n\n\n\n from {}'.format(email),
                email,
                [DEFAULT_TO],

                fail_silently=False,
            )

            contact_form = Messages()

            contact_form.name = name
            contact_form.email = email
            contact_form.subject = subject
            contact_form.message = message
            contact_form.save()

        return render(request, 'ElmaApp/index.html',{})

class Qform(TemplateView):

    def get(self, request):
        return render(request, 'ElmaApp/qform.html', {})

    @staticmethod
    def post(request):

        if request.method == 'POST':
            choices = []
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            contact = request.POST.get('contact')
            email = request.POST.get('email')
            company_name = request.POST.get('company_name')
            number_of_employees = request.POST.get('number_of_employees')
            additional_info = request.POST.get('additional_info')
            xpress = request.POST.get('xpress', None)
            partner = request.POST.get('partner', None)
            evolution = request.POST.get('evolution', None)
            quickbooks = request.POST.get('quickbooks', None)
            webdesign = request.POST.get('webdesign', None)
            fix = request.POST.get('fix', None)
            payroll = request.POST.get('payroll',None)
            pos = request.POST.get('pos', None)
            networking = request.POST.get('networking', None)
            icdl = request.POST.get('icdl', None)


            if xpress:
                choices.append('Xpress')

            if partner:
                choices.append('Partner')

            if evolution:
                choices.append('Evolution')

            if quickbooks:
                choices.append('QuickBooks')

            if webdesign:
                choices.append('Web Design')

            if fix:
                choices.append('Desktop & Laptop repair')


            if payroll:
                choices.append('payroll')

            if pos:
                choices.append('POS')

            if networking:
                choices.append('Networking')

            if icdl:
                choices.append('ICDL')
    

            send_mail(
                'Requesting a Quotation',
                '{} {}  \n company name: {} \n contact: {} \n additional infomation: {} \n Softwares: {} \n\n\n\n from: {}'.format(
                    name, surname, company_name, contact, additional_info, choices,email),

                email,
                [DEFAULT_TO],

                fail_silently=False,
                )

        return render(request, 'ElmaApp/qform.html', {})


class AccountingSolutionView(TemplateView):
    template_name = 'ElmaApp/AccountingSolutions.html'


class ProductsView(TemplateView):
    template_name = 'ElmaApp/products.html'


class DevelopmentView(TemplateView):
    template_name = 'ElmaApp/Development.html'

class SoftwareSolutioins(TemplateView):
    template_name = 'ElmaApp/SoftwareSolutions.html'

class ICTSolutioins(TemplateView):
    template_name = 'ElmaApp/ict.html'


class Training(TemplateView):
    template_name = 'ElmaApp/training.html'

class Support(TemplateView):
    template_name = 'ElmaApp/Support.html'

