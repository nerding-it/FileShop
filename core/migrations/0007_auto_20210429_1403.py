# Generated by Django 3.2 on 2021-04-29 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210425_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status_of_transaction',
            field=models.IntegerField(choices=[(-1, 'Not Started'), (0, 'Unconfirmed'), (1, 'Partial Confirmed'), (2, 'Confimed')], default=-1),
        ),
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('ZAR', 'ZAR'), ('TPE', 'TPE'), ('SIT', 'SIT'), ('BHD', 'BHD'), ('GTQ', 'GTQ'), ('TND', 'TND'), ('NPR', 'NPR'), ('UYU', 'UYU'), ('XEU', 'XEU'), ('CNH', 'CNH'), ('SOS', 'SOS'), ('GEL', 'GEL'), ('MXN', 'MXN'), ('BOB', 'BOB'), ('SAR', 'SAR'), ('HRK', 'HRK'), ('BGN', 'BGN'), ('SBD', 'SBD'), ('XDR', 'XDR'), ('BDT', 'BDT'), ('AFN', 'AFN'), ('DDM', 'DDM'), ('MZE', 'MZE'), ('CNX', 'CNX'), ('MXP', 'MXP'), ('MDC', 'MDC'), ('DKK', 'DKK'), ('MUR', 'MUR'), ('VUV', 'VUV'), ('NIC', 'NIC'), ('MRU', 'MRU'), ('TMM', 'TMM'), ('MOP', 'MOP'), ('GHS', 'GHS'), ('LTL', 'LTL'), ('BGO', 'BGO'), ('SHP', 'SHP'), ('UAK', 'UAK'), ('ANG', 'ANG'), ('XRE', 'XRE'), ('MGA', 'MGA'), ('BOP', 'BOP'), ('YUN', 'YUN'), ('ADP', 'ADP'), ('ALK', 'ALK'), ('XBC', 'XBC'), ('BTN', 'BTN'), ('BMD', 'BMD'), ('ZRN', 'ZRN'), ('KRO', 'KRO'), ('GWP', 'GWP'), ('HKD', 'HKD'), ('BIF', 'BIF'), ('BOL', 'BOL'), ('BGL', 'BGL'), ('KYD', 'KYD'), ('PLN', 'PLN'), ('CHE', 'CHE'), ('VEF', 'VEF'), ('USD', 'USD'), ('NGN', 'NGN'), ('SZL', 'SZL'), ('XBB', 'XBB'), ('SRD', 'SRD'), ('IRR', 'IRR'), ('NZD', 'NZD'), ('CLE', 'CLE'), ('CYP', 'CYP'), ('TRY', 'TRY'), ('MYR', 'MYR'), ('COP', 'COP'), ('GNS', 'GNS'), ('UYW', 'UYW'), ('RWF', 'RWF'), ('YDD', 'YDD'), ('YUM', 'YUM'), ('FKP', 'FKP'), ('KZT', 'KZT'), ('BRR', 'BRR'), ('AED', 'AED'), ('GMD', 'GMD'), ('BGM', 'BGM'), ('PES', 'PES'), ('VNN', 'VNN'), ('TZS', 'TZS'), ('AOR', 'AOR'), ('GHC', 'GHC'), ('CNY', 'CNY'), ('TWD', 'TWD'), ('BOV', 'BOV'), ('BRE', 'BRE'), ('RHD', 'RHD'), ('KPW', 'KPW'), ('UZS', 'UZS'), ('JOD', 'JOD'), ('ZWL', 'ZWL'), ('AOK', 'AOK'), ('BRZ', 'BRZ'), ('ARS', 'ARS'), ('ZWR', 'ZWR'), ('ALL', 'ALL'), ('BAD', 'BAD'), ('AMD', 'AMD'), ('XUA', 'XUA'), ('MMK', 'MMK'), ('MKD', 'MKD'), ('FRF', 'FRF'), ('MTL', 'MTL'), ('KMF', 'KMF'), ('GWE', 'GWE'), ('ARP', 'ARP'), ('XPT', 'XPT'), ('VES', 'VES'), ('NIO', 'NIO'), ('XCD', 'XCD'), ('YER', 'YER'), ('LRD', 'LRD'), ('MGF', 'MGF'), ('ESA', 'ESA'), ('TOP', 'TOP'), ('STN', 'STN'), ('TJR', 'TJR'), ('JMD', 'JMD'), ('COU', 'COU'), ('OMR', 'OMR'), ('TMT', 'TMT'), ('UYI', 'UYI'), ('SLL', 'SLL'), ('GIP', 'GIP'), ('USS', 'USS'), ('VEB', 'VEB'), ('MDL', 'MDL'), ('BEC', 'BEC'), ('PGK', 'PGK'), ('XPD', 'XPD'), ('AZM', 'AZM'), ('NAD', 'NAD'), ('LTT', 'LTT'), ('DEM', 'DEM'), ('GRD', 'GRD'), ('MNT', 'MNT'), ('BAM', 'BAM'), ('HTG', 'HTG'), ('MCF', 'MCF'), ('MWK', 'MWK'), ('IQD', 'IQD'), ('USN', 'USN'), ('BRC', 'BRC'), ('BAN', 'BAN'), ('GBP', 'GBP'), ('XAF', 'XAF'), ('CDF', 'CDF'), ('BRN', 'BRN'), ('AOA', 'AOA'), ('CZK', 'CZK'), ('SGD', 'SGD'), ('XBA', 'XBA'), ('ARM', 'ARM'), ('IEP', 'IEP'), ('MLF', 'MLF'), ('KRH', 'KRH'), ('THB', 'THB'), ('ROL', 'ROL'), ('EUR', 'EUR'), ('BBD', 'BBD'), ('STD', 'STD'), ('EEK', 'EEK'), ('CHF', 'CHF'), ('ATS', 'ATS'), ('ZWD', 'ZWD'), ('DOP', 'DOP'), ('PLZ', 'PLZ'), ('LVR', 'LVR'), ('SDP', 'SDP'), ('RUR', 'RUR'), ('BRB', 'BRB'), ('PHP', 'PHP'), ('ECS', 'ECS'), ('ITL', 'ITL'), ('BEF', 'BEF'), ('MVR', 'MVR'), ('LAK', 'LAK'), ('LKR', 'LKR'), ('KWD', 'KWD'), ('ECV', 'ECV'), ('CSK', 'CSK'), ('SDG', 'SDG'), ('LUF', 'LUF'), ('ZMK', 'ZMK'), ('AFA', 'AFA'), ('SDD', 'SDD'), ('DJF', 'DJF'), ('AON', 'AON'), ('SCR', 'SCR'), ('ZRZ', 'ZRZ'), ('KRW', 'KRW'), ('FJD', 'FJD'), ('BND', 'BND'), ('ESB', 'ESB'), ('ILR', 'ILR'), ('EGP', 'EGP'), ('LSL', 'LSL'), ('CVE', 'CVE'), ('XPF', 'XPF'), ('FIM', 'FIM'), ('PEN', 'PEN'), ('LUL', 'LUL'), ('PYG', 'PYG'), ('SYP', 'SYP'), ('PTE', 'PTE'), ('CAD', 'CAD'), ('XFO', 'XFO'), ('VND', 'VND'), ('CUP', 'CUP'), ('BYN', 'BYN'), ('ILS', 'ILS'), ('BYR', 'BYR'), ('SEK', 'SEK'), ('YUD', 'YUD'), ('QAR', 'QAR'), ('XAG', 'XAG'), ('JPY', 'JPY'), ('TTD', 'TTD'), ('ISK', 'ISK'), ('MRO', 'MRO'), ('SVC', 'SVC'), ('PAB', 'PAB'), ('CRC', 'CRC'), ('GYD', 'GYD'), ('RON', 'RON'), ('XBD', 'XBD'), ('SKK', 'SKK'), ('KES', 'KES'), ('AUD', 'AUD'), ('MZN', 'MZN'), ('CHW', 'CHW'), ('ZAL', 'ZAL'), ('MAF', 'MAF'), ('CLF', 'CLF'), ('NLG', 'NLG'), ('XAU', 'XAU'), ('ARA', 'ARA'), ('NOK', 'NOK'), ('GEK', 'GEK'), ('MVP', 'MVP'), ('UYP', 'UYP'), ('UGX', 'UGX'), ('ARL', 'ARL'), ('BZD', 'BZD'), ('MZM', 'MZM'), ('CSD', 'CSD'), ('LBP', 'LBP'), ('DZD', 'DZD'), ('ZMW', 'ZMW'), ('TRL', 'TRL'), ('UAH', 'UAH'), ('BRL', 'BRL'), ('HUF', 'HUF'), ('CUC', 'CUC'), ('WST', 'WST'), ('MTP', 'MTP'), ('PEI', 'PEI'), ('BSD', 'BSD'), ('MAD', 'MAD'), ('ISJ', 'ISJ'), ('HRD', 'HRD'), ('BWP', 'BWP'), ('KGS', 'KGS'), ('LVL', 'LVL'), ('XTS', 'XTS'), ('AWG', 'AWG'), ('RSD', 'RSD'), ('ILP', 'ILP'), ('IDR', 'IDR'), ('ERN', 'ERN'), ('BYB', 'BYB'), ('INR', 'INR'), ('UGS', 'UGS'), ('KHR', 'KHR'), ('GQE', 'GQE'), ('SUR', 'SUR'), ('HNL', 'HNL'), ('TJS', 'TJS'), ('XXX', 'XXX'), ('SSP', 'SSP'), ('BEL', 'BEL'), ('YUR', 'YUR'), ('ETB', 'ETB'), ('LUC', 'LUC'), ('ESP', 'ESP'), ('MKN', 'MKN'), ('SRG', 'SRG'), ('CLP', 'CLP'), ('GNF', 'GNF'), ('MXV', 'MXV'), ('XSU', 'XSU'), ('XFU', 'XFU'), ('XOF', 'XOF'), ('BUK', 'BUK'), ('LYD', 'LYD'), ('PKR', 'PKR'), ('AZN', 'AZN'), ('RUB', 'RUB')], default='USD', max_length=3),
        ),
    ]