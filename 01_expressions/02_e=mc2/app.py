# Problem Statement

# E = m * c**2

# Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

# Solution

def main():
    SPEEd_OF_LIGHT = 299_792_458
    
    print("🔬 Welcome to the Mass-Energy Calculator 🔬")
    
    # Mass in kilograms
    mass_kg = float(input("💡 Enter mass in kilogram: "))
    
    # Calculate Energy
    energy = mass_kg * SPEEd_OF_LIGHT ** 2
    
    print("\n📘 Calculaton steps using: E = m x c squared")
    print(f"👉 Mass (m): {mass_kg}")
    print(f"👉 Speed of light (c): {SPEEd_OF_LIGHT} m/s")
    print(f"⚡ Calculated Energy (E): {energy}")
    
    print("\n✅ Energy successfully calculated")
    
if __name__ == "__main__":
    main()
    