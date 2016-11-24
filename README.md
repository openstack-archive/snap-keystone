# Keystone Snap

This repository contains the source code of the snap for the OpenStack Identity
service, Keystone.

## Installing this snap

The keystone snap can be installed directly from the snap store:

    sudo snap install [--edge] keystone

## Configuring Keystone

Snaps run in an AppArmor and seccomp confined profile, so don't read
configuration from `/etc/keystone` on the hosting operating system install.

This snap supports configuration via the $SNAP\_COMMON writable area for the
snap:

    etc
    ├── keystone
    │   ├── keystone.conf
    └── keystone.conf.d
        ├── database.conf
        ├── keystone-snap.conf
        └── keystone.conf

The keystone applications can be configured in a few ways.

Firstly the WSGI daemon will detect and read `etc/keystone/keystone.conf`
if it exists so you can just place all configuration in the file for each
daemon.

Alternatively the WSGI daemon will load all configuration files from
`etc/keystone.conf.d` - in the above example, database and keystone authtoken
configuration is shared across both daemons using configuration snippets in
separate files in `etc/keystone.conf.d`.

For reference, $SNAP\_COMMON is typically located under
`/var/snap/keystone/common`.

## Managing Keystone

Currently all snap binaries must be run as root; for example, to run the
keystone-manage binary use:

    sudo keystone.manage

## Restarting Keystone services

To restart all keystone services:

    sudo systemctl restart snap.keystone.*

or use the individual service:

    sudo systemctl restart snap.keystone.api

## Building the Keystone snap

Simply clone this repository and then install and run snapcraft:

    git clone https://github.com/openstack-snaps/snap-keystone
    sudo apt install snapcraft
    cd keystone
    snapcraft

## Support

Please report any bugs related to this snap on
[Launchpad](https://bugs.launchpad.net/snap-keystone/+filebug).

Alternatively you can find the OpenStack Snap team in `#openstack-snaps`
on Freenode IRC.
