FROM python:3.13
WORKDIR /Structure_enquiry
COPY . .
RUN pip install --no-cache-dir pytest
# Run tests at build time (CI)
RUN pytest
# FIXED entrypoint (never replaced)
ENTRYPOINT ["python", "driving_licence_app.py"]