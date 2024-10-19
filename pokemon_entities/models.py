from django.db import models  

class Pokemon(models.Model):
    title = models.CharField(max_length=200,verbose_name="Название покемона на русском")
    image = models.ImageField(blank=True, null=True, upload_to="pokemons",verbose_name="Картинка")
    description = models.TextField(blank=True, null=True,verbose_name="Описание покемона")
    title_en = models.CharField(max_length=150,blank=True, null=True, verbose_name="Название покемона на английском")
    title_jp = models.CharField(max_length=150,blank=True, null=True, verbose_name="Название покемона на японском")
    evolution = models.ForeignKey(
        "Pokemon" ,
        on_delete=models.CASCADE, 
        blank=True, 
        null=True,
        related_name="next_evolutions",
        verbose_name="Предыдущая эволюция"
    )

    def __str__(self):
        return self.title
    
class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name="Широта ")
    lon = models.FloatField(verbose_name="Долгота")
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Покемон")
    appeared_at = models.DateTimeField(null=True, blank=True, verbose_name="Когда появляется на карте")
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name="Когда исчезает с карты")
    level = models.IntegerField(null=True, blank=True, verbose_name="Уровень")
    health = models.IntegerField(null=True, blank=True, verbose_name="Здоровье")
    strenght = models.IntegerField(null=True, blank=True, verbose_name="Сила")
    defence = models.IntegerField(null=True, blank=True, verbose_name="Защита")
    stamina = models.IntegerField(null=True, blank=True, verbose_name="Выносливость")

    def __str__(self):
        return f'{self.lat} {self.lon} {self.pokemon.title}'