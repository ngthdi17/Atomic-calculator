mass_proton_amu = 1.00727
mass_neutron_amu = 1.00867
mass_electron_amu = 5.485*(10**-4)
ab_mass = 0
negative = ['no','n','not','enough','stop','nah','nope']


#Intro:
print(f'WELCOME TO ATOMIC ANALYZER')
print(f"""Options:
        1. Calculate average atomic mass
        2. Calculate binding energy
        3. Calculate the mass using the mass of the subatomic particles
        4. Exit"""
)
print()
option = str(input("What do you want to do? "))

#1.
if option in ['1']:
    while True:
        number_isotopes = int(input("How many isotopes are there in this element? "))
        num_isotopes = list(range(1, number_isotopes + 1))
        
        for values in num_isotopes:
            if values == 1:
                isotopes = list(input("What is the isotope name? "))
                mass_number = int(input(f"What is the first {isotopes[0].upper()}{isotopes[1].lower()}'s mass number? "))
                atomic_mass = float(input(f"What {isotopes[0].upper()}{isotopes[1].lower()}-{mass_number}'s atomic mass? (in amu) "))
                abundance = float(input(f"What is {isotopes[0].upper()}{isotopes[1].lower()}-{mass_number}'s abundance percentage? (in %) "))
                abundance_mass = (abundance/100)*atomic_mass
                ab_mass = ab_mass + abundance_mass
                print(f"The first isotope is {isotopes[0].upper()}{isotopes[1].lower()}-{mass_number} and its mass is {abundance_mass}")
            elif values > 1:
                mass_number = int(input(f"What is the next {isotopes[0].upper()}{isotopes[1].lower()} mass number? "))
                atomic_mass = float(input(f"What is {isotopes[0].upper()}{isotopes[1].lower()}-{mass_number}'s atomic mass? (in amu) "))
                abundance = float(input(f"What is {isotopes[0].upper()}{isotopes[1].lower()}-{mass_number}'s abundance percentage? (in %) "))
                abundance_mass = (abundance/100)*atomic_mass
                ab_mass = ab_mass + abundance_mass
                print(f"The next isotope is {isotopes[0].upper()}{isotopes[1].lower()}-{mass_number} and its mass is {abundance_mass}")
        print(f"The average atomic mass of {isotopes[0].upper()}{isotopes[1].lower()} is {ab_mass} amu ( or {round(ab_mass, 2)} amu)")
        print()
        more = input("Are there any other element you want to calculate the avarage atomic mass? ")
        if more in negative:
            break











#Wrong theory
#2.


if option in ['2','two']:
   print("""---CALCULATE BINDING ENERGY---
         1. Enter the isotope you want to calculate the bonding energy.
         2. Find the average atomic mass
         3. Calculate the Δ mass ( Δmass = average atomic mass (calculated) - atomic mass)
         4. Convert the mass in amu to kg (Δmass amu * (1.6605*(10^-27)kg/1amu) )
         5. Calculate the binding energy (in Joules (J)) (E=mc^2) 
         """)
   print()
   print(f"1. Enter the isotope you want to calculate the bonding energy. ")
   while True:
     isotopes = input("What is an element symbol?  ")
     if isotopes == "":
       print("You didn't enter an element symbol yet")
       continue
     else:
       labeled = isotopes[0].upper() + isotopes[1:].lower()
       break
   print()
   print(f"2. Find {labeled}'s average atomic mass")
   print()
   shortcut = input("Do you want to calculate the average atomic mass or you want to type? (cal - 1/type - 2)").lower()
   if shortcut == 'cal' or shortcut == '1':
      while True:
        number_isotopes = int(input("How many isotopes are there in this element? "))
        num_isotopes = list(range(1, number_isotopes + 1))
        ab_mass = 0
        for values in num_isotopes:
            if values == 1:
                mass_number = int(input(f"What is the first {labeled}'s mass number? "))
                questions = [f"What {labeled}-{mass_number}'s atomic mass? (in amu) ", f"What is {labeled}-{mass_number}'s abundance percentage? (in %) " ]
                answers = []
                i = 0
                while i < len(questions):
                    answer = float(input(questions[i]))
                    confirm = input(f"Confirm {answer}? (yes/no) ").lower()
                    if confirm in positive:
                       answers.append(answer)
                       i = i + 1
                    elif confirm in negative:
                       continue #Don't change i, so it repeat the question again!
                    else:
                      continue #If they type something else=> no
                abundance_mass = answers[0]*(answers[1]/100)
                ab_mass = ab_mass + abundance_mass
                print(f"The first isotope is {labeled}-{mass_number} and its mass is {abundance_mass} amu ")
            elif values > 1:
                mass_number = int(input(f"What is the next {labeled}'s mass number? "))
                questions = [f"What {labeled}-{mass_number}'s atomic mass? (in amu) ", f"What is {labeled}-{mass_number}'s abundance percentage? (in %) " ]
                answers = []
                i = 0
                while i < len(questions):
                    answer = float(input(questions[i]))
                    confirm = input(f"Confirm {answer}? (yes/no) ").lower()
    
                    if confirm in positive:
                       answers.append(answer)
                       i = i + 1
                    elif confirm in negative:
                       continue #Don't change i, so it repeat the question again!
                    else:
                      continue #If they type something else=> no
                abundance_mass = answers[0]*(answers[1]/100)
                ab_mass = ab_mass + abundance_mass
                print(f"The next isotope is {labeled}-{mass_number} and its mass is {abundance_mass} amu ")
        print(f"The average atomic mass of {labeled} is {ab_mass} amu ( or {round(ab_mass, 2)} amu)")
        break
   elif shortcut == 'type' or shortcut == '2':
     while True:
        type = float(input(f"What is the average atomic mass of {labeled}? "))
        confirm = input(f"Confirm {type}? (yes/no) ").lower()
        if confirm in positive:
           break
   print()
   print(f"3. Calculating the Δ mass")
   bond_iso = int(input(f"What isotope of {labeled} do you want to calculate the bonding energy? (Enter atomic mass, like if it's 'Bo', enter 11 or 10)  "))
   bond_labeled = f"{labeled}-{bond_iso}"
   atomic_mass = float(input(f"What is the atomic mass of {bond_labeled} : "))
   print()
   try:
      ab_mass   # Python checks if this variable exists
   except NameError: #If my_var is not defined, Python throws an error called NameError.
      delta_mass = type - atomic_mass #The except part catches that error instead of crashing your code.
   else:
      delta_mass =round(ab_mass - atomic_mass, 3) 
   print(f"Δmass = {delta_mass} amu ")
   print()
   print(f"4. Convert the mass in amu to kg (Δmass amu * (1.6605*(10^-27)kg/1amu) ) ")
   delta_mass_kg = delta_mass * (1.6605*(10**-27))
   sci_dmk = f"{delta_mass_kg:.2e}" # '1.23e+05'
   base_dmk , exp_dmk = sci_dmk.split("e") # ['1.23', '+05'] \
   exp_dmk = int(exp_dmk) # convert '+05' → 5
   formatted_dmk = f"{base_dmk} x 10^{exp_dmk}"
   print(f"Δmass in kg is: {formatted_dmk} kg")
   print()
   print(f"5. Calculate the binding energy (in Joules (J)) (E=mc^2) ")
   m = delta_mass_kg
   e = m*(c**2)
   sci_e = f"{e:.2e}"
   base_e, exp_e = sci_e.split("e")
   exp_e = int(exp_e)
   formatted_e = f"{base_e} x 10^{exp_e}"
   print(f"The binding energy for {bond_labeled} is {formatted_e} J")





   
   
     


   

        