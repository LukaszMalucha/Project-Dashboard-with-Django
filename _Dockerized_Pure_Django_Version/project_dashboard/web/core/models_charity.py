from django.db import models


class Charity(models.Model):
    """Charity Cause Model"""
    name = models.CharField(max_length=254, default='Charity')
    description = models.TextField(blank=False)
    donation = models.DecimalField(max_digits=1, decimal_places=0, default=5)
    image = models.ImageField(upload_to='donations')

    class Meta:
        verbose_name = "Proposed Charity"
        verbose_name_plural = "Proposed Charities"

    def __str__(self):
        return self.name


class Donation(models.Model):
    """Donation Tranaction"""
    donor = models.CharField(max_length=50, blank=False, default="Donor")
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.donor)

    class Meta:
        verbose_name = "User Donation"
        verbose_name_plural = "User Donations"


class DonationLineItem(models.Model):
    """Donation Item Model"""
    donation = models.ForeignKey(Donation, null=False, on_delete=models.CASCADE)
    charity = models.ForeignKey(Charity, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, default=1)

    def __str__(self):
        return str(self.charity.name)






