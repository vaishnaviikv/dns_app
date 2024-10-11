FROM python:3.5

RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN groupadd -g 799 vv2342 && \
    useradd -r -u 999 -g vv2342 vv2342

# Set up a working folder and install the pre-reqs
WORKDIR /app

RUN pip install Flask

RUN pip install requests

USER asg8830

COPY --chown=vv2342:vv2342 . .

CMD [ "python", "./US.py" ]
