FROM  nginx:latest
ADD default.conf /etc/nginx/conf.d/default.conf
RUN mkdir -p /var/www/media
RUN mkdir -p /var/www/keys
ADD 1_www.lieoncx.cn_bundle.crt /var/www/keys/1_www.lieoncx.cn_bundle.crt
ADD 2_www.lieoncx.cn.key /var/www/keys/2_www.lieoncx.cn.key
WORKDIR /var/www/media
RUN chown -R nginx:nginx /var/www/media


