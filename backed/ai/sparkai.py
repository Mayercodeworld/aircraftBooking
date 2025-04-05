from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage

SPARKAI_URL = 'wss://spark-api.xf-yun.com/v1.1/chat'
SPARKAI_APP_ID = '38f43656'
SPARKAI_API_SECRET = 'ZTBhODUwZDk5MjQwYjhmMzZiYWQyNjFm'
SPARKAI_API_KEY = '2ec3725c7f3f66cb54b1417391ad0141'
SPARKAI_DOMAIN = 'lite'

class Spark:
    def __init__(self):
        self.spark = ChatSparkLLM(
            spark_api_url=SPARKAI_URL,
            spark_app_id=SPARKAI_APP_ID,
            spark_api_key=SPARKAI_API_KEY,
            spark_api_secret=SPARKAI_API_SECRET,
            spark_llm_domain=SPARKAI_DOMAIN,
            streaming=False,
        )

    # 返回指定数据
    #############################
    # 后继可以查看a打印的数据格式，返回其他数据
    ############################
    # 返回指定数据
    def spark_response(self, query):
        messages = [ChatMessage(
            role="user",
            content=query
        )]
        handler = ChunkPrintHandler()
        a = self.spark.generate([messages], callbacks=[handler])
        
        # 提取文本内容
        text_content = a.generations[0][0].text
        
        # 转换为 Markdown 格式
        markdown_content = self.convert_to_markdown(text_content)
        
        print(markdown_content)
        return markdown_content

    def convert_to_markdown(self, text):
        # 将段落转换为 Markdown 格式
        paragraphs = text.split('\n\n')
        markdown_text = '\n\n'.join(f'**{p.split("：")[0]}：** {p.split("：")[1]}' if '：' in p else p for p in paragraphs)
        
        # 将列表项转换为 Markdown 格式
        markdown_text = markdown_text.replace('1.', '-')
        markdown_text = markdown_text.replace('2.', '-')
        markdown_text = markdown_text.replace('3.', '-')
        markdown_text = markdown_text.replace('4.', '-')
        markdown_text = markdown_text.replace('5.', '-')
        markdown_text = markdown_text.replace('6.', '-')
        markdown_text = markdown_text.replace('7.', '-')
        
        return markdown_text

if __name__ == '__main__':
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    messages = [ChatMessage(
        role="user",
        content='你好呀'
    )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    print(a)