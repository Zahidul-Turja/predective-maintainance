from django.db import models


class PredictiveMaintenance(models.Model):
    # Device Information
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    device_age = models.PositiveIntegerField(help_text="Device age in months")
    storage_capacity = models.CharField(max_length=20)
    ram_capacity = models.CharField(max_length=20)

    # Battery & Performance
    battery_cycle_count = models.PositiveIntegerField(null=True, blank=True)
    battery_health = models.FloatField(null=True, blank=True)
    storage_usage = models.FloatField(null=True, blank=True)
    ram_usage = models.FloatField(null=True, blank=True)
    fast_charging = models.CharField(
        max_length=10, choices=[("yes", "Yes"), ("no", "No")], blank=True
    )
    charges_overnight = models.CharField(
        max_length=10, choices=[("yes", "Yes"), ("no", "No")], blank=True
    )

    # Repair History
    previous_repairs = models.JSONField(blank=True, default=list)
    last_repair_date = models.DateField(null=True, blank=True)
    authorized_service = models.CharField(
        max_length=10, choices=[("yes", "Yes"), ("no", "No")], blank=True
    )
    warranty_status = models.CharField(
        max_length=20,
        choices=[("in", "In Warranty"), ("out", "Out of Warranty")],
        blank=True,
    )

    # Hardware Condition
    overheating = models.BooleanField(default=False)
    drop_history = models.BooleanField(default=False)
    water_damage = models.BooleanField(default=False)
    sensor_issues = models.BooleanField(default=False)
    battery_bulging = models.BooleanField(default=False)
    screen_cracked = models.BooleanField(default=False)
    buttons_not_working = models.BooleanField(default=False)

    # Usage Behavior
    screen_time = models.CharField(
        max_length=10, blank=True
    )  # e.g., "<2h", "2-4h"
    primary_use = models.JSONField(blank=True, default=list)
    charge_frequency = models.CharField(max_length=20, blank=True)
    charge_time = models.CharField(max_length=20, blank=True)
    environment = models.CharField(max_length=50, blank=True)
    region_temp = models.FloatField(null=True, blank=True)
    updated_software = models.CharField(
        max_length=10, choices=[("yes", "Yes"), ("no", "No")], blank=True
    )
    rooted = models.CharField(
        max_length=10,
        choices=[("yes", "Yes"), ("no", "No"), ("unknown", "Not Sure")],
        blank=True,
    )
    major_concern = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.os})"

    class Meta:
        ordering = ["-created_at"]