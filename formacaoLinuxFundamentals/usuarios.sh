#!/bin/bash

echo "Criando o diretório '/publico'"
mkdir /publico

echo "Liberando permissões públicas"
chmod 777 /publico

echo "Criando grupos"
groupadd GRP_ADM
groupadd GRP_VEN
groupadd GRP_SEC

echo "Criando criando usuários e ambiente adm"

useradd carlos -c "Carlos ADM" -s /bin/bash -m -p $(openssl passwd -6 senha123)
passwd carlos -e

useradd maria -c "Maria ADM" -s /bin/bash -m -p $(openssl passwd -6 senha123)
passwd maria -e

useradd joao -c "Joao ADM" -s /bin/bash -m -p $(openssl passwd -6 senha123)
passwd joao -e

usermod -G GRP_ADM carlos
usermod -G GRP_ADM maria
usermod -G GRP_ADM joao

mkdir /adm
chown root:GRP_ADM /adm
chmod 770 /adm


echo "Criando usuários e ambiente ven"

useradd debora -m -s /bin/bash -p $(openssl passwd -6 senha123)
passwd debora -e

useradd sebastiana -m -s /bin/bash -p $(openssl passwd -6 senha123)
passwd sebastiana -e

useradd roberto -m -s /bin/bash -p $(openssl passwd -6 senha123)
passwd roberto -e

usermod -G GRP_VEN debora
usermod -G GRP_VEN sebastiana
usermod -G GRP_VEN roberto

mkdir /ven
chown root:GRP_VEN /ven
chmod 770 /ven


echo "Criando usuários e ambiente sec"

useradd josefina -m -s /bin/bash -p $(openssl passwd -6 senha123)
passwd josefina -e

useradd amanda -m -s /bin/bash -p $(openssl passwd -6 senha123)
passwd amanda -e

useradd rogerio -m -s /bin/bash -p $(openssl passwd -6 senha123)
passwd rogerio -e

usermod -G GRP_SEC josefina
usermod -G GRP_SEC amanda
usermod -G GRP_SEC rogerio

mkdir /sec
chown root:GRP_SEC /sec
chmod 770 /sec