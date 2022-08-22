from django.test import TestCase
from pharmacy.models import Pharmacy
from accounts.models import Patient,Doctor

class URLTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

class Pharmacy(TestCase):
    def test_patient_creation(self):
        patient = Pharmacy.objects.create(rating=3)
        self.assertTrue(patient, 3) 

class Doctor(TestCase):
    def test_doctor_creation(self):
        doctor = Doctor.objects.create(location='3')
        self.assertTrue(doctor, 3)

class Patient(TestCase):
    def test_patient_creation(self):
        patient = Patient.objects.create(blood='3')
        self.assertTrue(patient, 3)
