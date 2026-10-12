from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Note


@login_required
def note_list(request):
    notes = Note.objects.filter(owner=request.user)

    return render(
        request,
        "notes/note_list.html",
        {"notes": notes}
    )


@login_required
def create_note(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        Note.objects.create(
            owner=request.user,
            title=title,
            content=content
        )

        return redirect("note_list")

    return render(request, "notes/create_note.html")\
