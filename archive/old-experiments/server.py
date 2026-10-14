from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mymcp = FastMCP('addnum')

@mymcp.tool()
async def add_two_num(a:int,b:int)->int:
    """Function to add two numbers.
    """
    return a + b

@mymcp.tool()
async def multiply_two_num(a:int,b:int)->int:
    """Function to multiple two numbers.
    """
    return a * b


if __name__=="__main__":
    mymcp.run(transport='stdio')