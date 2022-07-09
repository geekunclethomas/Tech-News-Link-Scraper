#!/bin/bash

#This program give us latest news of technology 

DELAY=1 #Number of seconds to display results
arr=('-' '\' '|' '/')

spinner(){

while true; do
    for c in "${arr[@]}"; do
        echo -en "\r $c "
        sleep .5
    done
    break
done
}




main() {

cat << EOF 

    What would you like to read today King *Mani*?

    1.Hacker News
    2.Hardware News
    3.How To Geek
    4.Quit: 
EOF
read Sel

spinner

if [ $Sel = 4 ];then
    return 1

else

    python3 /home/rose/news/news.py $Sel | more 
fi

echo "  Would You Like To Continue My Lord: [y/n] "
echo ""
read Continue

if [ $Continue = 'y' ];then
     main

else
    echo " Hope to See You Again My Lord"
    return 1
fi
}

main








