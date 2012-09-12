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
    nome = schema.TextLine(
        title=_(u'Nome'),        required=True,
        )
    cognome = schema.TextLine(
        title=_(u'Cognome'),
        required=True,
        )
    nazione_nascita = schema.TextLine(
        title=_("Nazione di nascita"),
        required=True,
        )
    provincia_nascita = schema.TextLine(
        title=_("Provincia di nascita"),
        required=True,
        )
    comune_nascita = schema.TextLine(
        title=_("Comune di nascita"),
        required=True,
        )
    sesso = schema.Choice(
        title=_(u'Sesso'),
        values = [
            _(u'Maschio'),
            _(u'Femmina'),
            ],
        required=True,
        )
    data_nascita = schema.Date(
        title=_(u'Data di nascita'),
        required=True,
        )
    indirizzo = schema.TextLine(
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
    nazione = schema.TextLine(
        title=_(u'Nazione di residenza'),
        required=True,
        )
    telefono = schema.TextLine(
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
        title=_(u'Accetto'),
        description=_(u"Autorizzo al trattamento dei dati personali"),
        required=True,
        constraint=validateAccept,
        )