# Base image
FROM node:lts-alpine3.17

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json
COPY ./package.json /app/package.json
COPY ./package-lock.json /app/package-lock.json

# Install project dependencies
RUN npm install

# Copy the rest of the application
COPY . /app

# List files to debug
RUN ls -la /app
RUN ls -la /app/src

# Expose a port
EXPOSE 3000

# Executables
CMD [ "npm", "run", "serve" ]