#!/usr/bin/env bash
if [[ -z "$MUESLI_TESTMODE" ]]
then
    sed 's/\/\/\//\/\/postgres@postgres\//' muesli.yml.example | sed 's/localhost/0.0.0.0/' > muesli.yml
    sed 's/\/\/\//\/\/postgres@postgres\//' alembic.ini.example > alembic.ini
    echo "Sleeping for 3s ..."; sleep 3;
    echo "Generating configs ... "
    python3 -m smtpd -n -c DebuggingServer localhost:25 &
fi

echo "Running database upgrade ... "
alembic upgrade head
echo -n "IP-address: "
ip -4 addr show | grep -oP "(?<=inet ).*(?=/)" | grep -ve "127.0.0.1"

if [[ -z "$MUESLI_TESTMODE" ]]
then
    su -c /opt/muesli4/muesli-test muesli
else
    su -c /opt/muesli4/muesli-serve muesli
fi
