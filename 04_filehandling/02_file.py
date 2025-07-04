# Read marks from myFile4.txt and print doubled marks

with open('myFile4.txt', 'r') as f_read:
    i = 0
    while True:
        i = i + 1
        line = f_read.readline()
        if not line:
            break

        parts = line.strip().split(",")
        if len(parts) < 3:
            print(f"Skipping invalid line: {line.strip()}")
            continue

        try:
            m1 = int(parts[0])
            m2 = int(parts[1])
            m3 = int(parts[2])
        except ValueError:
            print(f"Skipping non-numeric line: {line.strip()}")
            continue

        print(f"Marks of student {i} in Maths is: {m1 * 2}")
        print(f"Marks of student {i} in English is: {m2 * 2}")
        print(f"Marks of student {i} in SST is: {m3 * 2}")

        print(f"Original line: {line.strip()}")

# Write new lines to myFile5.txt

lines = [
    'This is line 1\n',
    'This is line 2\n',
    'This is line 3\n'
]

with open('myFile5.txt', 'w') as f_write:
    f_write.writelines(lines)

print("New lines written to myFile5.txt.")
