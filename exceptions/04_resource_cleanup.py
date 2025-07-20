class Resource:
  def __enter__(self, *args):
    print("Entering resource", args)
    return 1 # If invoked by `with`, result will be as i command
  
  def __exit__(self, exec_type, exec_val, exec_tb):
    print("exiting context", (exec_type, exec_val, exec_tb))
    return True # True if i want to handle exception here that was raised in with clause, i.e. suppress the exception

with Resource() as r:
  print(r, type(r))
  raise NameError("Hehe")
