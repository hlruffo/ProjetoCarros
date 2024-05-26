from django.test import TestCase
from .forms import CarForm

class CarFormTest(TestCase):
    def test_factory_year_validation(self):
        data = {
            'model': 'Test Model',
            'factory_year': 1980,
        }
        form = CarForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('factory_year', form.errors)
        self.assertEqual(form.errors['factory_year'], ['Ano de fabricação inválido'])
