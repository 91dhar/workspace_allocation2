# Define the number of people in each project
project_sizes = {
    'Project A': 110,
    'Project B': 70,
    'Project C': 30,
    'Project D': 40,
    'Project E': 100,
}

# Define the number of seats in each workspace
workspace_seats = {
    'Workspace A': 80,
    'Workspace B': 17,
    'Workspace C': 22,
    'Workspace D': 77,
    'Workspace E': 46,
    'Workspace F': 25,
    'Workspace G': 25,
    'Workspace H': 39,
    'Workspace I': 19,
}

# Initialize a dictionary to keep track of allocated seats for each workspace
allocated_seats = {workspace: [] for workspace in workspace_seats}

# Sort projects by size in descending order
sorted_projects = sorted(project_sizes.items(), key=lambda x: x[1], reverse=True)

# Allocate seats project by project while minimizing splits
for project, size in sorted_projects:
    allocated = False
    # Try to allocate the entire project to a single workspace
    for workspace, seats in sorted(workspace_seats.items(), key=lambda x: -x[1]):
        if seats >= size:
            allocated_seats[workspace].append((project, size))
            workspace_seats[workspace] -= size
            allocated = True
            break
    # If the entire project cannot fit in one workspace, spill over minimally
    if not allocated:
        for workspace, seats in sorted(workspace_seats.items(), key=lambda x: -x[1]):
            if seats > 0:
                allocation = min(seats, size)
                allocated_seats[workspace].append((project, allocation))
                workspace_seats[workspace] -= allocation
                size -= allocation
                if size == 0:
                    break

# Print the allocation
for workspace, projects in allocated_seats.items():
    total_size = sum(size for _, size in projects)
    project_names = ', '.join(f'{project} ({size})' for project, size in projects)
    print(f'{workspace}: {total_size} seats allocated to {project_names}')
