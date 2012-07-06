#!/usr/bin/python

import random

count = 255

print '''
<html>
<head>
<style>
div {
  height:100px;
  width:100px;
}
'''

for i in range(count):
  print '.g' + str(i) + '{'
  print 'background-image: -moz-linear-gradient(bottom, rgb('+str(int(random.random() * 255))+',142,219) 2%, rgb(105,171,255) 51%);'
  print '}'

print '''
</style>
</head>
<body>'''

for i in range(count):
  print '<div class="g' + str(i) + '"> </div>'

print '''</body></html>'''
