# install all packages listed in packages.txt
while read -r line; do sudo apt install $line; done < packages.txt
