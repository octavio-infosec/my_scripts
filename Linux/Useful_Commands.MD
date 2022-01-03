# Useful Linux commands. In no particular order. Use ctrl + F to find information.

Decode base64 string:

`
echo -n "string==" | base64 -d
`

Execute base64 string:

`
echo 'ZWNob=' | base64 -d | bash
`

Encode file line-by-line:

`
for var in $(cat credential.txt); do echo -n $var | base64;done
`

Join usernames.txt and password.txt files with a ":" placed in between each credential. Then encode each entry line-by-line:

` 
for var in $(paste -d " " usernames.txt passwords.txt | tr -s " " | cut -d " " -f 1,2 --output-delimiter=':'); do echo -n $var | base64;done
`
