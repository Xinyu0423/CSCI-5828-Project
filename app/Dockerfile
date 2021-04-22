FROM node:alpine

WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH

COPY . /app
RUN npm install && \ 
    npm run build --production

EXPOSE 3000

CMD next start -p $PORT