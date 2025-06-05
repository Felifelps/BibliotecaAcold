import csv
from datetime import datetime

from django.core.management import BaseCommand
from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV'
        )

        parser.add_argument(
            'delete_existing',
            type=bool,
            help='Deletar dados existentes antes de importar novos?'
        )

    def handle(self, *args, **options):
        DATE_FORMAT = '%Y-%m-%d'
        DATETIME_FORMAT = f'{DATE_FORMAT} %H:%M:%S'
        file_name = options['file_name']
        delete_existing = options['delete_existing']

        if delete_existing:
            Book.objects.all().delete()
            self.stdout.write(self.style.WARNING('Dados existentes deletados.'))

        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                for field in ['author_id', 'location_id', 'category_id', 'publisher_id']:
                    if not row.get(field):
                        row[field] = None

                if row['publication_date']:
                    row['publication_date'] = datetime.strptime(row['publication_date'], DATE_FORMAT)
                else:
                    row['publication_date'] = None

                row['created_at'] = datetime.strptime(row['created_at'].split('.')[0], DATETIME_FORMAT)
                row['updated_at'] = datetime.strptime(row['updated_at'].split('.')[0], DATETIME_FORMAT)

                obj = Book.objects.create(**row)
                self.stdout.write(self.style.NOTICE(str(obj)))

        self.stdout.write(self.style.SUCCESS('Dados importados com sucesso!'))
