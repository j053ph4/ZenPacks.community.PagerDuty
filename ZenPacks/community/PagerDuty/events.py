class PagerDutyPreEventPlugin(object):
    def apply(self, eventProxy, dmd):
        event = eventProxy._zepRawEvent.event
        try:
            event.pdServiceKey = device.zPDServiceKey
        except:
            try: event.pdServiceKey = 'nokey'
            except:  pass
