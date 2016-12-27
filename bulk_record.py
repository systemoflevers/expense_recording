#!/usr/bin/env python                                                                                                                                        
                                                                                                                                                             
import cgi                                                                                                                                                   
import cgitb; cgitb.enable()                                                                                                                                 
                                                                                                                                                             
def headers():                                                                                                                                               
  print "content-type: text/plain"                                                                                                                           
  print                                                                                                                                                      
         

def getParameters(expense):
  values = expense.split("|")
  # WHEN|WHAT|AMOUNT|JOINT|DESCRIPTION
  parameters = {
    "who" : values[0],
    "when" : values[1],
    "what" : values[2],
    "amount" : values[3],
    "joint" : values[4],
    "description"  values[5],
  }
  
  parameterList = (
    "entry.272749610=%(who)s&entry.2037284352=%(what)s&entry.671256177=%(type)s"
    "&entry.234466585=%(amount)s&entry.696825855=%(when)"
    "&entry.2125473046=%(desc)s"
  )
  
  return parameterList % parameters
                                                                                                                                                             
def main():                                                                                                                                                  
  form = cgi.FieldStorage()                                                                                                                                  
  expenses = form.getlist("expense")                                                                                                                         
                                                                                                                                                             
  headers()                                                                                                                                                  
                                                                                                                                                             
  for e in expenses:                                                                                                                                         
    print  getParameters(e)                                                                                                                                                 
  print "done"                                                                                                                                               
                                                                                                                                                             
main()