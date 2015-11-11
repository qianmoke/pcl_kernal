#custome awk.py module

class controller:
  
  def __init__(self):
    self.m_handlers =[]

  def subscribe(self,o):
    self.m_handlers.append(o)
  
  def run(self):
    for o in self.m_handlers:
      o.begin()
      o.choose_first()
      o.choose_second()
      o.end()

  def print_results(self):
    print
    print "Results:"
    print
    for o in self.m_handlers:
      print '----------------------------------'
      print o.description()
      print '----------------------------------'
      print o.result()
