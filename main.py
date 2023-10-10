n = int(input("Enter your number: "))
if n >= 0:
    def countdown(n):
        if n == 0:
            print('Blastoff!')
        else:
            while n >= 0:
                print(n)
                if n == 0:
                    print('Blastoff!')
                    break
                n -= 1
    countdown(n)

else:
    def countup(n):
        if n == 0:
            print('Blastoff!')
        else:
            while n <= 0:
                print(n)
                if n == 0:
                    print('Blastoff!')
                    break
                n += 1
    countup(n)

