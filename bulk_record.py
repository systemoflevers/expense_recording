#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable()

def headers():
  print "content-type: text/plain"
  print
  

def main():
  form = cgi.FieldStorage()
  expenses = form.getList("expense")
  
  headers()
  
  for e in expenses:
    print  e
  print "done"

if __name__ == "__main__":
  main()