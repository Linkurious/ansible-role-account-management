account-management
==================

[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.com/Temelio/ansible-role-account-management.svg?branch=master)](https://travis-ci.com/Temelio/ansible-role-account-management)
[![Updates](https://pyup.io/repos/github/Temelio/ansible-role-statsd/shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-statsd/)
[![Python 3](https://pyup.io/repos/github/Temelio/ansible-role-statsd/python-3-shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-statsd/)
[![Ansible Role](https://img.shields.io/ansible/role/12562.svg)](https://galaxy.ansible.com/Temelio/statsd/)
[![GitHub tag](https://img.shields.io/github/tag/Temelio/ansible-role-statsd.svg)](https://github.com/Temelio/ansible-role-stasd/tags)


Manage users and groups, and authorized keys.

## Requirements

This role requires Ansible 2.4 or higher, and platform requirements are listed
in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Ubuntu Trusty
- Ubuntu Xenial
- Ubuntu Bionic
- Debian Stretch

and use:
- Ansible 2.4.x
- Ansible 2.5.x
- Ansible 2.6.x
- Ansible 2.7.x

### Running tests

#### Using Docker driver

```
$ tox
```

### Default role variables

``` yaml
Follow the possible variables with their default values
# if you want to use skel set this variable to true
am_copy_skeleton_files: false
# Template:
#  - dest: '/etc/skel/.vimrc'
#    src: "{{ role_path }}/files/vimrc"
#    owner: 'root'
#    group: 'root'
#    mode: '0644'
am_skeleton_files_config: []

# List of groups to create
#
# Template :
# - name         : my-group     # Name of group
#   gid          : 1500         # Set the GID       (Default : False)
#   state        : absent       # Should exists ?   (Default : present)
#   is_system    : True         # Is system group ? (Default : False)
account_management_groups : []

# List of users to create
#
# Template :
# - name         : my-user      # Name of user
#   append       : False        # Add or replace add groups (Default : True)
#   comment      : "Foobar"     # Describe user             (Default : '')
#   createhome   : False        # Explicit                  (Default : True)
#   home_mode    : 0750         # Permissions for home      (Default : 0700)
#   group        : "my-user"    # Primary user group        (Default : username)
#   groups       : []           # Additionnal groups
#   uid          : 1500         # Set the UID               (Default : False)
#   password     : "qsdqdqsd"   # Encrypted password        (Default : False)
#   state        : absent       # Should exists ?           (Default : present)
#   is_system    : True         # Is system user ?          (Default : False)
#   remove       : True         # Should be removed ?       (Default : False)
#   skeleton     : /skels/foo   # Skeleton used at create   (Default : False)
#   home         : "/var/foo"   # Home path  (Default : /home/username)
#   shell        : "/bin/sh"    # User shell (Default : /usr/sbin/nologin)
#   authorized_public_keys : [] # Public ssh keys used for authentication
#   exclusive_public_keys  : False # Only listed keys exists in authorized-keys
#                                  # (Default : True)
#
# Template used for authorized keys entries
# - filename : "/etc/public-keys/foo.key"   # Filename where is the public key
#   state    : "absent"                     # Used for auth (Default : present))
#   key_options : ""                        # Add ssh options for this key
#
account_management_users : []
```

## Generating a password hash:

# On Debian/Ubuntu (via the package "whois")
mkpasswd --method=SHA-512 --rounds=4096

# OpenSSL (note: this will only make md5crypt.  While better than plantext it should not be     considered fully secure)
openssl passwd -1

# Python (change password and salt values)
python -c "import crypt, getpass, pwd; print crypt.crypt('password', '\$6\$SALT\$')"

# Perl (change password and salt values)
perl -e 'print crypt("password","\$6\$SALT\$") . "\n"'

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: temelio.account-management }
```

## License

MIT

## Author Information

L Machetel (for Temelio company)
Fork from Alexandre Chaussier (for Infopen company)
