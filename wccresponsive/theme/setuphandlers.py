from collective.grok import gs
from wccresponsive.theme import MessageFactory as _

@gs.importstep(
    name=u'wccresponsive.theme', 
    title=_('wccresponsive.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wccresponsive.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
