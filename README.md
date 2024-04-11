# WebWorm
Data Visualization | Data Processing | Data Manipulation | Python | Matplotlib | Numpy | Graphs | DFS | File Handling

![image](https://github.com/Shivani0230/WebWorm/assets/166192409/c9bf5127-2cc7-46df-aebc-b9458164bfce)

## Project Description
Web Worm project leverages Python programming along with data visualization libraries to analyze and visualize subdomains' relationships within a domain. By fetching subdomains using Subfinder and creating a graph representation, this project aims to provide insights into the structure and connectivity of subdomains. Additionally, it checks the status of each subdomain URL, adding another layer of analysis to the visualization.

## Prerequisites
- Python 3.x
- NetworkX
- Matplotlib
- Requests

## Installation
- Clone the repository: git clone https://github.com/Shivani0230/WebWorm.git
- Install dependencies: pip install -r requirements.txt

## Usage
- Run the script: python subdomain_graph.py
- Enter the domain name when prompted.
- The script will fetch subdomains using Subfinder and visualize them in a graph.

## Example
- python subdomain_graph.py
- Enter domain: example.com

## Output
The script will save the subdomains to subdomains.txt and the not-working subdomains to notworking.txt. It will also display a graph of the subdomains with green nodes for working URLs and red nodes for not-working URLs.

