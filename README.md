# ⚛️ Atomic Analyzer

A fully interactive **Python CLI** tool for physics and chemistry calculations related to **atomic structure, isotopes, and binding energy**.

---

## 🎯 Overview

This tool helps students, teachers, and researchers quickly calculate:
- **Average atomic mass** from isotope data  
- **Mass of isotopes** using subatomic particle masses  
- **Binding energy** (E = mc²) *(under development)*  

It’s designed to be **clear, interactive, and educational** — perfect for classroom use or personal learning.

---

## 🚀 Features

✅ Calculate **average atomic mass** based on isotope masses and abundances  
✅ Compute **isotope mass** from subatomic particles (protons, neutrons, electrons)  
✅ Convert between **amu** and **kg** automatically  
✅ Input validation and confirmation for each user entry  
✅ Built-in constants for accurate scientific computation  
✅ Ready for **future GUI integration** or **database linking**

---

## 🧪 Scientific Constants Used

| Quantity | Symbol | Value | Unit |
|-----------|---------|--------|------|
| Proton mass | mₚ | 1.00727 | amu |
| Neutron mass | mₙ | 1.00867 | amu |
| Electron mass | mₑ | 5.485 × 10⁻⁴ | amu |
| Proton mass | mₚ | 1.673 × 10⁻²⁷ | kg |
| Neutron mass | mₙ | 1.675 × 10⁻²⁷ | kg |
| Electron mass | mₑ | 9.11 × 10⁻³¹ | kg |
| Speed of light | c | 2.998 × 10⁸ | m/s |

---

## ⚙️ Requirements

- Python **3.10+**  
- No external libraries required

---

## 🧩 Installation

```bash
# clone the repo
git clone https://github.com/ngthdi17/atomic-analyzer.git

# navigate to project folder
cd atomic-analyzer

# run the main script
python Atomic_Analyzer_Advanced.py
🧠 How It Works
1️⃣ Average Atomic Mass

Process:

Enter the element symbol (e.g., Cl, Na, C).

Specify the number of isotopes.

For each isotope:

Enter its mass number

Enter its atomic mass (amu)

Enter its abundance (%)

The program calculates:

Average atomic mass
=
∑
(
isotope mass
×
abundance
/
100
)
Average atomic mass=∑(isotope mass×abundance/100)
Example:
Element: Cl  
Isotopes: 2
Cl-35 → 34.969 amu (75.78%)
Cl-37 → 36.966 amu (24.22%)

Average atomic mass = 35.453 amu
2️⃣ Mass From Subatomic Particles

Process:

Enter element symbol and mass number (e.g., O-16)

Input atomic number (number of protons)

The app calculates:

Neutrons = mass number - protons

Electrons = protons ± charge

Masses are computed as:

𝑀
=
(
𝑝
×
𝑚
𝑝
)
+
(
𝑛
×
𝑚
𝑛
)
+
(
𝑒
×
𝑚
𝑒
)
M=(p×m
p
	​

)+(n×m
n
	​

)+(e×m
e
	​

)

Convert between amu and kg using:

1
 amu
=
1.6605
×
10
−
27
 kg
1 amu=1.6605×10
−27
 kg

The output is formatted in scientific notation automatically:
1.23 × 10^−25 kg
3️⃣ Binding Energy (Coming Soon)

It will use:

𝐸
=
Δ
𝑚
𝑐
2
E=Δmc
2

where Δm is the mass defect between predicted atomic mass and measured atomic mass.
💡 Example Interaction
WELCOME TO ATOMIC ANALYZER
Options:
 1. Calculate average atomic mass
 2. Calculate the mass using the mass of subatomic particles
 3. Calculate the binding energy
 4. Exit

Option: 1
Enter an element symbol? Cl
How many isotopes are there in this element? 2
What Cl-35's atomic mass? (in amu) 34.969
What is Cl-35's abundance percentage? (in %) 75.78
What is Cl-37's atomic mass? (in amu) 36.966
What is Cl-37's abundance percentage? (in %) 24.22

The average atomic mass of Cl is 35.453 amu
🗂️ Project Structure
atomic-analyzer/
│
├── Atomic_Analyzer_Advanced.py     # main interactive script
├── README.md                       # project documentation
├── .gitignore                      # excluded files
└── test.py                         # test sandbox
🧭 Future Improvements

Add binding energy computation

Add GUI interface (Tkinter or PyQT)

Add database of isotope masses for auto-calculation

Add unit test framework for scientific validation

Option to export data to CSV or JSON
⚠️ Known Issues

Option 3 (binding energy) is incomplete

Input errors (non-numeric) may cause loops — will add better error catching

Conversion confirmations need streamlining
👥 Contributors

ngthdi17 — Creator & Developer

(add your friend’s GitHub username) — Collaborator

If you want to contribute:

Fork the repo

Create a new branch (feature-newcalc)

Commit your changes

Submit a Pull Request

📜 License

This project is open-source under the MIT License — free to use, modify, and distribute.

🌟 Acknowledgments

Inspired by physics and chemistry learners who want accurate, clean tools for real calculations — not pre-made apps.
Built to learn, understand, and calculate scientifically.

---


How to run:
git clone https://github.com/ngthdi17/Atomic-calculator
cd Atomic-calculator
python Atomic_Analyzer_Advanced.py

What I’m Looking For?
Is my file structure clean?

Any optimization suggestions for performance?

How can I make this tool more user-friendly?

Thanks for helping me!
