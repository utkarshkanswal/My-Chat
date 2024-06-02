from django.urls import path

from TechChat.views import MyInbox

urlpatterns = [
    path('my-messages/<user_id>/', MyInbox.as_view({'get':'list'}), name='my_inbox'),
]

