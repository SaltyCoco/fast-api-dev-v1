#!/bin/bash

# This would be converted into a k8 job.
su - postgres
mkdir -p ~/postgres/backups
crontab -e
0 0 * * 0 pg_dump -U postgres db_name | gzip > backup_file.gz
