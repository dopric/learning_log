from django.shortcuts import render
from .models import Topic, Entry

# Create your views here.

def index(request):
    topics = Topic.objects.all()
    print("Anzahl topics", len(topics))
    return render(request, "learning_logs/index.html", {"topics": topics})

def about(request):
    return render(request, 'learning_logs/about.html')

def contact(request):
    return render(request, 'learning_logs/contact.html')

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    return render(request, 'learning_logs/topic.html', {"topic": topic, "entries": topic.entry_set.all()})

def entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    return render(request, "learning_logs/entry.html", {"entry": entry})