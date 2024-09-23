from django import forms
from django.shortcuts import render, redirect
from django.core.mail import send_mail, get_connection


class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=120)
    email = forms.EmailField(required=False)
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        # con = get_connection('django.core.mail.backends.console.EmailBackend')
        send_mail(
            data['subject'],
            data['message'],
            data.get('email', 'noreply@example.com'),
            ['siteowner@example.com']
        )
        return redirect('contact_us')
    return render(request, 'contact/contact.html', {'form': form})
