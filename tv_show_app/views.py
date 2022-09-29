from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages


def index(request):
    return redirect("/shows")


def view_shows(request):
    # print(Show.objects.all())
    context = {
        "shows": Show.objects.all(),
    }
    return render(request, "index.html", context)


def add_new_show_page(request):
    return render(request, "add_show.html")


def create_show(request):

    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect("/shows/new")

    created_show = Show.objects.create(
        title=request.POST["title"],
        network=request.POST["network"],
        release_date=request.POST["release_date"],
        description=request.POST["desc"],
    )
    return redirect(f"/shows/{created_show.id}")


def view_show_details(request, show_id):
    context = {
        "show": Show.objects.get(id=show_id),
    }
    return render(request, "show-details.html", context)


def edit_show_page(request, show_id):
    context = {
        "show": Show.objects.get(id=show_id),
    }
    return render(request, "edit-show.html", context)


def delete_show(request, show_id):
    deleted_show = Show.objects.get(id=show_id)
    deleted_show.delete()

    return redirect("/shows")


def update_show(request, show_id):

    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect(f"/shows/{show_id}")

    show = Show.objects.get(id=show_id)
    show.title = request.POST["title"]
    show.network = request.POST["network"]
    show.release_date = request.POST["release_date"]
    show.description = request.POST["desc"]
    show.save()

    return redirect(f"/shows/{show_id}")
