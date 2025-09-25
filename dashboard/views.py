from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import random


projects = []
sample_titles = ["AI Blog", "E-commerce Store", "Portfolio Site", "Travel App", "Chatbot Platform"]
sample_desc = [
    "A cool project about machine learning and blogs.",
    "A simple shop built with Django.",
    "A personal site showcasing skills.",
    "A booking app for travel adventures.",
    "An AI-powered assistant demo."
]
sample_imgs = [
    "https://picsum.photos/400/250?random=1",
    "https://picsum.photos/400/250?random=2",
    "https://picsum.photos/400/250?random=3",
    "https://picsum.photos/400/250?random=4",
    "https://picsum.photos/400/250?random=5",
]

for i in range(6):
    projects.append({
        "title": random.choice(sample_titles),
        "description": random.choice(sample_desc),
        "image": random.choice(sample_imgs),
    })

def home(request):
    return render(request, "dashboard/home.html", {"projects": projects})
