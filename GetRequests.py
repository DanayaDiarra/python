import requests  
from bs4 import BeautifulSoup  

url = 'https://gsom.spbu.ru/en/'  

resp = requests.get(url)
if resp.status_code == 200:  

    soup = BeautifulSoup(resp.content, "html.parser")  
    # List to hold PNG links  
    png_links = []

    # Finding all <img> tags and check their 'src' attribute for PNG links
    for img in soup.find_all("img", src=True):
        src = img['src']  
# Checking if the 'src' ends with ".png"
        if src.lower().endswith(".png"):  
# Append the found PNG link   
            png_links.append(src)

    # Prepend base URL if needed (handling relative links)
    base_url = "https://gsom.spbu.ru"  
    full_png_links = []  

    for link in png_links:  
        # If the link is relative, prepend the base URL  
        if link.lower().endswith(".png"):  
            full_png_links.append(base_url + link)
    count_png=len(full_png_links)

    # Print the extracted PNG links 
    print("Total_png_links: ", count_png)
    print("Extracted PNG Links:")  
    for link in full_png_links:  
        print(link) 