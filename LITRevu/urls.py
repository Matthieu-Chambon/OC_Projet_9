"""
URL configuration for LITRevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path

import authentication.views
import reviews.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
            name='login'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', authentication.views.home, name='home'),
    path('my-posts/', reviews.views.my_posts, name='my-posts'),
    
    path('tickets/add/', reviews.views.ticket_create, name='ticket-create'),
    path('tickets/<int:ticket_id>/', reviews.views.ticket_details, name='ticket-details'),
    path('tickets/<int:ticket_id>/edit/', reviews.views.ticket_edit, name='ticket-edit'),
    path('tickets/<int:ticket_id>/delete/', reviews.views.ticket_delete, name='ticket-delete'),
    
    path('tickets/<int:ticket_id>/create-review/', reviews.views.review_create, name='review-create'),
    path('reviews/<int:review_id>/edit/', reviews.views.review_edit, name='review-edit'),
    path('reviews/<int:review_id>/delete/', reviews.views.review_delete, name='review-delete'),
    
    path('create-ticket-and-review/', reviews.views.create_ticket_and_review, name='create-ticket-and-review'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)