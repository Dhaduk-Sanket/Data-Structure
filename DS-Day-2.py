#1. The Spam Detector (Linear Search)

blacklist = ["abc111", "fake999", "spam123", "test456"]

sender = input("Enter sender ID: ")

found = False

for i in blacklist:
    if i == sender:
        found = True
        break

if found:
    print("Spam Sender Found!")
else:
    print("Safe Sender")


#2. E-Commerce Price Filter (Binary Search - Lower Bound)

prices = [22000, 29000, 39000, 55000, 65000, 80000]

target = int(input("Enter minimum price: "))

low = 0
high = len(prices) - 1
answer = -1

while low <= high:
    mid = (low + high) // 2

    if prices[mid] >= target:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

if answer != -1:
    print("First product >= target is", prices[answer], "at index", answer)
else:
    print("No product found")


#3. IRCTC Waitlist Merger (Merge Step)

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

i = 0
j = 0
merged = []

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

while i < len(list1):
    merged.append(list1[i])
    i += 1

while j < len(list2):
    merged.append(list2[j])
    j += 1

print("Merged List:", merged)
