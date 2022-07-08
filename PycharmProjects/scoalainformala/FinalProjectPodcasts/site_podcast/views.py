from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView

from site_podcast.models import Podcasts


class PodcastView(LoginRequiredMixin, ListView):
    model = Podcasts
    template_name = "site_podcast/Podcasts_index.html"

    queryset = model.objects.all()
    context_object_name = 'podcasts'

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data()
        return data


@login_required
def cautare(request):
    if request.method == "POST":
        cautat = request.POST["cautat"]
        variabila = Podcasts.objects.filter(searching__icontains=cautat)
        return render(request, "site_podcast/cautare.html", {"cautat": cautat, 'variabila': variabila})
    else:
        return render(request, "site_podcast/cautare.html", {})


def podcast_detail_view(request, pk):
    podcast = get_object_or_404(Podcasts, id=pk)
    return render(request, 'site_podcast/displayphoto.html', context={'podcast': podcast})


@login_required
def categories(request):
    if request.method == "POST":
        categorii = request.POST["categorii"]
        alta_variabila = Podcasts.objects.filter(categories__icontains=categorii)
        return render(request, "site_podcast/categories.html",
                      {"categorii": categorii, 'alta_variabila': alta_variabila})
    else:
        return render(request, "site_podcast/categories.html", {})
