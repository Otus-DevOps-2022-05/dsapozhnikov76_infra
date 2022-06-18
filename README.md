# dsapozhnikov76_infra
dsapozhnikov76 Infra repository

Самостоятельное задание

1. ****Исследовать способ подключения к someinternalhost в одну
команду:****
````
ssh -i ~/.ssh/appuser -J appuser@51.250.73.188 appuser@10.128.0.6
````

2. ****Вариант решения для подключения из консоли при помощи
команды вида ssh someinternalhost из локальной консоли рабочего
устройства:****

Добавить файл конфигурации **~/.ssh/config:**

````
Host bastion
     Hostname 51.250.73.188
     User appuser
     Port 22
     IdentityFile ~/.ssh/appuser

Host someinternalhost
     User appuser
     ProxyCommand ssh bastion -W 10.128.0.6:22
````

