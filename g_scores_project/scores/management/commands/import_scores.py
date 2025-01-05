from django.core.management.base import BaseCommand
from scores.models import Score
import csv

class Command(BaseCommand):
    help = "Import scores from a CSV file into the database"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    Score.objects.create(
                        sbd=row['sbd'],
                        toan=float(row['toan']) if row['toan'] else None,
                        ngu_van=float(row['ngu_van']) if row['ngu_van'] else None,
                        ngoai_ngu=float(row['ngoai_ngu']) if row['ngoai_ngu'] else None,
                        vat_li=float(row['vat_li']) if row['vat_li'] else None,
                        hoa_hoc=float(row['hoa_hoc']) if row['hoa_hoc'] else None,
                        sinh_hoc=float(row['sinh_hoc']) if row['sinh_hoc'] else None,
                        lich_su=float(row['lich_su']) if row['lich_su'] else None,
                        dia_li=float(row['dia_li']) if row['dia_li'] else None,
                        gdcd=float(row['gdcd']) if row['gdcd'] else None,
                        ma_ngoai_ngu=row['ma_ngoai_ngu'] if row['ma_ngoai_ngu'] else None,
                    )
            self.stdout.write(self.style.SUCCESS("Scores successfully imported from CSV."))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File '{csv_file}' not found."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {e}"))
