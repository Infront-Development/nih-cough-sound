FROM mcr.microsoft.com/mssql/server:2019-latest

# Switch to root user for access to apt-get install
USER root

# Install node/npm
RUN apt-get -y update  && \
        apt-get install -y curl

# Install tedious, the driver for SQL Server for Node.js

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

# Grant permissions for the import-data script to be executable
RUN chmod +x /usr/src/app/import-data.sh

EXPOSE 1443

# Switch back to mssql user and run the entrypoint script
# USER mssql
ENTRYPOINT /bin/bash ./entrypoint.sh
CMD 
