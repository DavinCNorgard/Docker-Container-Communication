FROM mongo:latest

# Set working directory
WORKDIR /usr/src/app

# Copy MongoDB config file
COPY ./mongod.conf /etc/mongod.conf

# Expose MongoDB port
EXPOSE 27017

# Start MongoDB server
CMD ["mongod", "--config", "/etc/mongod.conf"]