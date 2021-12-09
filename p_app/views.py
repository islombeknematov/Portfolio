from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from p_app.forms import ContactModelForm


class ContactCreateView(CreateView):
    template_name = 'index.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('portfolio')


# def file(request):
#     context = {}
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         fs = FileSystemStorage()
#         name = fs.save(uploaded_file.name, uploaded_file)
#         url = fs.url(name)
#         context['url'] = fs.url(name)
#     return render(request, 'index.html', context)

