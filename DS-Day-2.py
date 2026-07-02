#1. The Spam Detector (Linear Search)

spam_list = [113, 288, 350, 400, 425]

def linear_search(sender_id):
    for i in range(len(spam_list)):
        if spam_list[i] == sender_id:
            return i
    return -1

sender = 350

result = linear_search(sender)

if result != -1:
    print("Spam sender found at position:", result)
else:
    print("Sender is not in spam list")


#2. E-Commerce Price Filter (Binary Search - Lower Bound)

prices = [22000, 29000, 39000, 55000, 65000, 80000]

def lower_bound(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

target = 55000

index = lower_bound(prices, target)

if index < len(prices):
    print("First product price >=", target, "is", prices[index])
else:
    print("No product found")


#3. IRCTC Waitlist Merger (Merge Step)

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

def merge_lists(a, b):
    result = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    while i < len(a):
        result.append(a[i])
        i += 1

    while j < len(b):
        result.append(b[j])
        j += 1

    return result

final_waitlist = merge_lists(list1, list2)

print("Merged Waitlist:", final_waitlist)