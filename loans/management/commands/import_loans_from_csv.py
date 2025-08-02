import csv
from datetime import datetime

from django.core.management import BaseCommand
from loans.models import Loan


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV'
        )

        parser.add_argument(
            '--delete-existing',
            action='store_true',
            help='Deletar dados existentes antes de importar novos'
        )

    def handle(self, *args, **options):
        DATE_FORMAT = '%Y-%m-%d'
        DATETIME_FORMAT = f'{DATE_FORMAT} %H:%M:%S'
        file_name = options['file_name']
        delete_existing = options['delete_existing']

        if delete_existing:
            Loan.objects.all().delete()
            self.stdout.write(self.style.WARNING('Dados existentes deletados.'))

        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                for field in ['book_id', 'reader_id']:
                    if not row.get(field):
                        row[field] = None

                for field in ['loan_date', 'expected_return_date', 'actual_return_date']:
                    if row.get(field):
                        row[field] = datetime.strptime(row[field], DATE_FORMAT).date()
                    else:
                        row[field] = None

                row['created_at'] = datetime.strptime(row['created_at'].split('.')[0], DATETIME_FORMAT)
                row['updated_at'] = datetime.strptime(row['updated_at'].split('.')[0], DATETIME_FORMAT)

                obj = Loan.objects.create(**row)
                self.stdout.write(self.style.NOTICE(str(obj)))

        self.stdout.write(self.style.SUCCESS('Dados importados com sucesso!'))
