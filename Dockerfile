#映像檔:使用的語言
FROM python:3.10-alpine
#設置工作目錄
WORKDIR /app
#複製檔案至Docker內
COPY . .
#執行輸入的指令(cmd,python....)
#這裡執行BeautifulSoup request
RUN pip install bs4
#mkdir:建立目錄，-p:以路徑名格式指定目錄名，如果路徑名中的目錄不存在，便會新建一個。
#/app/data : 跟目錄下的data
RUN mkdir -p /app/data
#在運行中執行 phthon3，crawler.py
CMD ["python3", "crawler.py"]
#port 3000
EXPOSE 3000