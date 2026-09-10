#!/usr/bin/env bash
# Gets the keywords from each .md file and their count

get_keywords(){
  # get all keywords
  grep -hr -A1 -E "^(\*\*Keywords:\*\*)" . | grep -v Foo | grep -v Keywords | awk -F ', ' '{ printf("%s\n%s\n%s\n%s\n", $1, $2, $3, $4, $5 ) }' | sort | grep -v '\--'
}

SAVEIFS=$IFS
IFS=$'\n'
kw=$(get_keywords|uniq)
keywords=($kw)

for i in $kw; do
  echo "|$i| $(get_keywords|grep $i| wc -l)|"
done
IFS=$SAVEIFS
