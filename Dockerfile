# Use a lightweight Nginx image to serve the static files
FROM nginx:alpine

# Copy all the static files from the current directory into Nginx's web root directory
COPY . /usr/share/nginx/html

# Expose port 80, which is the default for Nginx
EXPOSE 80

# The default command runs Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
