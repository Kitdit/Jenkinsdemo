FROM python
# using python image from docker hub
WORKDIR /Selvicode
# creating and changing folder in docker image
COPY Automate.py /Selvicode/
CMD [ "python" , "Automate.py" ]