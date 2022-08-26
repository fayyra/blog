from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import TemplateView
from .forms import BlogCreateForm, CommentForm, BlogUpdateForm, SignUpForm, UserForm, ProfileForm
from .models import Blog, Comment, Profile
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    num_blogs = Blog.objects.count()
    user_count = User.objects.count()

    context = {'num_blogs': num_blogs,
               'user_count': user_count
               }

    return render(request, 'index.html', context=context)


class BlogsListView(generic.ListView):
    model = Blog
    paginate_by = 10
    context_object_name = 'blogs_list'


class BlogDetail(generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['comment_form'] = CommentForm()
        return context


class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogCreateForm

    def post(self, request, *args, **kwargs):
        data = request.POST
        form = self.form_class(data, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author_id = request.user.id
            form.save()
            return redirect(reverse_lazy('blog-detail', kwargs={'pk': form.id}))

        context = {'form': form}
        return render(request, 'main/blog_form.html', context=context)


class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogUpdateForm


class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs')


def myblogs_list(request):
    blogs = Blog.objects.filter(author=request.user)
    paginate_by = 5

    return render(request, 'main/myblogs_list.html', context={"myblogs": blogs, "paginate_by": paginate_by})


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'main/blog_detail.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        super().form_valid(form)
        return redirect('blog-detail', self.kwargs['pk'])


class UserRegisterView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        return HttpResponseRedirect(reverse_lazy('login'))


class BloggerDetail(generic.DetailView):
    model = Profile
    template_name = 'main/blogger_detail.html'


class ProfileUpdate(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'registration/profile_edit.html'

    def dispatch(self, request, *args, **kwargs):
        post_data = request.POST or None

        user_form = self.user_form(post_data, instance=request.user)
        profile_form = self.profile_form(post_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse_lazy('profile', kwargs={'pk': request.user.profile.id}))

        context = {'user_form': user_form,
                   'profile_form': profile_form}

        return render(request, 'registration/profile_edit.html', context=context)
