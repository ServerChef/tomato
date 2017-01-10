from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from betterboy.helpers.decorators import GetWebsite


def website_common(request: WSGIRequest):
    if request.method == "GET":
        return JsonResponse("GETTING")
    elif request.method == "POST":
        return JsonResponse("POSTING")
    else:
        raise Exception("request method {} not implemented".format(request.method))


@GetWebsite
def website_single(request: WSGIRequest, website):
    if request.method == "GET":
        return JsonResponse(website.to_dict())

    return JsonResponse("success")
