import pandas as pd
vendedores = ["Ana", "Luis", "Marta", "Sergio"]
ventas = [1500.50, 2300.75, 1800.00, 2100.25]
df = pd.DataFrame({
    "Vendedor": vendedores, 
    "Ventas": ventas
})  
print(df)

print("\nInformación del DataFrame:")