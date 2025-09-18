import random

#สุ่มเลขระหว่าง 0 - 9
test_random = random.randint(1, 20)

print("--เกมทายตัวเลข มาเดาใจตอมพิวเตอร์กันเถอะ --")
print("--ทายเลขจำนวนเต็มตั้งเเต่ 1 - 20 --")
print("--มีโอกาส 6 ครั้ง --")

for i in range(6):

    #รับค่าการทายเลขจากผู้ใช้
    print(f"ความพยายามครั้งที่ {i+1}")
    guess_number = int(input("What if your guess number (1-20)?: "))

# condition ==> if-elif-else
    if test_random == guess_number:
        print("ยูเก่งมาก มั่วถูกตั้งเเต่ครั้งเเรกเลย เทพจริงๆ ")
        break
    elif guess_number < test_random:
        print("ผิดจ้า น้อยไปเนอะ")

    elif guess_number > test_random:
        print("ผิดจ้า มากไปหน่อย") 
