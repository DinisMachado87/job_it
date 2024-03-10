# Generated by Django 4.2.11 on 2024-03-10 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_manager', '0003_alter_job_bring_pet_alter_job_child_care_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='bring_pet',
            field=models.IntegerField(choices=[(0, 'N/a'), (1, 'Yes'), (2, 'No')], default=1, help_text='Whether pets are allowed in the office'),
        ),
        migrations.AlterField(
            model_name='job',
            name='child_care',
            field=models.IntegerField(choices=[(0, 'N/a'), (1, 'Yes'), (2, 'No')], default=1, help_text='Availability of child care close to the office'),
        ),
        migrations.AlterField(
            model_name='job',
            name='company_size',
            field=models.IntegerField(choices=[(0, 'N/a'), (1, 'Small'), (2, 'Medium'), (3, 'Large')], default=1, help_text='Size of the company'),
        ),
        migrations.AlterField(
            model_name='job',
            name='freelance_hire',
            field=models.IntegerField(choices=[(0, 'N/a'), (1, 'Yes'), (2, 'No')], default=0, help_text='If you will be invoicing the company or hired as an employee'),
        ),
        migrations.AlterField(
            model_name='job',
            name='office_days',
            field=models.IntegerField(choices=[(0, 'N/a'), (1, 'Working from home'), (2, '1'), (3, '2'), (4, '3'), (5, '4'), (6, '5'), (7, '6'), (8, '7')], default=5, help_text='Number of office days per week'),
        ),
        migrations.AlterField(
            model_name='job',
            name='office_type',
            field=models.IntegerField(choices=[(0, 'N/a'), (1, 'Open'), (2, 'Cubicle'), (3, 'Private')], default=0, help_text='Type of office layout'),
        ),
        migrations.AlterField(
            model_name='job',
            name='own_computer',
            field=models.IntegerField(choices=[(0, 'N/a'), (1, 'Yes'), (2, 'No')], default=1, help_text='Whether you need to bring your own computer'),
        ),
        migrations.AlterField(
            model_name='job',
            name='pet_sitter',
            field=models.IntegerField(choices=[(0, 'N/a'), (1, 'Yes'), (2, 'No')], default=1, help_text='Availability of pet sitter close to the office'),
        ),
        migrations.AlterField(
            model_name='job',
            name='responsibility',
            field=models.IntegerField(choices=[(0, 'N/a'), (1, 'Manager'), (2, 'Supervisor'), (3, 'Team Leader'), (4, 'Employee')], default=3, help_text='Job responsibility level', null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='schedule_type',
            field=models.IntegerField(choices=[(0, 'N/a'), (1, 'Fixed'), (2, 'Flexible'), (3, 'Remote')], default=0, help_text='Type of work schedule'),
        ),
        migrations.AlterField(
            model_name='job',
            name='starting_time',
            field=models.IntegerField(choices=[(0, 'N/a'), (1, '6:00am'), (2, '6:30am'), (3, '7:00am'), (4, '7:30am'), (5, '8:00am'), (6, '8:30am'), (7, '9:00am'), (8, '9:30am'), (9, '10:00am'), (10, '10:30am'), (11, '11:00am'), (12, '11:30am'), (13, '12:00pm'), (14, '12:30pm'), (15, '1:00pm'), (16, '1:30pm'), (17, '2:00pm'), (18, '2:30pm'), (19, '3:00pm'), (20, '3:30pm'), (21, '4:00pm'), (22, '4:30pm'), (23, '5:00pm'), (24, '5:30pm'), (25, '6:00pm'), (26, '6:30pm'), (27, '7:00pm'), (28, '7:30pm'), (29, '8:00pm'), (30, '8:30pm'), (31, '9:00pm'), (32, '9:30pm'), (33, '10:00pm'), (34, '10:30pm'), (35, '11:00pm'), (36, '11:30pm'), (37, '12:00am'), (38, '12:30am'), (39, '1:00am'), (40, '1:30am'), (41, '2:00am'), (42, '2:30am'), (43, '3:00am'), (44, '3:30am'), (45, '4:00am'), (46, '4:30am'), (47, '5:00am'), (48, '5:30am')], default=0, help_text='Starting time of the work'),
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.IntegerField(choices=[(0, 'N/a'), (1, 'Considering'), (2, 'Applied'), (3, 'Interviewing'), (4, 'Rejected'), (5, 'Accepted')], default=0, help_text='Current status of the job application'),
        ),
    ]
