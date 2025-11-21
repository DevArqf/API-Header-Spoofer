import requests
import json
import random
import time

url = "WEBSITE HERE"

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
]

def get_spoofed_headers():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        
        'Connection': 'keep-alive',
        
        'Referer': 'WEBSITE HERE',
        
        'DNT': '1',
        
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        
        'Upgrade-Insecure-Requests': '1',
        
        # Optional: Spoof X-Forwarded-For to appear from different IP
        # (Note: Many servers ignore this or validate it)
        # 'X-Forwarded-For': '8.8.8.8',
        
        # Optional: Custom origin header
        # 'Origin': 'WEBSITE HERE'
    }

def make_stealthy_request(url, delay_range=(1, 3)):
    """
    Make a request with spoofed headers and realistic delays
    
    Args:
        url: Target URL
        delay_range: Tuple of (min, max) seconds to wait between requests
    """
    try:
        if delay_range:
            delay = random.uniform(delay_range[0], delay_range[1])
            print(f"Waiting {delay:.2f} seconds (mimicking human behavior)...")
            time.sleep(delay)
        
        print("Fetching data with spoofed headers...")
        
        headers = get_spoofed_headers()
        print(f"Using User-Agent: {headers['User-Agent'][:50]}...")
        
        response = requests.get(url, headers=headers, timeout=10)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("Success! Data received:")
            print("-" * 50)
            
            try:
                data = response.json()
                print(json.dumps(data, indent=2))
                return data
            except json.JSONDecodeError:
                print("Response is not JSON. Raw content:")
                print(response.text[:500])
                return response.text
        else:
            print(f"Error: Received status code {response.status_code}")
            print(f"Response: {response.text[:200]}")
            return None
            
    except requests.exceptions.Timeout:
        print("Error: Request timed out")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    return None

def scrape_with_rotation(url, num_requests=3):
    """
    Make multiple requests with header rotation and delays
    """
    print("=" * 60)
    print("EDUCATIONAL HEADER SPOOFING DEMONSTRATION")
    print("Only use on APIs/sites you own or have permission to access!")
    print("=" * 60)
    print()
    
    results = []
    for i in range(num_requests):
        print(f"\n--- Request {i+1}/{num_requests} ---")
        result = make_stealthy_request(url)
        if result:
            results.append(result)
    
    print(f"\n\nTotal successful requests: {len(results)}/{num_requests}")
    return results

if __name__ == "__main__":
    make_stealthy_request(url, delay_range=None)
    
    # Uncomment to test multiple requests with rotation:
    # scrape_with_rotation(url, num_requests=3)