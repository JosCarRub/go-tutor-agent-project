FROM node:20-alpine AS builder

WORKDIR /app

COPY package.json package-lock.json* ./

RUN npm install

COPY . .

RUN npm run build

FROM node:20-alpine

WORKDIR /app

COPY --from=builder /app/dist ./dist


RUN npm install -g serve

EXPOSE 4321


CMD ["serve", "dist", "-l", "4321"]