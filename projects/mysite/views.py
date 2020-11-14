from django.views.generic.base import TemplateView
from django.apps import apps


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["app_list"] = ["polls", "books"]
        app_names = []
        for app in apps.get_app_configs():
            if "site-packages" not in app.path:
                app_names.append(app.name)

        context["app_list"] = app_names

        return context