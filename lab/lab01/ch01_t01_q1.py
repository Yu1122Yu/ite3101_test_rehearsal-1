def main():
    while True:
        try:
            num = int(input("Type an integer:"))
            break
        except ValueError:
            print('Please enter an inreger.')
        if num % 10== 0 and num % 3 != 0:
           print(f{num} is divisiable by 10 and not divisible by 3.)
                 
   
   
 if __name__ == "__main__":
    # execute only if run as a script
    main()
