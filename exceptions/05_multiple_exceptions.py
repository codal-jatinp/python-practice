def f():
  excs = [OSError("Error 1"), SystemError("Error 2")]
  raise ExceptionGroup('there are problems', excs)

try:
  f()
# except OSError:
#   print("Got os error")
# except ExceptionGroup:
#   print('got a group')
except* OSError:
 print('there where os errors') 
# except* SystemError:
#   print('There was system error')