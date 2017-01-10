from django.http import JsonResponse


def validation_error(form):
    return JsonResponse({
        "success": False,
        "error": form.errors
    })


def success():
    return JsonResponse({
        "success": True
    })
