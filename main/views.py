from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project, Client, Contact, Subscriber
from .forms import (
    ContactForm, SubscriberForm,
    ProjectForm, ClientForm
)


def home(request):
    projects = Project.objects.all().order_by('-id')[:6]
    clients = Client.objects.all().order_by('-id')[:6]

    contact_form = ContactForm()
    subscriber_form = SubscriberForm()

    if request.method == 'POST':
        if 'contact_submit' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, "Thanks! We will contact you soon.")
                return redirect('home')
        elif 'newsletter_submit' in request.POST:
            subscriber_form = SubscriberForm(request.POST)
            if subscriber_form.is_valid():
                subscriber_form.save()
                messages.success(request, "Subscribed successfully!")
                return redirect('home')
        elif 'consultation_submit' in request.POST:
            # Handle consultation form submission
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            # You can save this to a model or send an email
            messages.success(request, "Thank you for your interest! We will contact you soon.")
            return redirect('home')

    context = {
        'projects': projects,
        'clients': clients,
        'contact_form': contact_form,
        'subscriber_form': subscriber_form
    }
    return render(request, 'home.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks! We will contact you soon.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# ---------- Simple Custom Admin Panel ----------

@login_required
def admin_dashboard(request):
    projects_count = Project.objects.count()
    clients_count = Client.objects.count()
    contacts_count = Contact.objects.count()
    subs_count = Subscriber.objects.count()

    return render(request, 'admin/dashboard.html', {
        'projects_count': projects_count,
        'clients_count': clients_count,
        'contacts_count': contacts_count,
        'subs_count': subs_count,
    })


@login_required
def admin_projects(request):
    projects = Project.objects.all().order_by('-id')
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Project added successfully.")
            return redirect('admin_projects')
    else:
        form = ProjectForm()

    return render(request, 'admin/projects.html', {
        'form': form,
        'projects': projects,
    })


@login_required
def admin_clients(request):
    clients = Client.objects.all().order_by('-id')
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Client added successfully.")
            return redirect('admin_clients')
    else:
        form = ClientForm()

    return render(request, 'admin/clients.html', {
        'form': form,
        'clients': clients,
    })


@login_required
def admin_contacts(request):
    contacts = Contact.objects.all().order_by('-created_at')
    return render(request, 'admin/contacts.html', {'contacts': contacts})


@login_required
def admin_subscribers(request):
    subs = Subscriber.objects.all().order_by('-created_at')
    return render(request, 'admin/subscribers.html', {'subs': subs})
