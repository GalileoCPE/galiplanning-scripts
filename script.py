#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 10:53:48 2017

@author: Mayeul Cantan
@licence: AGPLv3
"""


from bs4 import BeautifulSoup as bs
import os

back_link_href = "/"
back_link_str = "Retour aux plannings"
page_title = "Plannings d'anglais"
infile='/mnt/in.xlsx'
tmpfile='/mnt/tmp.html'
outfile = '/mnt/out.html'

os.system("ssconvert  -T Gnumeric_html:html40frag %s %s" % (infile, tmpfile))

fhandle = open(tmpfile, 'r')
htmlorig = fhandle.read()
fhandle.close()
soup = bs(htmlorig, 'lxml')

#Clean the source a bit by removing every empty <p>
for p in soup.find_all("p",{"string":""}):
    p.decompose()

header = soup.new_tag("select")

captions = soup.find_all("caption")
for c in captions:
    # Add an id to the tag, with underscores  instead of spaces
    id_caption = c.text.replace(" ","_")
    # Change caption tag to details tag (css3)
    c.name = 'details'
    # wrap the previous tag text into a summary tag
    c.string.wrap(soup.new_tag("summary"))
    # Now, wrap the table into the tag (after removing it from its current position)
    c.parent['id'] = id_caption
    c.parent.wrap(c.extract())

# Wrap the tables into a div
main_div = soup.new_tag("div",id="main_content")
for cont in soup.body.contents:
    main_div.append(cont.extract())


back_div = soup.new_tag("div",id="back_link")
back_link = soup.new_tag("a",href=back_link_href)
back_link.string = back_link_str
back_div.append(back_link)

soup.body.append(back_div)
soup.body.append(main_div)

#let's regenerate a nice <head> for our document
charset = soup.new_tag("meta", charset="utf-8")
title = soup.new_tag("title"); title.string = page_title
head = soup.new_tag("head")
head.append(charset) # if you want some custom css, add the sheet here
head.append(title)

soup.body.insert_before(head)
soup.html['lang'] = 'fr'
to_write = "<!DOCTYPE html>\n" + soup.prettify() + '\n'

fhandle = open(outfile,'wb')
fhandle.write(to_write.encode('utf8'))
fhandle.close()
