FROM python:3.6

RUN apt-get update && \
  apt-get -qq -y install  libxpm4 libxrender1 libgtk2.0-0 libnss3\ 
  libgconf-2-4  libpango1.0-0 libxss1 libxtst6 fonts-liberation\ 
  libappindicator1 xdg-utils

RUN apt-get -y install \
  xvfb gtk2-engines-pixbuf \
  xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable \
  imagemagick x11-apps zip wget

# Set up the Chrome PPA
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Update the package list and install chrome
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable


COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
ADD . .