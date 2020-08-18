from django.shortcuts import render
from cowsay_app.forms import result
from cowsay_app.models import Results
import subprocess
# Create your views here.


def home_view(request):
    initial_greeting = subprocess.run(["cowsay", "hello"], capture_output=True)
    greeting = (initial_greeting.stdout.decode())

    form = result()
    if request.method == "POST":
        form = result(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            Results.objects.create(input_text=data.get("input_text"))

            p = subprocess.run(
                ["cowsay", data.get("input_text")], capture_output=True)
            greeting = p.stdout.decode()

            form = result()
            return render(request, "home.html", {"form": form, "test": greeting})
    return render(request, "home.html", {"form": form, "test": greeting})


def history_view(request):
    history = [value.input_text for value in Results.objects.all()][-10:]

    return render(request, "history.html", {"results": history})
