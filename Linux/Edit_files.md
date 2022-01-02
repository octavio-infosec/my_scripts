# Useful shell commands to manipulate files in Linux. 

Join usernames.txt and password.txt files with a ":" placed in between each credential:

` 
for var in $(paste -d " " usernames.txt passwords.txt | tr -s " " | cut -d " " -f 1,2 --output-delimiter=':'); do echo -n $var | base64;done
`
