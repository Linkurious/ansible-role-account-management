"""
Role tests
"""
import os
import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name,gid', [
    ('my-group', None),
    ('my-group2', 1500),
    ('my-user3', 1503),
])
def test_groups(host, name, gid):
    """
    Tests about groups
    """

    group = host.group(name)

    if gid is None:
        assert group.exists is False
    else:
        assert group.exists
        assert group.gid == gid


def test_not_existing_user(host):
    """
    Tests user not exists if state is 'absent'
    """

    assert host.user('my-user').exists is False


def test_user_with_default_values(host):
    """
    Tests user exists if state is 'present'
    """

    user = host.user('my-user2')
    assert user.exists is True
    assert user.group == 'my-user2'

    # Home testing
    user_home = host.file('/home/my-user2')
    assert user_home.exists is True
    assert user_home.is_directory is True
    assert user_home.mode == 0o750
    assert user_home.user == 'my-user2'
    assert user_home.group == 'my-user2'


def test_user_with_custom_values(host):
    """
    Tests user exists if state is 'present' and custom values
    """

    user = host.user('my-user3')
    assert user.exists is True
    assert user.uid == 1503
    assert user.gid == 1503
    assert user.group == 'my-user3'
    assert user.groups == ['my-user3', 'my-group2']
    assert user.home == '/home/my-user3'
    assert user.shell == '/bin/sh'

    # Home testing
    user_home = host.file('/home/my-user3')
    assert user_home.exists is True
    assert user_home.is_directory is True
    assert user_home.mode == 0o755
    assert user_home.user == 'my-user3'
    assert user_home.group == 'my-user3'

    # Skeleton testing
    assert host.file('/home/my-user3/.bashrc').exists is True
    assert host.file('/home/my-user3/.profile').exists is True
