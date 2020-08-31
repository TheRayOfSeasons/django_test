from django.db import models


class Chair(models.Model):
    """
    This represents some goodass chair.
    """
    WOOD = 'wood'
    STEEL = 'steel'
    COUCH = 'couch'
    ASCENDED = 'ascended'
    IMMORTAL = 'immortal'
    TYPES = (
        (WOOD, 'Wood'),
        (STEEL, 'Steel'),
        (COUCH, 'Couch'),
        (ASCENDED, 'Ascended'),
        (IMMORTAL, 'Immortal')
    )

    name = models.CharField(max_length=64)
    sittabilitiy = models.IntegerField()
    kind = models.CharField(max_length=16, choices=TYPES)
    is_soft = models.BooleanField(default=False)

    def __str__(self):
        return self.name
