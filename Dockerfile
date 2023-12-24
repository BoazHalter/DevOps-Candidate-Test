# Use an official Node.js runtime as the base image
FROM node:14

# Create and set the working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the working directory
COPY node-hello/package*.json ./
COPY README.md ./
# Install Node.js dependencies
RUN npm install

# Copy the application files to the working directory
COPY . .

# Expose port 5000
EXPOSE 5000

# Define the command to run the Node.js application on port 5000
CMD ["npm", "start"]
