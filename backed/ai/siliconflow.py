from openai import OpenAI
# 硅基流动api的调用   https://cloud.siliconflow.cn/account/ak
class SiliconFlow:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://api.siliconflow.cn/v1",
            api_key="sk-xycrdrdoixkekxhrjnrozcmvvcjxkicsboxrvljirczmudvu",
        )

    def get_response(self, query):
        completion = self.client.chat.completions.create(
            model="Qwen/Qwen2.5-7B-Instruct",
            messages=[
                {
                    "role": "user",
                    "content": query
                }
            ],
            stream=False,
            max_tokens=512,
            stop=None,
            temperature=0.7,
            top_p=0.7,
            frequency_penalty=0.5,
            n=1,
            response_format={"type": "text"}
        )
        return completion.choices[0].message.content

# # 实例化 SiliconFlow 类
# silicon_flow_instance = SiliconFlow()

# # 定义查询内容
# query = "你是三亚当地的资深导游,现在需要你简单介绍一下当地有什么值得游玩的地方,倡议大家过来游玩，最好使用几个表情"

# # 调用 get_response 方法获取响应
# response_text = silicon_flow_instance.get_response(query)

# # 打印响应
# print(response_text)