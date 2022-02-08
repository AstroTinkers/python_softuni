def loading(percent):
    loading_bar = ["%" for i in range(0, percent//10)]
    for i in range(percent//10, 10):
        loading_bar.append(".")
    return ''.join(loading_bar)


percentage = int(input())
if '.' in (loading(percentage)):
    print(f"{percentage}% [{loading(percentage)}]")
    print("Still loading...")
else:
    print("100% Complete!")
    print(f"[{loading(percentage)}]")
