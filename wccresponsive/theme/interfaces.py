from zope import schema
from zope.interface import Interface

class IThemeSettings(Interface):
    scheme = schema.Choice(title=u"Color scheme",
            vocabulary="wccresponsive.theme.colorscheme",
            default='red')

    is_subsite = schema.Bool(
            title=u'Is Subsite',
            default=True
    )

    logo_url = schema.TextLine(
        title=u'URL the logo should link to',
        description=u'Leave empty to use default',
        default=u''
    )

class IThemeSpecific(Interface):
    pass
