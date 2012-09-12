from plone.app.users.browser.personalpreferences import UserDataPanelAdapter


fieldnames = ['codicefiscale', 'cognome', 'nome', 'data_nascita',
              'nazione_nascita', 'provincia_nascita', 'comune_nascita',
              'sesso', 'indirizzo', 'cap', 'comune', 'provincia', 'nazione',
              'telefono', 'tipo_documento', 'n_documento', 'rilasciato_da',
              'rilasciato_il']

def mkprop(fieldname):
    def getter(self):
        return self.context.getProperty(fieldname, '')
    def setter(self, value):
        return self.context.setMemberProperties({fieldname : value})
    return property(getter, setter)


class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    for fieldname in fieldnames:
        locals()[fieldname] = mkprop(fieldname)
