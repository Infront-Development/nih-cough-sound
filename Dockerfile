# load python 3.8 dependencies using slim debian 11 image.
FROM python:3.8-slim-bullseye

# build variables.
ENV DEBIAN_FRONTEND noninteractive

# install Microsoft SQL Server requirements.
ENV ACCEPT_EULA=Y
RUN apt-get update -y && apt-get update \
  && apt-get install -y --no-install-recommends curl gcc g++ gnupg unixodbc-dev

# Add SQL Server ODBC Driver for Debian 11
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg \
  && echo "deb [arch=amd64,arm64,armhf signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/11/prod bullseye main" > /etc/apt/sources.list.d/mssql-release.list \
  && apt-get update \
  && ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql18 mssql-tools18 \
  && echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bash_profile \
  && echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc

WORKDIR /code
COPY requirements.txt  /code
RUN pip install --upgrade pip==24.0 && \
    pip install -r requirements.txt
COPY . /code
EXPOSE 8000