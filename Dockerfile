FROM python:3

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get -y install locales && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TERM xterm
ENV TZ JST-9

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install pipenv
RUN mkdir /var/send_smart
COPY . /var/send_smart
WORKDIR /var/send_smart
RUN pipenv install --system --deploy
