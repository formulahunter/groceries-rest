#!/bin/sh

# djrf is the application user by which django connects to the database
# read password from file & pipe to the "interactive" --pwprompt
printf "$(cat /run/secrets/dj_pass)\n$(cat /run/secrets/dj_pass)\n" | createuser --createdb --no-createrole --no-superuser --pwprompt djrf
createdb --owner=djrf djrf
createdb --owner=djrf groceries

echo "user & databases created"

