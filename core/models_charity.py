from django.db import models
from core.utils import image_file_name


class CharityModel(models.Model):
    """Charity Cause Model"""
    name = models.CharField(max_length=254, default='Charity')
    description = models.TextField(blank=False)
    donation = models.DecimalField(max_digits=1, decimal_places=0, default=5)
    image = models.ImageField(upload_to=image_file_name, default='charity/default.jpg')

    class Meta:
        verbose_name = "Charity Action"
        verbose_name_plural = "Charity Actions"

    def __str__(self):
        return self.name


class DonationModel(models.Model):
    """Donation Transaction"""
    donor = models.CharField(max_length=50, blank=False, default="Donor")
    date = models.DateTimeField(auto_now=True)
    charity = models.ForeignKey(CharityModel, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, default=5)

    def __str__(self):
        return str(str(self.donor) + ' - ' + str(self.charity))

    class Meta:
        verbose_name = "Charity Donation"
        verbose_name_plural = "Charity Donations"







