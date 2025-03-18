
Pour ajouter un utilisateur au groupe `sudo`, tu peux utiliser la commande suivante :

bash

CopierModifier

`sudo usermod -aG sudo debian`

----


```
version: "3.8"

services:
  reverse-proxy:
    image: traefik:latest
    command:
      - "--api.insecure=false"
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.myresolver.acme.tlschallenge=true"
      - "--certificatesresolvers.myresolver.acme.email=contact@learn-it.ovh"
      - "--certificatesresolvers.myresolver.acme.storage=/letsencrypt/acme.json"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - "../letsencrypt:/letsencrypt"
      - "/var/run/docker.sock:/var/run/docker.sock:ro"
    restart: always

  web:
    image: nginx:alpine
    volumes:
      - ./html:/usr/share/nginx/html:ro
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.web.rule=Host(`groupe3.learn-it.ovh`)"
      - "traefik.http.routers.web.entrypoints=websecure"
      - "traefik.http.routers.web.tls.certresolver=myresolver"
    restart: always

  wordpress:
    image: wordpress:latest
    environment:
      WORDPRESS_DB_HOST: wordpress
      WORDPRESS_DB_USER: user
      WORDPRESS_DB_PASSWORD: password
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - wordpress_data:/var/www/html
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.wordpress.rule=Host(`blog.groupe3.learn-it.ovh`)"
      - "traefik.http.routers.wordpress.entrypoints=websecure"
      - "traefik.http.routers.wordpress.tls.certresolver=myresolver"
    restart: always
    depends_on:
      - wordpress_data

  glpi:
    image: diouxx/glpi
    environment:
      GLPI_DB_HOST: glpi
      GLPI_DB_USER: user
      GLPI_DB_PASSWORD: password
      GLPI_DB_NAME: glpi
    volumes:
      - glpi_data:/var/www/html
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.glpi.rule=Host(`helpdesk.groupe3.learn-it.ovh`)"
      - "traefik.http.routers.glpi.entrypoints=websecure"
      - "traefik.http.routers.glpi.tls.certresolver=myresolver"
    restart: always
    depends_on:
      - glpi_data

  adminer:
    image: adminer
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.adminer.rule=Host(`admin.groupe3.learn-it.ovh`)"
      - "traefik.http.routers.adminer.entrypoints=websecure"
      - "traefik.http.routers.adminer.tls.certresolver=myresolver"
    restart: always

  db_glpi:
    image: mysql:latest
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: glpi
      MYSQL_USER: user
      MYSQL_PASSWORD: password
    volumes:
      - glpi_data:/var/lib/mysql
    restart: always

  db_wordpress:
    image: mysql:latest
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: wordpress
      MYSQL_USER: user
      MYSQL_PASSWORD: password
    volumes:
      - wordpress_data:/var/lib/mysql
    restart: always



```


on créer une db par service