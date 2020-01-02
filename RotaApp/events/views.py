from django.shortcuts import render
from .forms import EventForm
from .models import Event


def index(request):
	if request.user.is_authenticated:
		events = Event.objects.all()
		return render(request, 'events/index.html', {'events': events})


def details(request, event_id):
	event = Event.objects.get(pk=event_id)
	return render(request, 'events/details.html', {'event': event})


def create_event(request):
    form = EventForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        event = form.save(commit=False)
        event.save()
        return render(request, 'events/details.html', {'event': event})
    return render(request, 'events/event_form.html', {'form': form})

def edit_event(request, event_id):
    event = Event.objects.get(pk=event_id)

    if request.method == "POST":
        form = EventForm(request.POST, instance=event)

        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return render(request, 'events/details.html', {'event': event})
    else:
        form = EventForm(instance=event)
        return render(request, 'events/event_form.html', {'form': form})

def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})