mass_proton_amu = 1.00727
mass_neutron_amu = 1.00867
mass_electron_amu = 5.485*(10**-4)
formatted_mea = f"5.485*(10^-4)"
mass_electron_kg = 9.11*(10**-31)
formatted_mek = f"9.11*(10^-31) "
mass_neutron_kg = 1.675*(10**-27)
formatted_mnk = f"1.675*(10^-27)"
mass_proton_kg = 1.673*(10**-27)
formatted_mpk = f"1.673*(10^-27)"
negative = ['no', 'n', 'not', 'enough', 'stop', 'nah', 'nope']
positive = ['yes', 'ye', 'y', 'yep', 'sure', 'correct', 'yeah', 'yea']
c = 2.998*(10**8)  # Speed of light
while True:
    # Intro:
    print(f'WELCOME TO ATOMIC ANALYZER')
    print(f"""Options:
        1. Calculate average atomic mass
        2. Calculate the mass using the mass of the subatomic particles
        3. Calculate the binding energy
        4. Exit"""
          )
    print()
    print("-- PLEASE ALWAYS READ THE INSTRUCTION CAREFULLY!-- ")
    option = str(input("What do you want to do? ")).lower()
    # 1.
    if option in ['1', 'one']:
        print("""---CALCULATING AVERAGE ATOMIC MASS---
        1. Enter an element ( SYMBOL )
        2. Enter the first isotopes mass number
        3. Enter the first isotopes atomic mass
        4. Enter the first isotopes abundance
        5. Do the same for the 2nd, 3rd, 4th,... isotopes
        6. Get the average atomic mass
        """)
        print()
        while True:
            isotopes = input("Enter an element symbol? ")
            if not isotopes:
                print("You didn't enter an element symbol yet")
                continue

            labeled = isotopes[0].upper() + isotopes[1:].lower()
            number_isotopes = int(
                input("How many isotopes are there in this element? "))
            num_isotopes = list(range(1, number_isotopes + 1))
            ab_mass = 0
            for values in num_isotopes:
                if values == 1:
                    mass_number = int(
                        input(f"What is the first {labeled}'s isotope mass number? "))
                    questions = [
                        f"What {labeled}-{mass_number}'s atomic mass? (in amu) ", f"What is {labeled}-{mass_number}'s abundance percentage? (in %) "]
                    answers = []
                    i = 0
                    while i < len(questions):
                        answer = float(input(questions[i]))
                        confirm = input(f"Confirm {answer}? (yes/no) ").lower()
                        if confirm in positive:
                            answers.append(answer)
                            i = i + 1
                        elif confirm in negative:
                            continue  # Don't change i, so it repeat the question again!
                        else:
                            continue  # If they type something else=> no
                    abundance_mass = answers[0] * (answers[1] / 100)
                    ab_mass = ab_mass + abundance_mass
                    print(
                        f"The first isotope is {labeled}-{mass_number} and its mass is {abundance_mass} amu ")
                elif values > 1:
                    mass_number = int(
                        input(f"What is the next {labeled}'s mass number? "))
                    questions = [
                        f"What {labeled}-{mass_number}'s atomic mass? (in amu) ", f"What is {labeled}-{mass_number}'s abundance percentage? (in %) "]
                    answers = []
                    i = 0
                    while i < len(questions):
                        answer = float(input(questions[i]))
                        confirm = input(f"Confirm {answer}? (yes/no) ").lower()
                        if confirm in positive:
                            answers.append(answer)
                            i = i + 1
                        elif confirm in negative:
                            continue  # Don't change i, so it repeat the question again!
                        else:
                            continue  # If they type something else=> no
                    abundance_mass = answers[0] * (answers[1] / 100)
                    ab_mass = ab_mass + abundance_mass
                    print(
                        f"The next isotope is {labeled}-{mass_number} and its mass is {abundance_mass} amu ")
            print(
                f"The average atomic mass of {labeled} is {ab_mass} amu ( or {round(ab_mass, 3)} amu)")
            more = input(
                "Are there any other element you want to calculate the avarage atomic mass? ").lower()
            if more in negative:
                break

    # 2.
    if option in ['2', 'two']:
        print(f""" ---CALCULATE THE MASS USING THE MASS OF SUBATOMIC PARTICLES---  
        1. Enter an isotope (name + mass num))
        2. Enter the number of proton of that element (atomic number) => number of electrons
        3. Calculate the number of neutron
        4. Enter the charge of that element (if no charge write 0)
        5. Calculate the number of electrons base on the charge
        6. Calculate the mass using the mass of protons, electrons, neutrons (in amu)
        7. Convert to kg (yes / no)""")
        print()
        while True:
            isotopes = input("1. Enter an element symbol? ")
            if not isotopes:
                print("You didn't enter an element symbol yet")
                continue
            labeled = isotopes[0].upper() + isotopes[1:].lower()
            mass_number = int(
                input(f"What is isotope of {labeled} do you want to calculate the mass? "))
            lb2 = f"{labeled}-{mass_number}"
            print()
            print(f"CALCULATING {lb2} MASS:")
            p = int(input(
                f"2. Look at the periodic table, what is the atomic number of {lb2}? (protons) "))
            e = p
            while True:
                confirm = input(
                    f'Confirming {lb2} have {p} protons? (yes/no) ').lower()
                if confirm in positive:
                    break
            print()
            print(f'{lb2} has {p} protons and {e} electrons without any charges')
            n = mass_number - p
            print(f'3. {lb2} has {n} neutrons. ')
            print()
            charge = int(input(f"4. What is the charge of {lb2}? "))
            lb_charge = ''
            ewc = 0
            if charge == 0:
                lb_charge = '0'
                ewc = 0
            elif charge > 0:
                lb_charge = f"+{charge}"
                ewc = e - charge
            else:
                lb_charge = f"{charge}"
                ewc = e - charge
            iwc = f"{lb2} ({lb_charge})"
            print(f"""5. For {lb2} (0), there are {e} electrons
                For {iwc}, there are {ewc} electrons""")
            print()
            print(f"""6. In theory:
            m_e = {formatted_mea} amu = {formatted_mek} kg
            m_p = {mass_proton_amu} amu = {formatted_mpk} kg
            m_n = {mass_neutron_amu} amu = {formatted_mnk} kg """)
            # electrons
            m_e_amu = ewc * mass_electron_amu
            m_e_kg = ewc * mass_electron_kg
            # protons
            m_p_amu = p * mass_proton_amu
            m_p_kg = p * mass_proton_kg
            # neutrons
            m_n_amu = n * mass_neutron_amu
            m_n_kg = n * mass_neutron_kg
            print()
            m_amu = m_e_amu + m_p_amu + m_n_amu
            sci_m_amu = f"{m_amu:.2e}"  # '1.23e+05'
            base_m_amu, exp_m_amu = sci_m_amu.split("e")  # ['1.23', '+05']
            exp_m_amu = int(exp_m_amu)  # convert '+05' → 5
            formatted_m_amu = f"{base_m_amu} x 10^{exp_m_amu}"
            print(f"The mass of {iwc} in amu is: {formatted_m_amu} amu ")
            while True:
                confirm_convert = input(
                    f"7. Convert mass of {iwc} = {formatted_m_amu} amu to kg? (yes/no) ").lower()
                if confirm_convert in negative:
                    print(
                        f" The mass of {iwc} in subatomic particles is {formatted_m_amu} amu ")
                elif confirm in positive:
                    break
            m_kg = m_e_kg + m_p_kg + m_n_kg
            sci_m_kg = f"{m_kg:.2e}"  # '1.23e+05'
            base_m_kg, exp_m_kg = sci_m_kg.split("e")  # ['1.23', '+05']
            exp_m_kg = int(exp_m_kg)  # convert '+05' → 5
            formatted_m_kg = f"{base_m_kg} x 10^{exp_m_kg}"
            print(
                f"The mass of {iwc} in subatomic particles is {formatted_m_amu} amu ")
            print(f"or m_{iwc} kg = {formatted_m_kg} kg ")
            more = input(
                "Are there any other element you want to calculate the mass base on the subatomic particle? ").lower()
            if more in negative:
                break
    # 3.
    if option in ['3', 'three']:
        print(f"""  ---CALCULATE THE BINDING ENERGY (REQUIRE 2)
              1. Calculating the Δ mass ( Δmass = subatomic particle mass - atomic mass)
              1a. Calculate the subatomic particle mass (or type in)
              1b. Enter the isotope's atomic mass
              1c. Calculate the Δ mass in amu
              2. Convert the Δ mass in amu into kilograms (Δmass amu * (1.6605*(10^-27)kg/1amu) )
              3. Calculate the binding energy (in Joules (J)) (E=mc^2))""")
        print()
        while True:
            isotopes = input("Enter an element symbol? ")
            if not isotopes:
                print("You didn't enter an element symbol yet")
                continue
            labeled = isotopes[0].upper() + isotopes[1:].lower()
            mass_number = int(
                input(f"What is isotope of {labeled} do you want to calculate the binding energy? "))
            lb2 = f"{labeled}-{mass_number}"
            print()
            print(f"1a. Calculating the subatomic partical of {lb2}")
            ask = input(
                f'Do you want to calculate the subatomic particle of {lb2} or type in? (calculate - "1"/type - "2")').lower()
            if ask in [positive, 'calculate', '1']:
                # Calculate
                print()
                print(f"CALCULATING {lb2} MASS:")
                p = int(input(
                    f"2. Look at the periodic table, what is the atomic number of {lb2}? (protons) "))
                e = p
                while True:
                    confirm = input(
                        f'Confirming {lb2} have {p} protons? (yes/no) ').lower()
                    if confirm in positive:
                        break
                print()
                print(f'{lb2} has {p} protons and {e} electrons without any charges')
                n = mass_number - p
                print(f'3. {lb2} has {n} neutrons. ')
                print()
                charge = int(input(f"4. What is the charge of {lb2}? "))
                lb_charge = ''
                ewc = 0
                if charge == 0:
                    lb_charge = '0'
                    ewc = 0
                elif charge > 0:
                    lb_charge = f"+{charge}"
                    ewc = e - charge
                else:
                    lb_charge = f"{charge}"
                    ewc = e - charge
                iwc = f"{lb2} ({lb_charge})"
                print(f"""5. For {lb2} (0), there are {e} electrons
                    For {iwc}, there are {ewc} electrons""")
                print()
                print(f"""6. In theory:
                m_e = {formatted_mea} amu = {formatted_mek} kg
                m_p = {mass_proton_amu} amu = {formatted_mpk} kg
                m_n = {mass_neutron_amu} amu = {formatted_mnk} kg """)
                # electrons
                m_e_amu = ewc * mass_electron_amu
                m_e_kg = ewc * mass_electron_kg
                # protons
                m_p_amu = p * mass_proton_amu
                m_p_kg = p * mass_proton_kg
                # neutrons
                m_n_amu = n * mass_neutron_amu
                m_n_kg = n * mass_neutron_kg
                print()
                m_amu = m_e_amu + m_p_amu + m_n_amu
                sci_m_amu = f"{m_amu:.2e}"  # '1.23e+05'
                base_m_amu, exp_m_amu = sci_m_amu.split("e")  # ['1.23', '+05']
                exp_m_amu = int(exp_m_amu)  # convert '+05' → 5
                formatted_m_amu = f"{base_m_amu} x 10^{exp_m_amu}"
                print(f"The mass of {iwc} in amu is: {formatted_m_amu} amu ")
                m_kg = m_e_kg + m_p_kg + m_n_kg
                sci_m_kg = f"{m_kg:.2e}"  # '1.23e+05'
                base_m_kg, exp_m_kg = sci_m_kg.split("e")  # ['1.23', '+05']
                exp_m_kg = int(exp_m_kg)  # convert '+05' → 5
                formatted_m_kg = f"{base_m_kg} x 10^{exp_m_kg}"
                print(
                    f"The mass of {iwc} in subatomic particles is {formatted_m_amu} amu ")
                print(f"or m_{iwc} kg = {formatted_m_kg} kg ")
                print()
                question = [f" What is {lb2}'s atomic mass in amu  "]
                answers = []
                i = 0
                while i < len(question):
                    answer = float(input(question[i]))
                    confirm = input(f"Confirm {answer}? (yes/no)  ").lower()
                    if confirm in positive:
                        answers.append(answer)
                        i = i + 1
                    elif confirm in negative:
                        continue  # Don't change i, so it repeat the question again!
                    else:
                        continue  # If they type something else=> no
                mass_amu = answers[0]
                mass_kg = mass_amu*(1.6605*(10**-27))
                delta_mass_kg = m_kg - mass_kg
                sci_delta_mass_kg = f"{delta_mass_kg:.2e}"
                base_delta_mass_kg, exp_delta_mass_kg = sci_delta_mass_kg.split(
                    "e")
                exp_delta_mass_kg = int(exp_delta_mass_kg)
                formatted_delta_mass_kg = f"{base_delta_mass_kg} x 10^{exp_delta_mass_kg}"
                print(
                    f'2.The mass of {iwc} in kg is: {formatted_delta_mass_kg} kg')
                print()
                print(f'3. Calculating the binding energy of {iwc} '
                      )
                e = delta_mass_kg*(c**2)
                sci_e = f"{e:.2e}"
                base_e, exp_e = sci_e.split("e")
                exp_e = int(exp_e)
                formatted_e = f"{base_e} x 10^{exp_e}"
                print()
                print(f"The binding energy of {lb2} is {formatted_e} J ")

            elif ask in [negative, 'type', '2']:
                print()
                question = [f"What is the subatomic particle mass of {lb2}? in amu? ",
                            f"What is {lb2}'s atomic mass: "]
                answers = []
                i = 0
                while i < len(question):
                    answer = float(input(question[i]))
                    confirm = input(f"Confirm {answer}? (yes/no) ").lower()
                    if confirm in positive:
                        answers.append(answer)
                        i = i + 1
                    elif confirm in negative:
                        continue  # Don't change i, so it repeat the question again!
                    else:
                        continue  # If they type something else=> no

                # answers = [sub_mass_amu ,atomic_mass]

                delta_mass_amu = answers[0]-answers[1]
                print(f"The Δ mass of {lb2} in amu is {delta_mass_amu} ")
                print()
                print(
                    f"2. Converting Δ mass = {delta_mass_amu} amu to Δ mass = kg ")
                delta_mass_kg = delta_mass_amu * (1.6605*(10**-27))
                sci_delta_mass_kg = f"{delta_mass_kg:.2e}"
                base_delta_mass_kg, exp_delta_mass_kg = sci_delta_mass_kg.split(
                    "e")
                exp_delta_mass_kg = int(exp_delta_mass_kg)
                formatted_delta_mass_kg = f"{base_delta_mass_kg} x 10^{exp_delta_mass_kg}"
                print(
                    f"The Δ mass of {lb2} in kg is {formatted_delta_mass_kg}")
                print()
                print(f'3. Calculating the binding energy of {lb2} ')
                e = delta_mass_kg*(c**2)
                sci_e = f"{e:.2e}"
                base_e, exp_e = sci_e.split("e")
                exp_e = int(exp_e)
                formatted_e = f"{base_e} x 10^{exp_e}"
                print()
                print(f"The binding energy of {lb2} is {formatted_e} J ")
            more = input(
                "Are there any other element you want to calculate the mass base on the subatomic particle? ").lower()
            if more in negative:
                break
