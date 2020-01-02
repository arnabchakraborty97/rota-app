from django.shortcuts import render
from .forms import MeetingForm
from .models import Meeting


def index(request):
	if request.user.is_authenticated:
		meetings = Meeting.objects.all()
		return render(request, 'meetings/index.html', {'meetings': meetings})


def details(request, meeting_id):
	meeting = Meeting.objects.get(pk=meeting_id)
	return render(request, 'meetings/details.html', {'meeting': meeting})


def create_meeting(request):
    form = MeetingForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        meeting = form.save(commit=False)
        meeting.save()
        return render(request, 'meetings/details.html', {'meeting': meeting})
    return render(request, 'meetings/meeting_form.html', {'form': form})

def edit_meeting(request, meeting_id):
    meeting = Meeting.objects.get(pk=meeting_id)

    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)

        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.save()
            return render(request, 'meetings/details.html', {'meeting': meeting})
    else:
        form = MeetingForm(instance=meeting)
        return render(request, 'meetings/meeting_form.html', {'form': form})

def delete_meeting(request, meeting_id):
    meeting = Meeting.objects.get(pk=meeting_id)
    meeting.delete()
    meetings = Meeting.objects.all()
    return render(request, 'meetings/index.html', {'meetings': meetings})
