# API Header Spoofing

Learn how HTTP header spoofing works through practical examples. This educational project shows you the techniques used for web scraping and API testing. Tested this Header Spoofing Code on https://wttd.trade/api/items/price-history using the DevTools Console & by executing the **spoof.py**

## ⚙️ What This Does

This code makes HTTP requests while modifying headers to look like they come from a real browser. You'll see how scrapers avoid detection and bypass basic rate limiting and API 403's. The script extracts specific data fields from API responses and displays them in a clean format. It handles both single objects and arrays of data.

## ⚠️ Warning

Only use this code on APIs you own or have explicit permission to access. Unauthorized scraping violates terms of service and may break laws in your jurisdiction. Many websites have legitimate reasons to block scrapers. Respect their bandwidth costs and data protection policies.

## ℹ️ How It Works

- Real browsers send specific HTTP headers with every request. Servers use these headers to identify clients and detect bots. The code rotates through different User Agent strings to appear as different browsers. Each request looks like it comes from a unique visitor.

```javascript
const USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36...',
    // More user agents
];
```

- Bots make requests instantly. Humans take time to click and read. The script adds random delays between 1 and 3 seconds. This mimics natural browsing behavior and helps avoid rate limits.

```javascript
const delay = Math.random() * (delayRange[1] - delayRange[0]) + delayRange[0];
await sleep(delay);
```

- Modern browsers send dozens of headers. The more headers you include, the more realistic your request looks.

```javascript
{
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache'
}
```

- The script extracts specific fields from JSON responses. It looks for id, name, history, and latest_date fields **(based on the API you test it on)** automatically. You get a clean summary instead of raw JSON dumps.

- Browsers restrict what JavaScript can do for security reasons. You cannot modify certain headers through the fetch API.

**Forbidden headers include**
```
* User Agent
* Host
* Origin
* Referer
* Cookie
```

CORS policy blocks most requests to external domains. This protection stops malicious websites from stealing your data. For full control over headers, you need server side code or browser extensions.

## Installation

1. Open your browser's developer console. Press & Hold **Ctrl+Shift+I** or right click anywhere and select Inspect. Click the Console tab.
2. Copy the entire JavaScript code and paste it into the console. Press Enter.

### Node.js Method

1. You need Python installed on your computer. Download it from [Python](https://www.python.org/) if you don't have it.
2. Create a new file called `spoof.py` and paste the code. Replace the fetch API calls with axios or node-fetch.
```bash
pip install -r requirements.txt
python spoof.py
```

## Usage

Replace `WEBSITE HERE` with your target API URL.

### Single Request

```javascript
makeStealthyRequest("https://api.example.com/data")
```

This makes one request with a random delay.

### Single Request Without Delay

```javascript
makeStealthyRequest("https://api.example.com/data", null)
```

This makes an immediate request.

### Multiple Requests

```javascript
scrapeWithRotation("https://api.example.com/data", 3)
```

This makes three requests with different headers and delays between each.

## Output Format

The script displays data in a structured format.

```
--- Item 1 ---
ID: skins-192
Name: Tiger Vine
History: 36 entries
Latest Date: 2025-11-19 20:36:55
```

You also get the full JSON response for reference.

---

You can use these techniques for several legal purposes. Such as testing your own API's to see how your systems respond to different client types. Test rate limiting and security measures. Also, some academic research requires web data. Get written permission first. You can also use it to export your own data from services that don't provide good export tools. Check terms of service first. Security researchers also use these techniques to find vulnerabilities. Only participate in authorized programs.

## Common Issues

1. Browsers block cross origin requests by default. The API needs to allow your domain through CORS headers. You can't bypass this in browser JavaScript. Use a proxy server or server side code instead.
2. **403 Forbidden Access**, the server detected and blocked your request. Try different headers or slower request rates. Some sites use advanced bot detection that checks JavaScript execution and mouse movement.
3. **429 Too Many Requests**, you hit a rate limit. Increase delays between requests or reduce the number of requests. Respect these limits. They protect server resources.
4. The API might require authentication headers or cookies. Check the network tab in developer tools to see what a browser sends.

## Disclaimer

This project exists purely for educational purposes. The author take no responsibility for misuse. You take full responsibility for your actions. Unauthorized access to computer systems is illegal in most jurisdictions.
