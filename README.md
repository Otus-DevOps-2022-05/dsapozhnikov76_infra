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



# ДЗ 4

testapp_IP = 51.250.78.161

testapp_port = 9292

# ДЗ 6

1. Установил terraform 
2. Добавил в main.tf провайдера Yandex
3. Cделал terraform init
4. Собрал файл ~/.terraformrc со ссылкой на mirror провайдера
````
provider_installation {
  network_mirror {
    url = "https://terraform-mirror.yandexcloud.net/"
    include = ["registry.terraform.io/*/*"]
  }
  direct {
    exclude = ["registry.terraform.io/*/*"]
  }
}
````
5. Выполнил настройку main.tf чтобы создавать VM
   - Сделал создание VM по образу reddit-base
   - Добавил provisioning, connection с пользователем appuser
   - Проверил, что VM создается и доступен

6. Задание со звездой, добавил балансер, переделал main.tf на создание 2 VM

## ДЗ 7

1. Удалите из папки terraform файлы main.tf, outputs.tf, terraform.tfvars, 
    variables.tf, так как они теперь перенесены в stage и prod  **СДЕЛАНО** 
2. Параметризируйте конфигурацию модулей насколько считаете нужным **СДЕЛАНО**
3. Отформатируйте конфигурационные файлы, используя команду terraform fmt **СДЕЛАНО**
4. Настройте хранение стейт файла в удаленном бекенде (remote backends) для окружений 
   stage и prod, используя Yandex Object Storage в качестве бекенда. Описание бекенда 
   нужно вынести в отдельный файл backend.tf **СДЕЛАНО**
