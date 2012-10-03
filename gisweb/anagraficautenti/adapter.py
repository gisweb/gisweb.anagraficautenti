from plone.app.users.browser.personalpreferences import UserDataPanelAdapter
from datetime import date
from userdataschema import IEnhancedUserDataSchema


fieldnames = ['codicefiscale', 'cognome', 'nome', 'data_nascita',
              'nazione_nascita', 'provincia_nascita', 'comune_nascita',
              'sesso', 'indirizzo', 'cap', 'comune', 'provincia', 'nazione',
              'telefono', 'tipo_documento', 'n_documento', 'rilasciato_da',
              'rilasciato_il']

def mkprop(fieldname):
    field = IEnhancedUserDataSchema[fieldname]
    def getter(self):
        value = self.context.getProperty(fieldname, '')
        return unicode(value, 'utf8')
    def setter(self, value):
        if isinstance(value, date):
            value = value.strftime("%Y-%m-%d")
        return self.context.setMemberProperties({fieldname : value})
    return property(getter, setter)


class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    for fieldname in fieldnames:
        locals()[fieldname] = mkprop(fieldname)
    accept = mkprop('accept')