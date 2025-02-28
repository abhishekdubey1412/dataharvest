from django.db import models
from django.db.models import Q

class RawData(models.Model):
    url = models.URLField()
    data = models.JSONField()
    scraped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

def create_raw_data(url, data):
    """Creates a new RawData entry."""
    return RawData.objects.create(url=url, data=data)

def get_raw_data(**kwargs):
    """Fetches RawData entries based on filters."""
    if not kwargs:
        return RawData.objects.all()  # Return all data if no filters are given

    filters = {k + "__icontains" if k != "id" else k: v for k, v in kwargs.items()}
    return RawData.objects.filter(**filters)

def update_raw_data(raw_data_id, **kwargs):
    """Updates a RawData entry."""
    obj = RawData.objects.filter(id=raw_data_id).first()
    if obj:
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj
    return None

def delete_raw_data(raw_data_id):
    """Deletes a RawData entry."""
    obj = RawData.objects.filter(id=raw_data_id).first()
    if obj:
        obj.delete()
        return True
    return False