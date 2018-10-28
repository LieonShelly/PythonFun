FROM  nginx:latest
ADD newnginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /var/www/media
WORKDIR /var/www/media
ADD lieoncx.cn.crt /var/www/media/
ADD lieoncx.cn.key /var/www/media/
RUN chown -R nginx:nginx /var/www/media


