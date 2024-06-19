#Base image
FROM node:lts-alpine3.17

# Set the working directory
WORKDIR /app

# Copy the package.json
COPY ./package.json /app/package.json

# install project dependencies
RUN npm install

# Expose a port
EXPOSE 3000

# Executables
CMD [ "npm", "run", "dev" ]
