# pull official base image
FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies...
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev \
                       jpeg-dev \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       openjpeg-dev \
                       tiff-dev \
                       tk-dev \
                       tcl-dev \
                       harfbuzz-dev \
                       fribidi-dev

# create the app user & associated group with explicit uid/gid for read
# access to docker secrets (controlled using file permissions)
RUN addgroup -S -g 101 djrf && adduser -S -G djrf -u 101 djrf

# define directory structure
ENV HOME=/home/djrf/
ENV API_ROOT=${HOME}api/
ENV PUBLIC_ROOT=${HOME}public/

# WORKDIR automatically creates directories as needed
WORKDIR $API_ROOT
RUN mkdir $PUBLIC_ROOT

# install application dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

# copy project sources & startup script
#RUN mkdir api
#RUN mkdir receipts
COPY api ./api
COPY receipts ./receipts
COPY .env.dev manage.py ./
COPY entrypoint.sh $HOME

# chown all the files to the application user
RUN chown -c djrf:djrf $HOME
RUN chown -Rc djrf:djrf $HOME

# change to the app user
USER djrf

# run entrypoint.sh
ENTRYPOINT ["/home/djrf/entrypoint.sh"]
