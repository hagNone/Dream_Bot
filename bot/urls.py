from django.urls import path
from .views import dream_chat, dream_analysis

urlpatterns = [
    path("chat/", dream_chat, name="dream_chat"),  # 🌟 Chat UI page
    path("dream_analysis/", dream_analysis, name="dream_analysis"),  # 🔥 API endpoint
]
