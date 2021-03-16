from django.db import models


class JobsManager(models.Manager):
    """ Manager for Work Model """

    def list_active_jobs(self):
        data = self.filter(
            status='1'
        ).order_by('-id')
        return data

    def list_active_jobs_by_url(self, city):
        listing = self.filter(
            status='1',
            location_id__name=city,
        )
        return listing
