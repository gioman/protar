import datetime

from celery import shared_task

from corine.models import Patch
from django.contrib.gis.db.models.functions import Area, Intersection
from django.db.models import Sum
from natura.models import Cover, Site


@shared_task
def process_sites(sites):
    now = '[{0}]'.format(datetime.datetime.now().strftime('%Y-%m-%d %T'))
    print('{} Processing ids {} ... {}.'.format(now, sites[0], sites[-1]))

    batch = []
    for site in Site.objects.filter(id__in=sites):
        # Filter patches that intersect with this site
        qs = Patch.objects.filter(geom__intersects=site.geom)
        # Group output by relevant factors
        qs = qs.values('year', 'nomenclature_id', 'change', 'nomenclature_previous_id')
        # Annotate with sum of intersection areas
        qs = qs.annotate(area=Sum(Area(Intersection('geom', site.geom))))
        # Assemble cover objects from aggregate result
        for dat in qs:
            batch.append(Cover(site=site, **dat))
    # Commit cover for the sites to database
    Cover.objects.bulk_create(batch)
