FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y build-essential
RUN apt-get install -y libssl-dev
RUN pip3 install scrapy
RUN mkdir src
WORKDIR /src
RUN mkdir pages
COPY . .
CMD scrapy crawl obesity
