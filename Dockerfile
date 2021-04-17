FROM python:3.9

# run with: docker run --rm -it -v $(pwd):/frack frack:local

WORKDIR /frack

RUN pip3 install \
    tabulate \
    openpyxl \
    py3_validate_email \
    hurry.filesize \
    pandas \
    hurry \
    protobuf \
    validate_email \
    google.cloud \
    pyarrow \
    google-cloud-bigquery \
    google-cloud-storage \
    google \
    google.cloud \
    pyorc \
    sqlparse 


VOLUME /frack

ENTRYPOINT [ "bash" ]
