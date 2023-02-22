# Ansible role - composer
[![Maintainer](https://img.shields.io/badge/maintained%20by-claranet-e00000?style=flat-square)](https://www.claranet.fr/)
[![License](https://img.shields.io/github/license/claranet/ansible-role-composer?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/claranet/ansible-role-composer?style=flat-square)](https://github.com/claranet/ansible-role-composer/releases)
[![Status](https://img.shields.io/github/workflow/status/claranet/ansible-role-composer/Ansible%20Molecule?style=flat-square&label=tests)](https://github.com/claranet/ansible-role-composer/actions?query=workflow%3A%22Ansible+Molecule%22)
[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D2.10-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)
[![Ansible Galaxy](https://img.shields.io/badge/ansible-galaxy-black.svg?style=flat-square&logo=ansible)](https://galaxy.ansible.com/claranet/composer)


> :star: Star us on GitHub — it motivates us a lot!

Install and configure Composer

## :warning: Requirements

* Ansible >= 2.10
* PHP

## :zap: Installation

```bash
ansible-galaxy install claranet.composer
```

## :gear: Role variables

Variable | Default value | Description
---------|---------------|------------
composer_version | **1.10.26** | Composer version to install
composer_install_dir | **/usr/local/bin** | Composer bin folder to install the Composer bin
composer_self_update | **false** | Enable Composer self update after installation
composer_force_update | **false** | Enable Composer force update version (if false, Composer will not be updated with the new specified version if *composer_version* var changed)

## :arrows_counterclockwise: Dependencies

N/A

## :pencil2: Example Playbook

```yaml
---
- hosts: all
  roles:
    - claranet.composer
```

## :closed_lock_with_key: [Hardening](HARDENING.md)

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
