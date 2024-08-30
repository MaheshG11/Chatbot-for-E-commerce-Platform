FROM ubuntu
# Install.

RUN apt update -y
RUN apt upgrade -y
RUN apt install software-properties-common -y
RUN apt install python3-pip -y
RUN apt-get install python3-pyaudio portaudio19-dev net-tools -y
RUN apt install nvidia-cuda-toolkit

# Add files.
RUN mkdir whimsicalPractical
COPY . whimsicalPractical/
# RUN python3 -m ensurepip --default-pip -y
RUN pip install -r requirements.txt
#!/bin/sh
# This is a comment!
# Define default command.