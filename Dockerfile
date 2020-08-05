FROM ubuntu:18.04
COPY ./requirements.txt .
COPY ./conftest.py $HOME/gmail_send_simple_test
COPY ./target.json $HOME/gmail_send_simple_test
ADD fw $HOME/gmail_test/fw
ADD data $HOME/gmail_test/data
ADD fixture $HOME/gmail_test/fixture
ADD tests $HOME/gmail_test/tests
ADD page_objects $HOME/gmail_test/page_objects
ADD model $HOME/gmail_test/model

RUN apt-get update  && apt-get install python3-pip -y
RUN pip3 install -r requirements.txt



