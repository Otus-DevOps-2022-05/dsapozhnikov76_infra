import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

# check if MongoDB is enabled and running
def test_mongo_running_and_enabled(host):
    mongo = host.service("mongodb")
    assert mongo.is_running
    assert mongo.is_enabled

# check if configuration file contains the required line
def test_config_file(host):
    config_file = host.file('/etc/mongodb.conf')
    assert config_file.contains('bindIp: 0.0.0.0')
    assert config_file.is_file

# check if MongoDB is listenning port 27017
def test_mongo_listenning_port(host):
    port = host.socket("tcp://0.0.0.0:27017")
    assert port.is_listening
