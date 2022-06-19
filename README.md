# dsapozhnikov76_infra
dsapozhnikov76 Infra repository

# ДЗ 3

1. ****Исследовать способ подключения к someinternalhost в одну
команду:****
````
ssh -i ~/.ssh/appuser -J appuser@51.250.80.65 appuser@10.128.0.6
````

2. ****Вариант решения для подключения из консоли при помощи
команды вида ssh someinternalhost из локальной консоли рабочего
устройства:****

Добавить файл конфигурации **~/.ssh/config:**

````
Host bastion
     Hostname 51.250.80.65
     User appuser
     Port 22
     IdentityFile ~/.ssh/appuser

Host someinternalhost
     User appuser
     ProxyCommand ssh bastion -W 10.128.0.6:22
````

3. ****Подключение через VPN****

bastion_IP = 51.250.80.65

someinternalhost_IP = 10.128.0.6

4. ****Доп. задание - Подключение сертификата LetsEncrypt****

Адрес - [https://51-250-80-65.sslip.io/](https://51-250-80-65.sslip.io/)