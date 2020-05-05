#!/bin/bash
echo -e '\e[7;37m'type the number of your choice'\e[0m'
echo -e '\e[1;4m'"(1)"'\e[0m' hbots
echo -e '\e[1;4m'"(2)"'\e[0m' hsites
echo -e '\e[1;4m'"(3)"'\e[0m' hmisc
echo -e '\e[1;4m'"(4)"'\e[0m' computertime
echo -e '\e[1;4m'"(5)"'\e[0m' there are no more choices
read -n1 input
if [ "$input" != "1" ] && [ "$input" != "2" ] && [ "$input" != "3" ] && [ "$input" != "4" ] && [ "$input" != "5" ]; then
	echo -e "\nplease choose 1 2 3 4 or 5"
fi
if [ "$input" == "1" ] || [ "$input" == "2" ] || [ "$input" == "3" ] || [ "$input" == "4" ] || [ "$input" == "5" ]; then
	if (( "$input" == "1" )); then
		echo -e "\nyou chose hbots"
		python3 ~/pysvr/bots.py
		echo "bye"
	fi
	if (( "$input" == "2" )); then
		echo -e "\nyou chose hsites"
		python3 ~/pysvr/sites.py
		echo "bye"
	fi
	if (( "$input" == "3" )); then
		echo -e "\nyou chose hmisc"
		python3 ~/pysvr/misc.py
		echo "bye"
	fi
	if (( "$input" == "4" )); then
		echo -e "\nyou chose computertime"
		python3 ~/pysvr/chem.py
		echo "bye"
	fi
	if (( "$input" == "5")); then
		echo -e "\ndumbass"
	fi
fi