#!/usr/bin/env python

import cgi
import os.path
import os
import datetime
import cgitb; cgitb.enable()
import sys
import pytz

def headers():
  print "content-type: text/plain"
  print
  

def main():
  form = cgi.FieldStorage()
  expenses = form.getList("expense")
  
  headers()
  
  for e in expenses:
    print  e

if __name__ == "__main__":
  main()