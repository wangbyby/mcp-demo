# mcp-demo

本项目是mcp的简单例子。
cloned from: https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/clients/simple-chatbot/mcp_simple_chatbot/main.py

运行分为如下几步
1. python环境配置
2. 更改配置`.env`
3. 运行`python main.py`


## 1. python环境配置

使用uv创建python虚拟环境。
windows平台下：（linux/mac同理，改改路径名就行）
```shell
uv init mcp-demo
cd mcp-demo

# Create virtual environment and activate it
uv venv
.venv\Scripts\activate

# Install dependencies
uv add mcp[cli] httpx    
```
## 2. 更改配置`.env`
这里我们用qwen作为实例（免费）。
需要自己去阿里云申请API_KEY，然后填入`.env`文件中，一般是叫`sk-xxx`.
URL就是阿里云的API地址。
model就选个常见的。
```txt
LLM_API_KEY=
URL=https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions
model=qwen-plus
```


## 3. 运行`.\.venv\Scripts\python.exe .\main.py`

>当然了是windows平台的运行命令

结果实例
```txt
You: using mcp to add 1 and 2
2025-04-09 21:37:14,781 - INFO - 
 the message is: [{'role': 'system', 'content': 'You are a helpful assistant with access to these tools:\n\n\nTool: add\nDescription: \n    计算两个整数的和。\n\n    Args:\n        a: 第一个整数。\n        b: 第二个整数。\n\n    Returns:\n        两个整数的和。\n    \nArguments:\n- a: No description (required)\n- b: No description (required)\n\nChoose the appropriate tool based on the user\'s question. If no tool is needed, reply directly.\n\nIMPORTANT: When you need to use a tool, you must ONLY respond with the exact JSON object format below, nothing else:\n{\n    "tool": "tool-name",\n    "arguments": {\n        "argument-name": "value"\n    }\n}\n\nAfter receiving a tool\'s response:\n1. Transform the raw data into a natural, conversational response\n2. Keep responses concise but informative\n3. Focus on the most relevant information\n4. Use appropriate context from the user\'s question\n5. Avoid simply repeating the raw data\n\nPlease use only the tools that are explicitly defined above.'}, {'role': 'user', 'content': 'using mcp to add 1 and 2'}]
2025-04-09 21:37:15,303 - INFO - Sending request to https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions
2025-04-09 21:37:16,316 - INFO - HTTP Request: POST https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions "HTTP/1.1 200 OK"
2025-04-09 21:37:16,321 - INFO -
Assistant: {
    "tool": "add",
    "arguments": {
        "a": "1",
        "b": "2"
    }
}
2025-04-09 21:37:16,321 - INFO - Executing tool: add
2025-04-09 21:37:16,321 - INFO - With arguments: {'a': '1', 'b': '2'}
2025-04-09 21:37:16,329 - INFO - Executing add...
2025-04-09 21:37:16,811 - INFO - Sending request to https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions
2025-04-09 21:37:17,915 - INFO - HTTP Request: POST https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions "HTTP/1.1 200 OK"
2025-04-09 21:37:17,916 - INFO -
Final response: The sum of 1 and 2 is 3.

```

1. You：用户输入
2. 通过system角色描述mcp接口：
```txt
tools:\n\n\nTool: add\nDescription: \n    计算两个整数的和。\n\n    Args:\n        a: 第一个整数。\n        b: 第二个整数。\n\n    Returns:\n        两个整数的和。\n    \nArguments:\n- a: No description (required)\n- b: No description (required)\n\nChoose the appropriate tool based on the user\'s question.
```
 将用户输入内容附加在user角色里
3. 第一次向api发起请求，api返回了mcp调用描述
```txt
Assistant: {
    "tool": "add",
    "arguments": {
        "a": "1",
        "b": "2"
    } 
}
```

4. 执行mcp调用, 调用add函数
结果如下：
```txt
2025-04-09 21:48:35,594 - INFO - 
 After call mcp tools: Tool execution result: meta=None content=[TextContent(type='text', text='3', annotations=None)] isError=False
```

5. 附加上mcp的结果再次向api发起请求，并反正最终结果

```txt
2025-04-09 21:48:36,117 - INFO - Sending request to https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions

Final response: The sum of 1 and 2 is 3.
```

综上所述，mcp是个很强大的工具。其实也是api调用，但重要的是格式！
不足：有点费钱。。。
