from datetime import datetime
ahora = datetime.now()

print '%s/%s/%s %s:%s:%s' % (ahora.month, ahora.day, ahora.year, ahora.hour, ahora.minute, ahora.second)
