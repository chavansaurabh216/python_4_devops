text = "Hi Buddy!!!"

print(f"Length using the inbuilt function is {len(text)}")

length = len(text)

print(f"Length using the inbuilt function is {length}")


# Without using the inbuilt funtion

def string_len(string):
    count = 0
    
    for char in string:
        count += 1
        
    return count

print(f"Length using the manual function is {string_len(text)}")