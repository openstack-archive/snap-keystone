#!/bin/bash

set -x

sudo mysql -u root << EOF
DROP DATABASE IF EXISTS keystone;
EOF
