# Keystone Snap

This repository contains the source code of the snap for the OpenStack Identity
service, Keystone.

## Installing this snap

The keystone snap can be installed directly from the snap store:

    sudo snap install --channel=ocata/edge keystone

The keystone snap is working towards publication across tracks for
OpenStack releases. The edge channel for each track will contain the tip
of the OpenStack project's master or stable branch, with the beta, candidate,
and stable channels being reserved for released versions. The same version
will be published progressively to beta, then candidate, and then stable once
CI validation completes for the channel. This should result in an experience
such as:

    sudo snap install --channel=ocata/stable keystone
    sudo snap install --channel=pike/edge keystone

## Configuring keystone

The keystone snap gets its default configuration from the following $SNAP
and $SNAP_COMMON locations:

    /snap/keystone/current/etc/
    └── keystone
        ├── keystone.conf
        └── ...

    /var/snap/keystone/common/etc/
    ├── keystone
    │   └── keystone.conf.d
    │       └── keystone-snap.conf
    ├── nginx
    │   ├── snap
    │   │   ├── nginx.conf
    │   │   └── sites-enabled
    │   │       └── keystone.conf
    └── uwsgi
        └── snap
            └── keystone.ini

The keystone snap supports configuration updates via its $SNAP_COMMON writable
area. The default keystone configuration can be overridden as follows:

    /var/snap/keystone/common/etc/
    ├── keystone
    │   ├── keystone.conf.d
    │   │   ├── keystone-snap.conf
    │   │   ├── database.conf
    │   │   └── rabbitmq.conf
    │   └── keystone.conf
    ├── nginx
    │   ├── snap
    │   │   ├── nginx.conf
    │   │   └── sites-enabled
    │   │       └── keystone.conf
    │   ├── nginx.conf
    │   ├── sites-enabled
    │   │   └── keystone.conf
    └── uwsgi
        ├── snap
        │   └── keystone.ini
        └── keystone.ini

The keystone configuration can be overridden or augmented by writing
configuration snippets to files in the keystone.conf.d directory.

Alternatively, keystone configuration can be overridden by adding a full
keystone.conf file to the keystone/ directory. If overriding in this way, you'll
need to either point this config file at additional config files located in $SNAP,
or add those to $SNAP_COMMON as well.

The keystone nginx configuration can be overridden by adding an nginx/nginx.conf
and new site config files to the nginx/sites-enabled directory. In this case the
nginx/nginx.conf file would include that sites-enabled directory. If
nginx/nginx.conf exists, nginx/snap/nginx.conf will no longer be used.

The keystone uwsgi configuration can be overridden similarly by adding a
uwsgi/keystone.ini file. If uwsgi/keystone.ini exists, uwsgi/snap/keystone.ini
will no longer be used.

## Logging keystone

The services for the keystone snap will log to its $SNAP_COMMON writable area:
/var/snap/keystone/common/log.

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
