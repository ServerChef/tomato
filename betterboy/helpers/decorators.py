from functools import wraps
from betterboy.models import WebSite


class GetWebsite(object):
    """Returns website from it's ID.

    Initially, from url, the view is called with args (request, website_id, ...) which is transformed to
    (request, website, ...). It also throws an error if the website is not found
    """
    def __init__(self, view_func):
        self.view_func = view_func
        wraps(view_func)(self)

    def __call__(self, *args, **kwargs):
        assert (len(args) >= 2)

        args = list(args)  # we need to modify the args so convert list to tuple
        _id = int(args[1])

        # this line will throw an error itself if the website does not exist.
        website = WebSite.objects.get(id=_id)

        # let's be safe here
        assert (website is not None)

        args[1] = website

        return self.view_func(*args, **kwargs)
