from faker import Faker
from content.colors import Color

fake = Faker()

#nome = fake.name()
#primeiro_nome_fem = fake.first_name_female()
#usuario = fake.user_name()
#mes = fake.month()
senha = fake.password()

print(Color.VERMELHO + f'sua senha gerada é : {senha}')