# - coding: utf-8 -
from zope.interface import Interface, implements
from zope import schema

from collective.examples.userdata import _
from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.userdataschema import IUserDataSchema

def validateAccept(value):
    if not value == True:
        return False
    return True

class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema

class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """
    codicefiscale = schema.TextLine(
        title=_("Codice fiscale"),
        required=True
        )
    firstname = schema.TextLine(
        title=_(u'label_firstname', default=u'First name'),
        description=_(u'help_firstname',
                      default=u"Fill in your given name."),
        required=True,
        )
    lastname = schema.TextLine(
        title=_(u'label_lastname', default=u'Last name'),
        description=_(u'help_lastname',
                      default=u"Fill in your surname or your family name."),
        required=True,
        )
    birth_country = schema.TextLine(
        title=_("nazione di nascita"),
        required=True,
        )
    birth_state = schema.TextLine(
        title=_("Provincia di nascita"),
        required=True,
        )
    birth_city = schema.TextLine(
        title=_("Comune di nascita"),
        required=True,
        )
    gender = schema.Choice(
        title=_(u'label_gender', default=u'Gender'),
        description=_(u'help_gender',
                      default=u"Are you a girl or a boy?"),
        values = [
            _(u'Male'),
            _(u'Female'),
            ],
        required=True,
        )
    birthdate = schema.Date(
        title=_(u'label_birthdate', default=u'birthdate'),
        description=_(u'help_birthdate',
            default=u'Your date of birth, in the format dd-mm-yyyy'),
        required=True,
        )
    address = schema.TextLine(
        title=_("Indirizzo di residenza"),
        required=True,
        )
    cap = schema.TextLine(
        title=_("CAP"),
        required=True,
        )
    comune = schema.TextLine(
        title=_(u'label_city', default=u'Comune di residenza'),
        required=True,
        )
    provincia = schema.TextLine(
        title=_(u'Provincia di residenza'),
        required=True,
        )
    country = schema.TextLine(
        title=_(u'Nazione di residenza'),
        required=True,
        )
    phone = schema.TextLine(
        title=_(u'label_phone', default=u'Telephone number'),
        description=_(u'help_phone',
                      default=u"Leave your phone number so we can reach you."),
        required=False,
        )
    tipo_documento = schema.Choice(
        title=_(u'Tipo di documento'),
        values = [
            _(u'Passaporto'),
            _(u"Carta d'identita"), # XXX Put accent in transaltion
            ],
        required=True,
        )
    n_documento = schema.TextLine(
        title=_(u'Numero documento'),
        required=True,
        )
    rilasciato_da = schema.TextLine(
        title=_(u'Rilasciato da'),
        required=True,
        )
    rilasciato_il = schema.Date(
        title=_(u'Rilasciato da'),
        required=True,
        )
    accept = schema.Bool(
        title=_(u'label_accept', default=u'Accept terms of use'),
        description=_(u'help_accept',
                      default=u"Tick this box to indicate that you have found,"
                      " read and accepted the terms of use for this site. "),
        required=True,
        constraint=validateAccept,
        )

