FROM python:3.11-slim 
WORKDIR /app 
COPY main.py utils.py memory.py scheduling.py ./ 
RUN mkdir -p data 
COPY data/*.csv data/ 
RUN chmod +x main.py 
CMD ["python", "main.py"] 
# Mini OS Simulator - FCFS + FIFO 
# Ready for demo presentasi 
