from django.db import models

from .models import TimeStampedModel

class TimeStampedMixin(TimeStampedModel):

    """
    Mixin that provides fields created and updated at and by fields

    Includes
        - TimestampedModel
        - BaseUserTrackedModel
    """
    class Meta:
        abstract = True