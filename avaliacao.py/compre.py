nissin=float(input("quanto custa o miojo nissin "))
renata=float(input("quanto custa o miojo renata "))
adria=float(input("quanto custa o miojo adria"))
if (nissin<renata and nissin<adria):
    print(f"comprarei nissin por ser o mais barato")
if (renata<nissin and renata<adria):
    print(f"comprarei renata por ser o mais barato")
if (adria<nissin and adria<renata):
    print(f"comprarei adria por ser o mais barato")

