from django.db import models  

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True, upload_to="pokemons")
    description = models.TextField(blank=True, null=True)
    title_en = models.CharField(max_length=150,blank=True, null=True)
    title_jp = models.CharField(max_length=150,blank=True, null=True)
    evolution = models.ForeignKey("Pokemon" ,on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
    
class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True, blank=True)
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    strenght = models.IntegerField(null=True, blank=True)
    defence = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.lat} {self.lon} {self.pokemon.title}'