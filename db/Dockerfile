# syntax=docker/dockerfile:1
FROM postgres:13.3-alpine

# the official postgres image automatically runs `.sql` and `.sh` scripts
# in the `docker-entrypoint-initdb.d` directory "in sorted name order as
# defined by the current locale" after startup (but only if the container
# is started with an empty postgres data directory)

# custom initialization scripts must be placed in `init_files/` to be copied
# into this image and run after database startup
COPY init_files/ /docker-entrypoint-initdb.d/
