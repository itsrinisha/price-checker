from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .models import Link
from .forms import AddLinkForm


def home(request):
    discounted_items = 0
    error = 0
    form = AddLinkForm(request.POST or None)
    no_discounted=0
    if request.method == "POST":
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Couldn;t get the name/price"
        except:
            error = "Something went wrong"

    form = AddLinkForm()
    qs = Link.objects.all()
    items_no = qs.count()
    if items_no > 0:
        discount_list = []
        for item in qs:
            if item.old_price > item.current_price:
                discount_list.append(item)
            no_discounted = len(discount_list)

    context = {
        "qs": qs,
        "items_no": items_no,
        "no_discounted": no_discounted,
        "form": form,
        "error": error,
    }
    return render(request, "home.html", context)


def update_prices(request):
    qs = Link.objects.all()
    for link in qs:
        link.save()
    return redirect("home")


class LinkDeleteView(DeleteView):
    model = Link
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("home")
