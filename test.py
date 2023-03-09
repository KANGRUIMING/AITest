import os
import openai

openai.api_key = 'YOUR API KEY'

#create system role 建立ai的身份，从而得到更准确回答
messages = [
    #例子："You are a college interviewer, ask a question after each response"
    {"role": "system", "content": "你是一个专业科学家，专业写作论文"}    
    ]


#持续对话用while true
while True:
    
    content = input("User: ")
    messages.append({"role": "user", "content": content})
    
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages= messages 
    )
    
    chat_response = completion.choices[0].message.content
    
    print(f'AI: {chat_response}')
    #assistant role储存所有的回复，从而可以根据聊天记录回复
    messages.append({"role": "assistant", "content": chat_response})

