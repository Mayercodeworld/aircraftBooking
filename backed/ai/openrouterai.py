from openai import OpenAI
# openrouter api的调用
class Qwq:
    def __init__(self):
      self.client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
      )
    def qwq_response(self, query):
      completion = self.client.chat.completions.create(
        extra_headers={
          "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
          "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
        },
        extra_body={},
        model="qwen/qwq-32b:free",
        messages=[
          {
            "role": "user",
            "content": query
          }
        ]
      )
      return completion.choices[0].message.content
    # for chunk in completion:
    #         delta = chunk.choices[0].delta
    #         if 'content' in delta:
    #             yield delta['content']