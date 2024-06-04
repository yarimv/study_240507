from bs4 import BeautifulSoup

# Read the HTML content from the file
with open('data.html', 'r') as file:
    html_content = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all elements with the specified class and extract their text
target_elements = soup.find_all('p', class_='text-[0.8125rem] font-medium leading-[1.1375rem] tracking-[-0.02em] text-uniqueGray-50')

# Extract and print the text from each element
if target_elements:
    for index, element in enumerate(target_elements):
        extracted_text = element.text.strip()
        print(f"Extracted text {index + 1}:", extracted_text)
else:
    print("No elements found.")
