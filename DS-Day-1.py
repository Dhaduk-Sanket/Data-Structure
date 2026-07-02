#1. Amazon Fulfillment Centre

belt = ["Phone", "Laptop", "Watch", "Camera",
        "Mouse", "Keyboard", "Speaker", "Tablet"]

def check_slot(index):
    if 0 <= index < 8:
        print("Product at slot", index, ":", belt[index])
    else:
        print("Invalid slot")

def find_product(product):
    if product in belt:
        print(product, "found at slot", belt.index(product))
    else:
        print("Product not found")

def update_slot(index, product):
    if 0 <= index < 8:
        belt[index] = product
        print("Slot updated")
    else:
        print("Invalid slot")

def is_full():
    if len(belt) == 8:
        print("Belt is full")
    else:
        print("Belt is not full")

# Output
# check_slot(2)
# find_product("Camera")
# update_slot(1, "Printer")
# check_slot(1)
# is_full()



#2. Toll Plaza Simulation (Circular Queue)

size = 5
queue = [None] * size
front = -1
rear = -1

def enqueue(vehicle):
    global front, rear

    if (rear + 1) % size == front:
        print("Toll Plaza Full")
        return

    if front == -1:
        front = 0

    rear = (rear + 1) % size
    queue[rear] = vehicle
    print(vehicle, "entered")

def dequeue():
    global front, rear

    if front == -1:
        print("Toll Plaza Empty")
        return

    print(queue[front], "left")

    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % size

def display():
    if front == -1:
        print("No vehicles")
        return

    i = front
    print("Vehicles:", end=" ")
    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % size
    print()

# Output
# enqueue("Car")
# enqueue("Bus")
# enqueue("Bike")
# display()

# dequeue()
# display()

# enqueue("Truck")
# enqueue("Van")
# display()


#3. GPS Navigation System (Backtracking)

back_stack = []
forward_stack = []
current = None

def visit(place):
    global current

    if current is not None:
        back_stack.append(current)

    current = place
    forward_stack.clear()
    print("Current:", current)

def back():
    global current

    if len(back_stack) == 0:
        print("No previous place")
        return

    forward_stack.append(current)
    current = back_stack.pop()
    print("Current:", current)

def forward():
    global current

    if len(forward_stack) == 0:
        print("No forward place")
        return

    back_stack.append(current)
    current = forward_stack.pop()
    print("Current:", current)

# Output
# visit("Home")
# visit("Park")
# visit("Temple")

# back()
# back()

# forward()

# visit("Mall")