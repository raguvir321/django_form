from django.shortcuts import render
from django.http import HttpResponse
from .form import ContactForm, SnippetForm

def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print(name,email)
    else:

        form = ContactForm()
    return render(request,'form.html',{'form':form})


def snippet_detail(request):


    if request.method == "POST":
        form = SnippetForm(request.POST)

        if form.is_valid():

            form.save()



    form = SnippetForm()
    return render(request,'add.html',{'form':form})
