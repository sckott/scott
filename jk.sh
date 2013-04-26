#!/bin/sh

python remove_yaml.py

pandoc -V geometry:margin=1in -o pdfs/scott_vita.pdf vita_noyaml_nocvaspdf.md
pandoc -V geometry:margin=1in -o pdfs/scott_vita_nocvaspdf.pdf vita_noyaml_nocvaspdf.md

jekyll --server