from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .genai_analyzer import analyze_dream_gemini  # Import function

def dream_chat(request):
    return render(request, "chatbot.html")  # Ensure chatbot.html exists inside templates folder

@csrf_exempt
def dream_analysis(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            dream_text = data.get("dream_text", "")
            mode = data.get("mode", "analysis").lower()

            if not dream_text:
                return JsonResponse({"error": "No dream text provided"}, status=400)

            if mode not in ["story", "analysis"]:
                return JsonResponse({"error": "Invalid mode. Choose 'story' or 'analysis'."}, status=400)

            result = analyze_dream_gemini(dream_text, mode)
            return JsonResponse({"result": result}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON input"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

# this is a cloned project