from django.shortcuts import get_object_or_404


class MultiSlugMixin(object):
    model = None

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        model_class = self.model
        if slug is not None:
            try:
                obj = get_object_or_404(model_class, slug=slug)
            except model_class.MultipleObjectsReturned:
                obj = obj.filter(slug=slug).order_by("-title").first()
        else:
            obj = super(MultiSlugMixin, self).get_object(*args, **kwargs)
        return obj


class SubmitBtnMixin(object):
    submit_btn = None

    def get_context_data(self, *args, **kwargs):
        context = super(SubmitBtnMixin, self).get_context_data(*args, **kwargs)
        context["submit_btn"] = self.submit_btn
        return context
