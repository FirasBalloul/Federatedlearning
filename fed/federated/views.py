import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ModelVersion, ClientSubmission

from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def dashboard(request):
    model_versions = ModelVersion.objects.all()
    submissions = ClientSubmission.objects.all()
    context = {
        "model_versions": model_versions,
        "submissions": submissions,
    }
    return render(request, "dashboard.html", context)

@csrf_exempt
def submit_results(request):
    if request.method == "POST":
        try:
            # Log raw request body
            print("Raw request body:", request.body)

            # Parse JSON payload
            data = json.loads(request.body.decode("utf-8"))

            # Extract and validate fields
            accuracy = data.get("accuracy")
            parameters = data.get("parameters")

            if not accuracy or not parameters:
                return JsonResponse({"error": "Missing accuracy or parameters in submission."}, status=400)

            # Log received data
            print(f"Received accuracy: {accuracy}")
            print(f"Received parameters: {parameters}")

            # Save to the database
            model_version = ModelVersion.objects.first()
            if not model_version:
                model_version = ModelVersion.objects.create(version_number=1)
            ClientSubmission.objects.create(
                model_version=model_version,
                performance_metric=accuracy,
                parameters=parameters,
            )

            return JsonResponse({"message": "Submission successful!"}, status=200)

        except Exception as e:
            print("Error processing submission:", str(e))
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)
