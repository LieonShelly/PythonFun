FROM  nginx:latest
ADD default.conf /etc/nginx/conf.d/default.conf
RUN mkdir -p /var/www/media
WORKDIR /var/www/media
ADD 1_www.lieoncx.cn_bundle.crt /var/www/media/
ADD 2_www.lieoncx.cn.key /var/www/media/
RUN chown -R nginx:nginx /var/www/media


