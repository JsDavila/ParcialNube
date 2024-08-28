FROM python:3.6
COPY . /app2
# The EXPOSE instruction indicates the ports on which a container
# will listen for connections
# Since Flask apps listen to port 5000  by default, we expose it
EXPOSE 5002

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction
# creates a directory with this name if it doesn’t exist
WORKDIR /app2

# Install any needed packages specified in requirements.txt
#COPY requirements.txt /app
#RUN pip install flask
#RUN pip install Flask-Cors
#RUN pip install Flask-SQLAlchemy
#RUN pip install mysqlclient
COPY requirements.txt /app2/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Run app.py when the container launches
COPY run.py /app2
COPY config.py /app2
CMD python run.py config.py                                                       
