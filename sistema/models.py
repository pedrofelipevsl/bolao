from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
	def create_user(self, username, password=None):
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, password):
		user = self.create_user(
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Apostador(AbstractBaseUser):
	username = models.CharField(max_length=30, unique=True)
	saldo = models.FloatField(default=10.00)

	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'

	objects = MyAccountManager()

	def __str__(self):
		return self.username

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True


class Selecao(models.Model):
	nome_da_selecao = models.CharField(max_length=200) 
	qtd_de_titulos = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.nome_da_selecao

class Partida(models.Model):
	selecao_desafiante = models.ForeignKey(Selecao, on_delete=models.CASCADE, related_name='selecaodesafiante')
	selecao_visitante = models.ForeignKey(Selecao, on_delete=models.CASCADE, related_name='selecaovisitante')
	gols_desafiante = models.PositiveSmallIntegerField(blank=True, null=True)
	gols_visitante = models.PositiveSmallIntegerField(blank=True, null=True)
	estadio = models.CharField(max_length=200)
	data_hora = models.DateTimeField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return "%s x %s" % (self.selecao_desafiante, self.selecao_visitante,)

class Bolao(models.Model):
	nome_do_bolao = models.CharField(max_length=200)
	partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
	premiacao = models.FloatField(default=0.0)
	valor_disputado = models.FloatField(default=0.0)

	#vencedores = models.ForeignKey(Apostador, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome_do_bolao

class Aposta(models.Model):
	class Meta:
		unique_together = (('apostador','bolao'),)
	apostador = models.ForeignKey(Apostador, on_delete=models.CASCADE)
	bolao = models.ForeignKey(Bolao, on_delete=models.CASCADE)
	# A PK é composta de apostador e bolao
	qtd_gols_desafiante_apostado = models.PositiveSmallIntegerField()
	qtd_gols_visitante_apostado = models.PositiveSmallIntegerField()
	valor_da_aposta = models.FloatField(default=5.00)

	def __str__(self):
		return "%s aposta na partida com R$ %.2f reais" % (self.apostador, self.valor_da_aposta)

class ApostadoresVencedoresBolao(models.Model):
	class Meta:
		unique_together = (('apostador','bolao'),)
	apostador = models.ForeignKey(Apostador, on_delete=models.CASCADE)
	bolao = models.ForeignKey(Bolao, on_delete=models.CASCADE)
	#A PK é composta de apostador e bolao