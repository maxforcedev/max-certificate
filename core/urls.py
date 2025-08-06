from django.contrib import admin
from django.urls import path
from courses.views import CourseListView, CourseSelectListView
from certificates.views import CertificateCreateView, validate_certificate, request_certificate_code, my_certificates
from institution.views import InstitutionSettingsView

urlpatterns = [
    path('admin/', admin.site.urls),

    path("courses/", CourseListView.as_view(), name="course-list"),
    path("courses/select/", CourseSelectListView.as_view(), name="course-select"),

    path("institution/settings/", InstitutionSettingsView.as_view()),

    path("certificates/", CertificateCreateView.as_view(), name="certificate-create"),
    path("certificates/validate/", validate_certificate, name="certificate-validate"),
    path("certificates/request-code/", request_certificate_code),
    path("certificates/my-certificates/", my_certificates),
]
