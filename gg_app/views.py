from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self):
        data = {"message_title" : "Gamer Never Die They only Respawn (-)",
                "message" : "-Carriee"}                
        return data

class AboutPageView(TemplateView):
    template_name = "about.html"

class ResumePageView(TemplateView):
    template_name = "resume.html"