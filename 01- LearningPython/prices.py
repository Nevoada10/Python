from math import floor

# Variables Definitions:

base_discount = 30 / 100  # Percentage. # Default = 20%
base_price = 90  # R$
hours = 6
customer_name = ""
linear_ratio = int(round((base_price * (1 - base_discount)), -1))  # 0.8
final_price_sex = base_price + linear_ratio * hours  # Final price.
final_blowjob_price = int(round((base_price * (1 - base_discount)), -1))


# Functions Definitions:


def long_package(hours):
    package = (base_price + linear_ratio * hours) * (1 - base_discount)
    return int(package)


# Intro:

print("Deixe-me ser a nota sombria que completa a sua sinfonia.\n\nEntão {customer_name} infelizmente eu não "
      "tenho local fixo, e é um dos motivos pelos quais eu tenho um\nprecinho mais em conta."
      " A primeira hora é {base_price} R$, e cada hora extra são {linear_ratio} R$, e a mamada é\n"
      "{final_blowjob_price} R$ por cada dose de leitinho, okay anjo?\n"
      .format(customer_name=customer_name, base_price=base_price, linear_ratio=linear_ratio,
              final_blowjob_price=final_blowjob_price))

# Blowjob:
# final_blowjob_price = int(round((linear_ratio * (1 - base_discount)), -1))
print("💫 Banquete de Almas: ( Mamada ):")
print("Por Mamada:", final_blowjob_price, "R$\n")

# Sex price list:
print("🌹 Dança Noturna: ( Sexo + Mamada + Anal ):")
for hours in range(hours):
    price_sex = int(base_price + linear_ratio * hours)
    print(str(hours + 1) + " h:", price_sex, "R$")
print("...\n")

print("Pernoite: (12h):", round(long_package(12), -2), "R$")
print("Um Dia nas Sombras:(24h ou 1d):", round(long_package(24), -2), "R$")
print("Fim de Semana na Escuridão (48h ou 2d):", 100 * floor(long_package(48) / 100), "R$\n")

# Closing:

print("Invoco você a compartilhar essa dança enigmática comigo.\nDepois me fala o que achou dos preços e das ofertas, "
      "adoro ouvir os feedbacks!")
