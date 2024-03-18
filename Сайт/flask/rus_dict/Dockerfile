FROM python:3.10.12
COPY . /rus_dict
WORKDIR /rus_dict
RUN apt-get upgrade && apt-get install make
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN make /rus_dict
EXPOSE 15555
CMD python app.py
