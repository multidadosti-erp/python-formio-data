# Copyright Nova Code (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from test_component import ComponentTestCase
from components import phoneNumberComponent


class PhoneNumberComponentTestCase(ComponentTestCase):

    def test_object(self):
        # phoneNumberComponent
        phoneNumber = self.builder.components['phoneNumber']
        self.assertIsInstance(phoneNumber['component'], phoneNumberComponent)

        # Not phoneNumberComponent
        firstName = self.builder.components['firstName']
        self.assertNotIsInstance(firstName['component'], phoneNumberComponent)

        submit = self.builder.components['submit']
        self.assertNotIsInstance(submit['component'], phoneNumberComponent)

    def test_get_label(self):
        phoneNumber = self.builder.components['phoneNumber']['component']
        self.assertEqual(phoneNumber.label, 'Phone Number')

    def test_set_label(self):
        phoneNumber = self.builder.components['phoneNumber']['component']
        self.assertEqual(phoneNumber.label, 'Phone Number')
        phoneNumber.label = 'Foobar'
        self.assertEqual(phoneNumber.label, 'Foobar')

    def test_get_submission(self):
        phoneNumber = self.submission.components['phoneNumber']['component']
        self.assertEqual(phoneNumber.label, 'Phone Number')
        self.assertEqual(phoneNumber.value, '(069) 999-9999')

    def test_get_submission_data(self):
        phoneNumber = self.submission.data.phoneNumber
        self.assertEqual(phoneNumber.label, 'Phone Number')
        self.assertEqual(phoneNumber.value, '(069) 999-9999')