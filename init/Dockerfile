FROM python:3
ADD initdb.py /
ADD ../data.csv /
RUN pip install pandas
CMD [ "python", "./initdb.py" ]