FROM python:3.6
COPY . /app
# The EXPOSE instruction indicates the ports on which a container
# will listen for connections
# Since Flask apps listen to port 5000  by default, we expose it
EXPOSE 5001

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction
# creates a directory with this name if it doesn’t exist
WORKDIR /app

# Install any needed packages specified in requirements.txt
#COPY requirements.txt /app
RUN pip install flask
RUN pip install Flask-Cors
RUN pip install Flask-MySQLdb
RUN pip install Flask-SQLAlchemy
RUN pip install mysqlclient
RUN pip install SQLAlchemy
# Run app.py when the container launches
COPY run.py /app
COPY config.py /app
CMD python run.py config.py
