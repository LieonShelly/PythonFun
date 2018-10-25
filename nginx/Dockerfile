FROM  nginx:latest
ADD default.conf /etc/nginx/conf.d/default.conf
RUN mkdir -p /var/www/media
WORKDIR /var/www/media
RUN chown -R nginx:nginx /var/www/media


