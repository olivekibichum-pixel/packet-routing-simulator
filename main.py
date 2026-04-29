
def find_path(routing_table, source, destination):
    path = [source]
    
    while source != destination:
        if source not in routing_table:
            return None
        source = routing_table[source]
        path.append(source)
        
        if len(path) > 10:
            return None
    
    return path


routing_table = {
    "A": "B",
    "B": "C",
    "C": "D",
    "D": "E"
}

source = input("Enter source: ")
destination = input("Enter destination: ")

path = find_path(routing_table, source, destination)

if path:
    print("Path:", " -> ".join(path))
else:
    print("No valid route found.")
