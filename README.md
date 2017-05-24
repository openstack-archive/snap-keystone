# Keystone Snap

This repository contains the source code of the snap for the OpenStack Identity
service, Keystone.

## Installing this snap

The keystone snap can be installed directly from the snap store:

    sudo snap install --edge --classic keystone

The keystone snap is working towards publication across tracks for
OpenStack releases. The edge channel for each track will contain the tip
of the OpenStack project's master branch, with the beta, candidate and
release channels being reserved for released versions. These three channels
will be used to drive the CI process for validation of snap updates. This
should result in an experience such as:

    sudo snap install --classic --channel=ocata/stable keystone
    sudo snap install --classic --channel=pike/edge keystone

## Configuring keystone

The keystone snap supports configuration via its $SNAP_COMMON writable area,
/var/snap/keystone/common/etc. By default the directory structure will
have the following:

    /var/snap/keystone/common/etc/
    ├── keystone
    │   └── conf.d
    │       └── keystone-snap.conf
    ├── nginx
    │   ├── nginx-snap.conf
    │   ├── sites-enabled
    │   │   └── snap
    │   │       └── keystone-snap.conf
    └── uwsgi
        └── snap
            └── keystone-snap.ini

The keystone applications can be configured in a few ways. The directory
structure can be modified to override config as follows:

    /var/snap/keystone/common/etc/
    ├── keystone
    │   ├── conf.d
    │   │   ├── keystone-snap.conf
    │   │   ├── database.conf
    │   │   └── rabbitmq.conf
    │   └── keystone.conf
    ├── nginx
    │   ├── nginx-snap.conf
    │   ├── nginx.conf
    │   ├── sites-enabled
    │   │   ├── snap
    │   │   │   └── keystone-snap.conf
    │   │   └── keystone.conf
    └── uwsgi
        ├── snap
        │   └── keystone-snap.ini
        └── keystone.ini

The keystone configuration can be overridden by adding a keystone.conf
file, and can also be overridden or augmented by writing configuration snippets
to files in the conf.d directory.

The keystone nginx configuration can be overridden by adding an
nginx.conf and new site config files to the sites-enabled directory.
In this case the new nginx.conf file would include the sites-enabled directory.
If nginx.conf exists, nginx-snap.conf will no longer be used.

The keystone uwsgi configuration can be overridden by adding a new
keystone.ini file. If keystone.ini exists, keystone-snap.ini will no longer
be used.

## Logging keystone

The services for the keystone snap will log to its $SNAP_COMMON writable area:
/var/snap/keystone/common/log.

## Managing keystone

The keystone snap will drop privileges to run daemons and commands under
a regular user named snap-keystone. Additionally, permissions and ownership
of files and directories in /var/snap/keystone/common/ are modified to
restrict access from other users.

The keystone snap has alias support that enables use of the well-known
keystone-manage command. To enable the alias, run the following prior to
using the command:

    sudo snap alias keystone.manage keystone-manage

## Restarting keystone services

To restart all keystone services:

    sudo systemctl restart snap.keystone.*

or an individual service can be restarted by dropping the wildcard and
specifying the full service name.

## Building the keystone snap

Simply clone this repository and then install and run snapcraft:

    git clone https://github.com/openstack/snap-keystone
    sudo apt install snapcraft
    cd snap-keystone
    snapcraft

## Support

Please report any bugs related to this snap at:
[Launchpad](https://bugs.launchpad.net/snap-keystone/+filebug).

Alternatively you can find the OpenStack Snap team in `#openstack-snaps` on
Freenode IRC.
