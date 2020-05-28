FROM debian:10

WORKDIR /usr/src/app
RUN apt-get update
RUN apt-get install -y software-properties-common curl python3 python3-pip nano
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./api.py" ]