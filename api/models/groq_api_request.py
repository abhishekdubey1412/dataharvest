from django.db import models

class APIRequestLog(models.Model):
    request_time = models.DateTimeField(auto_now_add=True)
    status_code = models.IntegerField()
    tokens_used = models.IntegerField(default=0)
    response_time = models.FloatField(help_text="Time taken for API response in seconds")
    
    class Meta:
        ordering = ['-request_time']
    
    def __str__(self):
        return f"Request at {self.request_time} - Status: {self.status_code} - Tokens: {self.tokens_used}"