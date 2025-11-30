FROM nginx:alpine

# Apaga arquivos padrão do nginx
RUN rm -rf /usr/share/nginx/html/*

# Copia seus arquivos do front
COPY ./frontend /usr/share/nginx/html