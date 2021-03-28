from django.shortcuts import render
from django.views.generic import ListView, DetailView
# (Seungeon)
from users.models import Profile


def home(request):
    return render(request, 'social_app/home.html')

# (Seungeon)
# by default,
# url : <app>/<model>_<viewtype>.html
# in our case, 'users/profile_list.html'


class ProfileListView(ListView):
    # this behaves same as model = Profile.objects.get.all()
    model = Profile
    # The template_name attribute is used to tell Django to use a specific template name
    # instead of the autogenerated default template name
    template_name = 'social_app/home.html'
    # Designates the name of the variable to use in the context.
    # from Django official Docs
    # https://docs.djangoproject.com/en/3.1/ref/class-based-views/mixins-single-object/
    context_object_name = 'profiles'
    # ordering = [-some attribute] <- this will order it by whatever attribute in models.py specified

    def get_queryset(self):
        queryset = Profile.objects.all()
        return queryset


def profile_detail_view(request, pk):
    profile = Profile.objects.get(user__pk=pk)
    context = {"profile": profile}
    return render(
        request=request,
        template_name='social_app/detail.html',
        context=context,
    )


def about(request):
    return render(
        request=request,
        template_name='social_app/about.html'
    )
