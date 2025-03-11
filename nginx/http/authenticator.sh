#!/bin/bash
echo $CERTBOT_VALIDATION > /var/www/.well-known/acme-challenge/$CERTBOT_TOKEN
