# Build step 1(installing node modules and preparing compiled build)
FROM node:16.15.0-alpine as build
WORKDIR ./app
ENV PATH /app/node_modules/.bin:$PATH
COPY /app/package.json ./
RUN npm i --silent
COPY . ./
RUN npm run build

# Build step 2(Deploying build on NGINX)
FROM nginx:1.17-alpine
RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*
RUN rm -rf /usr/share/nginx/html/*
COPY --from=build /app/nginx/nginx.conf /etc/nginx/conf.d/default.conf:ro
COPY --from=build /app/dist /usr/share/nginx/html