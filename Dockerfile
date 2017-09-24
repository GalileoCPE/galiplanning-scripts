# AUTHOR Mayeul Cantan
# Copyright (c) 2017 Mayeul Cantan, Galiléo CPE
# License: AGPLv3

FROM debian:stretch
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install gnumeric
RUN apt-get -y install python3-bs4
ADD script.py /usr/bin/conversionScript
RUN chmod +x /usr/bin/conversionScript
VOLUME /mnt
CMD conversionScript
