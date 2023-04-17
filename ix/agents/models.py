from django.db import models


class Agent(models.Model):
    MODEL_CHOICES = (
        ("gpt4", "GPT4"),
        ("gpt-3.5-turbo", "GPT4"),
    )

    name = models.CharField(max_length=255)
    purpose = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # model config
    model = models.CharField(max_length=255)

    # agent config
    system_prompt = models.TextField()
    commands = models.JSONField(null=True, blank=True)
    config = models.JSONField()

    def __str__(self):
        return self.name


class Resource(models.Model):
    RESOURCE_TYPE_CHOICES = (
        ("vector_memory", "Vector Memory"),
        ("database", "Database"),
        ("file_system", "File System"),
        ("cache", "Cache"),
        ("api", "API"),
        ("knowledge_base", "Knowledge Base"),
        ("image_database", "Image Database"),
        ("audio_database", "Audio Database"),
        ("video_database", "Video Database"),
        ("cloud_storage", "Cloud Storage"),
        ("content_delivery_network", "Content Delivery Network"),
        ("message_queue", "Message Queue"),
        ("stream_processing", "Stream Processing"),
    )

    type = models.CharField(max_length=32, choices=RESOURCE_TYPE_CHOICES)
    config = models.JSONField()

    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="resources")

    def __str__(self):
        return f"{self.type} for {self.agent.name}"