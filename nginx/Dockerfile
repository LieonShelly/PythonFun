FROM  nginx:latest
ADD default.conf /etc/nginx/conf.d/default.conf
ADD . /nginx
WORKDIR /nginx
RUN chown -R nginx:nginx


