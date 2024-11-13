#!/bin/bash  

# Create a folder 'TXT' in the home directory  
mkdir ~/TXT  
  
mv -v ~/ *.txt ~/TXT/  

# Count the number of files moved  
count=$(ls ~/TXT/*.txt 2>/dev/null | wc -l)  

# Print the number of txt files moved  
echo "$count txt files moved"