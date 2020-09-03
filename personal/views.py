from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from . import forms
# from braces.views import SelectRelatedMixin
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()
from django.contrib import messages

from django.http import JsonResponse
from django.forms.models import model_to_dict


def handler404(request, *args, **argv):
    return render(request, '404.html', status=404)


def handler500(request, *args, **argv):
    return render(request, '404.html', status=404)


def blogList(request):
    me = models.UserProfile.objects.get(user__username="mayank")
    articles = models.Blog.objects.filter(user__username="mayank")
    context = {"profile": me, "posts": articles}
    print(articles)
    return render(request, 'bloglist.html', context)


class blogDetail(DetailView):
    model = models.Blog

    template_name = 'blog_detail.html'


def index(request):
    me = models.UserProfile.objects.get(user__username="mayank")
    projects = models.Project.objects.filter(user__username='mayank')
    works = models.Work.objects.filter(user__username='mayank')
    quotes = models.Intro.objects.filter(user__username='mayank')

    c = {"profile": me, "projects": projects, "works": works, "quotes": quotes}
    return render(request, 'index.html', c)


class CreateProject(LoginRequiredMixin, CreateView):
    fields = ['name', 'date', 'short_description', 'full_description', 'link', 'cover']
    template_name = 'projectForm.html'
    model = models.Project

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class CreateArticle(LoginRequiredMixin, CreateView):
    fields = ['title', 'cover', 'content']
    template_name = 'newblog.html'
    model = models.Blog

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class deleteArticle(LoginRequiredMixin, DeleteView):
    model = models.Blog
    success_url = reverse_lazy("bloglist")
    template_name = 'deleteBlog.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "article Deleted")
        return super().delete(*args, **kwargs)


class updateArticle(LoginRequiredMixin, UpdateView):
    model = models.Blog
    fields = ['title', 'cover', 'content']
    success_url = reverse_lazy('bloglist')
    template_name = 'updateBlog.html'


class CreateWork(LoginRequiredMixin, CreateView):
    fields = ['position', 'company', 'start_date', 'end_date', 'full_description', 'cover']
    template_name = 'workForm.html'
    model = models.Work

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class CreateQuote(LoginRequiredMixin, CreateView):
    fields = ['quote']
    template_name = 'quoteForm.html'
    model = models.Intro

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeleteProject(LoginRequiredMixin, DeleteView):
    model = models.Project
    success_url = reverse_lazy("personal-index")
    template_name = 'deleteProject.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Project Deleted")
        return super().delete(*args, **kwargs)


class DeleteWork(LoginRequiredMixin, DeleteView):
    model = models.Work
    success_url = reverse_lazy("personal-index")
    template_name = 'deleteWork.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Work Experience Deleted")
        return super().delete(*args, **kwargs)


class UpdateProject(LoginRequiredMixin, UpdateView):
    model = models.Project
    fields = ['name', 'date', 'short_description', 'full_description', 'link', 'cover']
    success_url = reverse_lazy('personal-index')
    template_name = 'updateProject.html'


class UpdateWork(LoginRequiredMixin, UpdateView):
    model = models.Work
    fields = ['position', 'company', 'start_date', 'end_date', 'full_description', 'cover']
    success_url = reverse_lazy('personal-index')
    template_name = 'updateWork.html'


def EditProfile(request):
    if request.method == "POST":
        user_form = forms.UserEditForm(request.POST, instance=request.user)
        profile_form = forms.UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            profile = profile_form.save(commit=False)
            profile.user = user
            print(request.FILES)
            if 'profile_pic' in request.FILES:
                print('got a picture')
                profile.profile_pic = request.FILES['profile_pic']

            user.save()
            profile.save()
            return redirect(reverse_lazy('personal-index'))
    else:
        profile_form = forms.UserProfileForm(instance=request.user.userprofile)
        user_form = forms.UserEditForm(instance=request.user)

        return render(request, 'EditProfile.html', {'u_form': user_form,
                                                    'p_form': profile_form})
