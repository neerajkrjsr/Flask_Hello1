from flask import Flask
import asyncio
from playwright.async_api import async_playwright, Playwright

app = Flask(__name__)

@app.route('/')
async def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = await chromium.launch()
    page = await browser.new_page()
    await page.goto("https://example.com")
    await page.wait_for_timeout(5000)
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
    
#def hello_world():
#    return 'Welcome Neeraj!'
