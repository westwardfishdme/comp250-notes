#!/usr/bin/env bash

while true; do 
pandoc --from=markdown --to=pdf ./paper_draft.md --citeproc --bibliography=paper.bib -o mnemosyne.pdf;
done
