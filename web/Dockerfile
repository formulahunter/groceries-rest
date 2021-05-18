FROM nginx:1.20-alpine

# the default config causes syntax problems in the main config
# they're related to include directives but not worth solving right now
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/
