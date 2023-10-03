from tkinter import *

def convert_number_to_words(n, country="US"):
    if country == "US":
        return convert_number_to_words_us(n)
    elif country == "India":
        return convert_number_to_words_in(n)
    
    
def convert_number_to_words_us(n):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]
    
    def rec_convert(num, idx):
        if num == 0:
            return ""
        
        words = []
        
        if num > 99:
            words.append(units[num // 100])
            words.append("hundred")
            num %= 100
        
        if num > 10 and num < 20:
            words.append(teens[num-10])
        else:

            if num >= 20 or num == 10:
                words.append(tens[num // 10])
                num %= 10
            
            if num > 0:
                words.append(units[num])
        
        if idx > 0 and any(words):
            words.append(thousands[idx])
        
        return ' '.join(words)
    
    words = []
    idx = 0
    while n > 0:
        segment = n % 1000
        words.append(rec_convert(segment, idx))
        n //= 1000
        idx += 1

    words = [w for w in reversed(words) if w]  
    

    if len(words) > 1:
        return ', '.join(words[:-1]) + ' and ' + words[-1]
    else:
        return words[0]


def convert_number_to_words_in(n):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "lakh", "crore"]


    def rec_convert(num, idx):
        if num == 0:
            return ""
        
        words = []
        
        if num > 99 and (idx == 0 or idx == 1):
            words.append(units[num // 100])
            words.append("hundred")
            num %= 100
        
        if num > 10 and num < 20:
            words.append(teens[num-10])
        else:
            if num >= 20 or num == 10:
                words.append(tens[num // 10])
                num %= 10
            
            if num > 0:
                words.append(units[num])
            
        if idx > 0 and any(words):
            words.append(thousands[idx])
        
        return ' '.join(words)
    
    words = []
    idx = 0
    while n > 0:
        segment_size = 3 if idx == 0 or idx == 1 else 2
        segment = n % (10**segment_size)
        
        words.append(rec_convert(segment, idx))
        n //= (10**segment_size)
        idx += 1

    words = [w for w in reversed(words) if w] 
    
    if len(words) > 1:
        return ', '.join(words[:-1]) + ' and ' + words[-1]
    else:
        return words[0]




def cheque_generator():
    name = name_entry.get()
    date = date_entry.get()
    amount = int(amount_entry.get())
    country = country_var.get()
    amount_in_words = convert_number_to_words(amount, country)
    result.set(f"Pay: {name}\nDate: {date}\nAmount: {amount_in_words}")


root = Tk()


Label(root, text="Name").grid(row=0)
Label(root, text="Date").grid(row=1)
Label(root, text="Amount").grid(row=2)
Label(root, text="Country").grid(row=3)

name_entry = Entry(root)
date_entry = Entry(root)
amount_entry = Entry(root)

name_entry.grid(row=0, column=1)
date_entry.grid(row=1, column=1)
amount_entry.grid(row=2, column=1)


countries = ["US", "India"]
country_var = StringVar(root)
country_var.set(countries[0])  
country_menu = OptionMenu(root, country_var, *countries)
country_menu.grid(row=3, column=1)

Button(root, text='Generate', command=cheque_generator).grid(row=4, column=1, sticky=W, pady=4)

result = StringVar()
Label(root, text="", textvariable=result).grid(row=5)

mainloop()
