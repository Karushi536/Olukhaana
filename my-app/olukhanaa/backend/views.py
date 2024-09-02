from django.shortcuts import render

# Create your views here.
# views.py

from dotenv import load_dotenv
import os
from django.http import JsonResponse
from convex import ConvexClient

load_dotenv(".env.local")  # Load environment variables from .env.local

client = ConvexClient(os.getenv("CONVEX_URL"))

def get_tasks(request):
    tasks = client.query("tasks:get")
    return JsonResponse(tasks, safe=False)
