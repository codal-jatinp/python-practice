import sys
# try:
#   print (1/0)
# except ZeroDivisionError as e:
#   e.add_note('intentional zero division')
#   tb = e.__traceback__


# raise BaseException('New one with traceback').with_traceback(tb)



# while True:
#   try:
#     x = int(input("Enter a number: "))
#     print("Apple per person is ", 5 / x)
#   except ValueError as e:
#     print("Oops! it was an invalid number. Try again:", e.__str__())
#     print(e.args)
#   except (KeyboardInterrupt, EOFError):
#     print("Alright i'll exit now")
#     exit(-1)
#   except (ZeroDivisionError, RuntimeError):
#     pass
#   else:
#     print('well done')
#     break


# raise NameError("HiThere")


# try:
#   # raise 1 # Not possible since it must be exception
#   raise Exception('spam', 'eggs')
# except int:
#   print('got int')
# except Exception as e:
#   print (e == sys.exception())
#   print(e.args, sys.exception().args)
# except BaseException:
#   # Since it's not instance of Exception, program should terminate
#   exit()

try:
  raise NameError("HiThere")
except NameError as e:
  raise RuntimeError from e
