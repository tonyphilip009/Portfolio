from django.contrib import admin
from django.urls import path
from api.views import about_me,EducationMe,ServicesView,CertificationView,ExperienceView,ProjectsView,SkillsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',about_me.as_view()),
    path('education/',EducationMe.as_view()),
    path('projects/',ProjectsView.as_view()),
    path('skills/',SkillsView.as_view()),
    path('experience/',ExperienceView.as_view()),
    path('certifications/',CertificationView.as_view()),
    path('services/',ServicesView.as_view())

]
