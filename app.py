from flask import Flask
from playwright.sync_api import sync_playwright, Playwright

app = Flask(__name__)

@app.route('/')
def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
    
#def hello_world():
#    return 'Welcome Neeraj!'
