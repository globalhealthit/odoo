FROM nginx:1.23-alpine
ARG NGINX_CONF

RUN rm /etc/nginx/conf.d/default.conf
COPY ./odoo.conf /etc/nginx/conf.d

