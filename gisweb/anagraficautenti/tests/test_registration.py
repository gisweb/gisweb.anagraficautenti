# - coding: utf-8 -
import unittest
from plone.testing.z2 import Browser
from gisweb.anagraficautenti.testing import GISWEB_ANAGRAFICAUTENTI_FUNCTIONAL_TESTING

class TestRegistration(unittest.TestCase):
    layer = GISWEB_ANAGRAFICAUTENTI_FUNCTIONAL_TESTING
    def test_registration_form(self):
        browser = Browser(self.layer['app'])
        browser.handleErrors = False
        portal = self.layer['portal']
        browser.open(portal.absolute_url())
        browser.getLink('Register').click()
        self.assertTrue('codicefiscale' in browser.contents)
        fields = portal.portal_properties.site_properties.user_registration_fields
        for fieldname in fields:
            field = browser.getControl(name='form.' + fieldname)
            if field.type == 'text':
                field.value = 'foo bàr'
            elif field.type == 'select':
                # we just select the last option
                field.value = [field.options[-1]]
            elif field.type == 'checkbox':
                field.value = True
            else:
                self.fail() # we're not prepared for what we're not prepared
        # Email must be something that validates properly
        browser.getControl(name='form.email').value = 'foo@example.com'
        # And username must be explicitly set (it's not in portal_properties..)
        browser.getControl(name='form.username').value = 'foo'
        # ..and dates must be valid
        browser.getControl(name='form.data_nascita').value = '1/1/1970'
        browser.getControl(name='form.rilasciato_il').value = '1/1/2000'
        browser.getControl(name="form.actions.register").click()
        self.assertTrue('foo' in portal.portal_membership.listMemberIds())
        member = portal.portal_membership.getMemberById('foo')
        member.setSecurityProfile(password="secret")
        import transaction; transaction.commit()

        # Now we (try to) login with the newly registered user
        browser.getLink('Log in').click()
        browser.getControl(name='__ac_name').value = 'foo'
        browser.getControl(name='__ac_password').value = 'secret'
        browser.getControl('Log in').click()

        browser.open(portal.absolute_url() + "/@@personal-information")
        browser.getControl(name='form.codicefiscale').value = 'changed!'
        browser.getControl('Save').click()
        member = portal.portal_membership.getMemberById('foo')
        new_value = member.getProperty('codicefiscale')
        self.assertEqual(new_value, 'changed!')
