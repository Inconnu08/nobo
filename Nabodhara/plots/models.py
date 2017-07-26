from django.db import models
from django.core.urlresolvers import reverse
from cloudinary.models import CloudinaryField


class Applicant(models.Model):
    profile_picture = CloudinaryField(blank=True, null=True)
    applicants_name_bangla = models.CharField(max_length=255, blank=True, null=True)
    applicants_name = models.CharField(max_length=255, blank=True, null=True)
    fathers_name_bangla = models.CharField(max_length=255, blank=True, null=True)
    fathers_name = models.CharField(max_length=255, blank=True, null=True)
    mothers_name_bangla = models.CharField(max_length=255, blank=True, null=True)
    mothers_name = models.CharField(max_length=255, blank=True, null=True)
    spouses_name_bangla = models.CharField(max_length=255, blank=True, null=True)
    spouses_name = models.CharField(max_length=255, blank=True, null=True)
    other_name = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=11, blank=True, null=True)
    present_address = models.CharField(max_length=255, blank=True, null=True)
    permanent_address = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    religion = models.CharField(max_length=50, blank=True, null=True)
    national_ID = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    passport_no = models.CharField(max_length=255, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    nominees_name = models.CharField(max_length=255, blank=True, null=True)
    nominess_relationship_with_applicant = models.CharField(max_length=255, blank=True, null=True)
    nominees_address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.applicants_name}'

    def get_absolute_url(self):
        return reverse("plot:applicantsdetail", kwargs={"pk": self.pk})


class Booking(models.Model):
    date_of_booking = models.DateField(blank=True, null=True)
    regular_price = models.IntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    rate_per_katha = models.IntegerField(blank=True, null=True)
    total_price = models.IntegerField(blank=True, null=True)
    total_price_in_words = models.CharField(max_length=255, blank=True, null=True)
    booking_money = models.IntegerField(blank=True, null=True)
    down_payment = models.IntegerField(blank=True, null=True)
    total_payment = models.IntegerField(blank=True, null=True)
    total_payment_in_words = models.CharField(max_length=255, blank=True, null=True)
    rest_amount = models.IntegerField(blank=True, null=True)
    rest_amount_in_words = models.CharField(max_length=255, blank=True, null=True)
    mode_of_payment = models.CharField(max_length=255, blank=True, null=True)
    one_time = models.IntegerField(blank=True, null=True)
    installment = models.IntegerField(blank=True, null=True)
    no_of_installment = models.IntegerField(blank=True, null=True)
    per_installment = models.IntegerField(blank=True, null=True)
    in_words = models.CharField(max_length=255, blank=True, null=True)
    booked_by = models.ForeignKey(Applicant, null=True, blank=True, related_name='booking')

    def __str__(self):
        return f'{self.booked_by} ({self.date_of_booking})'

    def get_absolute_url(self):
        return reverse("plot:bookingdetail", kwargs={"pk": self.pk})


class Plot(models.Model):
    plot_no = models.CharField(max_length=255, blank=True, null=True)
    road_no = models.CharField(max_length=255, blank=True, null=True)
    sector_block = models.CharField(max_length=255, blank=True, null=True)
    plot_size = models.CharField(max_length=255, blank=True, null=True)
    facing = models.CharField(max_length=255, blank=True, null=True)
    number_of_plot = models.CharField(max_length=255, blank=True, null=True)
    total_land = models.CharField(max_length=255, blank=True, null=True)
    total_land_in_words = models.CharField(max_length=255, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    booking_info = models.ForeignKey(Booking, null=True, blank=True, related_name='plot')

    def __str__(self):
        return f'{self.plot_no} -{self.road_no}-{self.sector_block}'

    def get_absolute_url(self):
        return reverse("plot:plotdetail", kwargs={"pk": self.pk})

    class Meta:
        unique_together = ('plot_no', 'road_no', 'sector_block')
