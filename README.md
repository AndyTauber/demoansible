# demoansible

Ansible Notes
https://github.com/maaydin/ansible-tutorial/blob/master/Ansible%20Tutorial.pdf

collections: https://docs.ansible.com/ansible/latest/collections/index.html


We will use user:ansible

On server and client, create the user: ansible

# adduser ansible
# usermod -aG sudo ansible

Setup ssh keys
login as ansible
ssh-keygen

copy key to .ssh/authorized_keys

on client, setup /etc/sudoers
ansible ALL=(ALL) NOPASSWD:ALL



Install Ansible on server

sudo apt-add-repository ppa:ansible/ansible
sudo apt update
sudo apt install ansible

Setup inventory file

sudo vi /etc/ansible/hosts

[clients]
client1 ansible_host=172.16.66.129

[all:vars]
ansible_python_interpreter=/usr/bin/python3



test
ansible all -m ping -u ansible

ansible -m shell -a 'hostname' client1

ansible -m shell -a "whoami" client1 --become
