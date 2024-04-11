import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict
import subprocess
import requests


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()

        self.DFSUtil(v, visited)

    def create_networkx_graph(self):
        G = nx.DiGraph()
        for node in self.graph:
            for neighbour in self.graph[node]:
                G.add_edge(node, neighbour)
        return G

    def check_url(self, url):
        try:
            response = requests.get("https://" + url,timeout=5)
            # print(f"{url}: {response.status_code}")
            return response.status_code == 200
        except requests.exceptions.RequestException as e:
            # print(f"Error checking URL {url}: {e}")
            with open("notworking.txt", "a") as f:
                f.write(url)
                f.write("\n")
            print("Not Working Subdomains saved to not working.txt")
            return False

def create_graph_from_subdomains(subdomain_file, sub1):
    g = Graph()
    try:
        g.addEdge(sub1, sub1)  
        with open(subdomain_file, "r") as f:
            for line in f:
                subdomain = line.strip()
                
                g.addEdge(sub1, subdomain)  
    except Exception as e:
        print(f"An error occurred: {e}")

    return g


def run_subfinder(subdomain):
    try:
        cmd = f"./subfinder -d {subdomain}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            with open("subdomains.txt", "w") as f:
                f.write(result.stdout)
            print("Subdomains saved to subdomains.txt")
        else:
            print("Subfinder command failed. Error output:")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")


def visualize_graph(graph):
    G = graph.create_networkx_graph()

    pos = nx.spring_layout(G, seed=42)  
    plt.figure(figsize=(12, 8))

    node_colors = []
    for node in G.nodes():
        if graph.check_url(node):
            node_colors.append("green")  
        else:
            node_colors.append("red")  

    nx.draw(G, pos, with_labels=True, node_size=1000, node_color=node_colors, font_size=10, font_weight="bold", connectionstyle="arc3,rad=0.1")
    plt.title("Connected Graph of Subdomains")
    plt.show()

if __name__ == "__main__":
    subdomain = input("Enter domain: ")
    run_subfinder(subdomain)
    subdomain_file = "subdomains.txt"
    g = create_graph_from_subdomains(subdomain_file, subdomain)

    print("Following is Depth First Traversal : ")

    g.DFS(subdomain)  
    
    visualize_graph(g)
