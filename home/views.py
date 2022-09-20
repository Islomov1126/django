import time
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .models import Book, Publisher
from .forms import LoginForm, RegisterForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views import View


# Create your views here.
class PublisherListView(ListView):
    model = Publisher
    template_name = 'publisher.html'

    def get_queryset(self):
        return Publisher.objects.filter(**self.request.GET.dict())


class PublisherCreateView(CreateView):
    model = Publisher
    fields = '__all__'
    template_name = 'add-publisher.html'
    success_url = reverse_lazy('publishers')


class PublisherDetialView(DetailView):
    model = Publisher
    template_name = 'publisher-view.html'


class PublisherDeleteView(DeleteView):
    model = Publisher
    success_url = reverse_lazy('publishers')
    template_name = 'publisher_confirm_delete.html'


class PublisherUpdateView(UpdateView):
    model = Publisher
    template_name = 'publisher-update.html'
    fields = '__all__'
    success_url = reverse_lazy('publishers')


class BookListView(ListView):
    model = Book
    template_name = 'index.html'

    def get_queryset(self):
        if len(self.request.GET.dict().items()) == 0:
            query = self.request.COOKIES.copy()
            if 'sessionid' in query:
                del query['sessionid']
            if 'csrftoken' in query:
                del query['csrftoken']
        else:
            query = self.request.GET.dict()
        
        return Book.objects.filter(**query)
    
    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        for key, val in self.request.GET.dict().items():
            response.set_cookie(key=key, value=val)
        return response


class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'add-book.html'
    success_url = reverse_lazy('index')


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('index')
    template_name = 'book_confirm_delete.html'


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book-view.html'
    fields = '__all__'
    success_url = reverse_lazy('index')


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, template_name='login.html', context={'form': form})
    else:
        from django.contrib.auth import login, authenticate
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect(reverse_lazy('index'))
        return render(request, template_name='login.html', context={'form': form, 'error_msg': 'Please, type correct user name and password'})

def logout_request(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect(reverse_lazy("index"))

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, template_name='register.html', context={'form': form})
    else:
        from django.contrib.auth import login, authenticate
        form = RegisterForm(data=request.POST)
        if form.is_valid():

            user = form.instance
            user.set_password(request.POST['password'])
            form.save()

            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user:
                login(request, user)
                return redirect(reverse_lazy('index'))
            return render(request, template_name='register.html', context={'form': form, 'error_msg': 'Please, type correct user name and password'})
        
        return render(request, template_name='register.html', context={'form': form})