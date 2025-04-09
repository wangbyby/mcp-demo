from mcp.server.fastmcp import FastMCP

# 创建 FastMCP 服务端实例，命名为 "add-server"
mcp = FastMCP("add-server")

# 使用 @mcp.tool() 装饰器定义一个名为 "add" 的工具
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    计算两个整数的和。

    Args:
        a: 第一个整数。
        b: 第二个整数。

    Returns:
        两个整数的和。
    """
    return a + b

# 主程序入口
if __name__ == "__main__":
    # 启动服务端，使用 stdio 作为传输方式
    mcp.run(transport='stdio')