from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from betterboy.helpers.decorators import GetWebsite
from betterboy.forms import WebSiteForm
import json, codecs
from betterboy.helpers import response

_reader = codecs.getreader("utf-8")


def website_common(request: WSGIRequest):
    if request.method == "GET":
        return JsonResponse("GETTING")
    elif request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        form = WebSiteForm(data)
        if form.is_valid():
            model = form.to_model()

            model.save()
            return response.success()
        else:
            return response.validation_error(form)
    else:
        raise Exception("request method {} not implemented".format(request.method))


@GetWebsite
def website_single(request: WSGIRequest, website):
    if request.method == "GET":
        return JsonResponse(website.to_dict())
    elif request.method == "POST":
        raise Exception("Y u posting on the wrong URL?")

    return JsonResponse("success")
