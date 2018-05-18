FROM python:3.7

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1
ENV APP_ROOT /code
ENV DEBUG False

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


# Copy in your requirements file
ADD requirements.txt /requirements.txt

# Install build deps, then run `pip install`, then remove unneeded build deps all in a single step. Correct the path to your production requirements file, if needed.
RUN pip install virtualenvwrapper
RUN python3 -m venv /venv
RUN /venv/bin/pip install -U pip
RUN /venv/bin/pip install --no-cache-dir -r /requirements.txt

# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}
ADD . ${APP_ROOT}
COPY mime.types /etc/mime.types

# uWSGI will listen on this port
EXPOSE 8000

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
# RUN if [ -f manage.py ]; then /venv/bin/python manage.py collectstatic --noinput; fi

# Start uWSGI
CMD [ "/venv/bin/uwsgi", "--ini", "/code/uwsgi.ini"]