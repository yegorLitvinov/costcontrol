mkdir -p ~/.ssh
chmod 0700 ~/.ssh
echo "$ID_RSA" > ~/.ssh/id_rsa
echo "$ID_RSA_PUB" > ~/.ssh/id_rsa.pub
chmod 0600 ~/.ssh/*
echo '195.201.27.44 ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBNSLwIS38fXmWekn7JAymlJ2zXCN8cDnVBVsyHHAV40RuQ/wQMLwZCtoGSKXPsGkK2F60J0VG35F7C2gM9cSgQ=' >> ~/.ssh/known_hosts

cd deploy && ansible-playbook deploy.yml
