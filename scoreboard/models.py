from django.db import models



class Game(models.Model):
    title = models.CharField(max_length=10485)
    description = models.CharField(max_length=10485)
    photo_url = models.CharField(max_length=10485, null=True)

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist', default=1)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='wishlist', default=1)

class Library(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='library', default=1)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='library', default=1)

class Catalogue(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='Catalogue', default=1)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='wishlist', default=1)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='library', default=1)

class WishlistCatalogue(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='wishlistcatalogue', default=1)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='wishlistcatalogue', default=1)

class LibraryCatalogue(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='librarycatalogue', default=1)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='librarycatalogue', default=1)