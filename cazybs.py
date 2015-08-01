# -*- coding: utf-8 -*-
# Copyright 2015 Erico Vieira Porto
#
#  Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. '''

from __future__ import print_function
import httplib

def findEnzymeInCazy(enzyname):
    conn = httplib.HTTPConnection("www.cazy.org", 80)
    conn.connect()
    conn.request('GET', "/search?tag=4&recherche=" + enzyname)
    lines = conn.getresponse().read().split('\n')
    for i,line in enumerate(lines):
        if ( '<td><a href="http://www.cazy.org/' in line ):
            linkLine = lines[i]
            j = linkLine.find( '"http://www.cazy.org/' ) + 21
            k = linkLine.find( '.html"', j )
            return linkLine[j:k] # beteween first and second double quotes
    return None
    
f = open('enzytable.csv','w')
print("enzyme     ; rank", file=f)
print("enzyme     ; rank")
for line in open("enzylist.csv","r"):
    pieces = line.split(";")
    enzyname = pieces[0].strip()
    enzyInCazy = findEnzymeInCazy(enzyname)
    if ( enzyInCazy != None ):
        print(enzyname.ljust(15) + '; ' + enzyInCazy.ljust(20), file=f)
        print(enzyname.ljust(15) + '; ' + enzyInCazy.ljust(20))
    else:
        print(enzyname.ljust(15) + '; ' + "not found!", file=f)
        print(enzyname.ljust(15) + '; ' + "not found!")
