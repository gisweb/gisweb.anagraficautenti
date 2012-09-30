# - coding: utf-8 -
from zope.interface import Interface, implements
from zope import schema

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
        title=u"Codice fiscale",
        required=True
        )
    nome = schema.TextLine(
        title=u'Nome',        required=True,
        )
    cognome = schema.TextLine(
        title=u'Cognome',
        required=True,
        )
    nazione_nascita = schema.TextLine(
        title=u"Nazione di nascita",
        required=True,
        )
    provincia_nascita = schema.TextLine(
        title=u"Provincia di nascita",
        required=True,
        )
    comune_nascita = schema.TextLine(
        title=u"Comune di nascita",
        required=True,
        )
    sesso = schema.Choice(
        title=u'Sesso',
        values = [
            u'Maschio',
            u'Femmina',
            ],
        required=True,
        )
    data_nascita = schema.Date(
        title=u'Data di nascita',
        required=True,
        )
    indirizzo = schema.TextLine(
        title=u"Indirizzo di residenza",
        required=True,
        )
    cap = schema.TextLine(
        title=u"CAP",
        required=True,
        )
    comune = schema.TextLine(
        title=u'Comune di residenza',
        required=True,
        )
    provincia = schema.TextLine(
        title=u'Provincia di residenza',
        required=True,
        )
    nazione = schema.TextLine(
        title=u'Nazione di residenza',
        required=True,
        )
    telefono = schema.TextLine(
        title=u'Numero di telefono',
        required=False,
        )
    tipo_documento = schema.Choice(
        title=u'Tipo di documento',
        values = [
            u'Passaporto',
            u"Carta d'identita", # XXX Put accent in transaltion
            ],
        required=True,
        )
    n_documento = schema.TextLine(
        title=u'Numero documento',
        required=True,
        )
    rilasciato_da = schema.TextLine(
        title=u'Rilasciato da',
        required=True,
        )
    rilasciato_il = schema.Date(
        title=u'Rilasciato il',
        required=True,
        )
    accept = schema.Bool(
        title=u'Accetto',
        description=u"Autorizzo al trattamento dei dati personali",
        required=True,
        constraint=validateAccept,
        )
