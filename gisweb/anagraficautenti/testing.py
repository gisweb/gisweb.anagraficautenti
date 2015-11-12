from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting
from plone.app.controlpanel.security import SecurityControlPanelAdapter
from plone.app.controlpanel.mail import MailControlPanelAdapter

from plone.testing import z2

class MyProduct(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import gisweb.anagraficautenti
        self.loadZCML(package=gisweb.anagraficautenti)

        # Install product and call its initialize() function
        z2.installProduct(app, 'gisweb.anagraficautenti')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'gisweb.anagraficautenti:default')
        # Enable self registration
        SecurityControlPanelAdapter(portal).set_enable_self_reg(True)
        # and email (otherwise self registration won't work)
        mailcp = MailControlPanelAdapter(portal)
        mailcp.set_email_from_name("Someone")
        mailcp.set_email_from_address("someone@example.com")
        mailcp.smtp_host = u"127.0.0.1"


    def tearDownZope(self, app):
        # Uninstall product
        z2.uninstallProduct(app, 'gisweb.anagraficautenti')

GISWEB_ANAGRAFICAUTENTI_FIXTURE = MyProduct()
GISWEB_ANAGRAFICAUTENTI_INTEGRATION_TESTING = IntegrationTesting(
    bases=(GISWEB_ANAGRAFICAUTENTI_FIXTURE,),
    name="gisweb.anagraficautenti:Integration")
GISWEB_ANAGRAFICAUTENTI_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(GISWEB_ANAGRAFICAUTENTI_FIXTURE,),
    name="gisweb.anagraficautenti:Functional")

