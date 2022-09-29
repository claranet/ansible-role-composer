#!/usr/bin/env python

import os
import stat
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")

composer_install_dir = "/usr/local/bin"

composer_bin_file = composer_install_dir + "/composer.phar"
composer_link_file = composer_install_dir + "/composer"

def test_composer_link_file(host):
    file = host.file(composer_link_file)
    assert file.exists
    assert file.is_file
    assert file.user == "root"
    assert file.group == "root"

def test_composer_bin_file(host):
    file = host.file(composer_bin_file)
    assert file.exists
    assert file.is_file
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o755

def test_composer_output(host):
    command = host.run("composer --version")
    assert command.rc == 0
    assert command.succeeded
    assert command.stderr == ""
    print(f"\n{command.stdout}")
