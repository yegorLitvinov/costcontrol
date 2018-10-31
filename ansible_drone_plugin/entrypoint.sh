mkdir -p ~/.ssh
chmod 0700 ~/.ssh
printf "$ID_RSA" > ~/.ssh/id_rsa
printf "$ID_RSA_PUB" > ~/.ssh/id_rsa.pub
chmod 0600 -R ~/.ssh/*
echo '195.201.27.44 ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBNSLwIS38fXmWekn7JAymlJ2zXCN8cDnVBVsyHHAV40RuQ/wQMLwZCtoGSKXPsGkK2F60J0VG35F7C2gM9cSgQ=' >> ~/.ssh/known_hosts

#
ls -lah ~/.ssh
cat ~/.ssh/id_rsa.pub
#

cd deploy
bash setup.sh
ansible-playbook deploy.yml
