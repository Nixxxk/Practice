# Read the initial number of elements in the set
n = int(input())
# Read the elements of the set
s = set(map(int, input().split()))
# Read the number of operations to be performed
N = int(input())

# Perform each operation
for _ in range(N):
    # Read the command and its arguments
    cmd = input().split()
    # Execute the corresponding set method based on the command
    if cmd[0] == "pop":
        s.pop()
    elif cmd[0] == "remove":
        # Use try-except to handle cases where the element is not in the set
        try:
            s.remove(int(cmd[1]))
        except KeyError:
            continue
    elif cmd[0] == "discard":
        # discard does not raise an error if the element is not found, so no try-except needed
        s.discard(int(cmd[1]))

# Print the sum of the elements in the set
print(sum(s))
