#!/bin/sh

python remove_yaml.py

pandoc -V geometry:margin=1in -o pdfs/scott_vita.pdf vita_noyaml.md

jekyll --server