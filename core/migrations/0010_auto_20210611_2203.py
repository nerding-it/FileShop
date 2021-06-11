# Generated by Django 3.2 on 2021-06-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_product_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='usd_price',
            field=models.DecimalField(decimal_places=10, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('AED', 'AED'), ('NPR', 'NPR'), ('LVR', 'LVR'), ('MCF', 'MCF'), ('BAN', 'BAN'), ('XAF', 'XAF'), ('MAF', 'MAF'), ('DKK', 'DKK'), ('BRL', 'BRL'), ('KRH', 'KRH'), ('ISJ', 'ISJ'), ('PYG', 'PYG'), ('FRF', 'FRF'), ('BRZ', 'BRZ'), ('CLE', 'CLE'), ('ZRN', 'ZRN'), ('KRO', 'KRO'), ('ALK', 'ALK'), ('PES', 'PES'), ('MZE', 'MZE'), ('SHP', 'SHP'), ('ROL', 'ROL'), ('JOD', 'JOD'), ('SVC', 'SVC'), ('RHD', 'RHD'), ('LBP', 'LBP'), ('EEK', 'EEK'), ('VEB', 'VEB'), ('HUF', 'HUF'), ('LUL', 'LUL'), ('KYD', 'KYD'), ('ERN', 'ERN'), ('ECV', 'ECV'), ('BIF', 'BIF'), ('ARL', 'ARL'), ('YER', 'YER'), ('ECS', 'ECS'), ('NZD', 'NZD'), ('CNX', 'CNX'), ('GMD', 'GMD'), ('MXV', 'MXV'), ('SSP', 'SSP'), ('SDP', 'SDP'), ('KGS', 'KGS'), ('ILR', 'ILR'), ('MZM', 'MZM'), ('EGP', 'EGP'), ('SZL', 'SZL'), ('YUN', 'YUN'), ('PTE', 'PTE'), ('KWD', 'KWD'), ('LVL', 'LVL'), ('ESP', 'ESP'), ('BYB', 'BYB'), ('SOS', 'SOS'), ('TMM', 'TMM'), ('HTG', 'HTG'), ('CHE', 'CHE'), ('ZWD', 'ZWD'), ('SUR', 'SUR'), ('BRN', 'BRN'), ('EUR', 'EUR'), ('PKR', 'PKR'), ('MXP', 'MXP'), ('CNY', 'CNY'), ('TRL', 'TRL'), ('MYR', 'MYR'), ('LUC', 'LUC'), ('NGN', 'NGN'), ('NIC', 'NIC'), ('TND', 'TND'), ('MGA', 'MGA'), ('TRY', 'TRY'), ('MOP', 'MOP'), ('CLF', 'CLF'), ('XAG', 'XAG'), ('XFU', 'XFU'), ('OMR', 'OMR'), ('SRG', 'SRG'), ('TTD', 'TTD'), ('MDL', 'MDL'), ('XRE', 'XRE'), ('KES', 'KES'), ('ARP', 'ARP'), ('AOA', 'AOA'), ('UYW', 'UYW'), ('XEU', 'XEU'), ('TOP', 'TOP'), ('UAK', 'UAK'), ('BUK', 'BUK'), ('CSD', 'CSD'), ('RUB', 'RUB'), ('PLN', 'PLN'), ('SDG', 'SDG'), ('ATS', 'ATS'), ('COP', 'COP'), ('BEC', 'BEC'), ('CUC', 'CUC'), ('KHR', 'KHR'), ('MMK', 'MMK'), ('JPY', 'JPY'), ('SDD', 'SDD'), ('CUP', 'CUP'), ('USN', 'USN'), ('XXX', 'XXX'), ('BRC', 'BRC'), ('BGN', 'BGN'), ('WST', 'WST'), ('MNT', 'MNT'), ('CDF', 'CDF'), ('ISK', 'ISK'), ('HKD', 'HKD'), ('BEL', 'BEL'), ('LTT', 'LTT'), ('HRK', 'HRK'), ('CYP', 'CYP'), ('DEM', 'DEM'), ('UZS', 'UZS'), ('GQE', 'GQE'), ('TZS', 'TZS'), ('XAU', 'XAU'), ('TWD', 'TWD'), ('XFO', 'XFO'), ('XBD', 'XBD'), ('AOK', 'AOK'), ('CSK', 'CSK'), ('TJS', 'TJS'), ('ANG', 'ANG'), ('MRO', 'MRO'), ('CNH', 'CNH'), ('SBD', 'SBD'), ('ZMW', 'ZMW'), ('USS', 'USS'), ('DJF', 'DJF'), ('MDC', 'MDC'), ('BND', 'BND'), ('COU', 'COU'), ('BEF', 'BEF'), ('NAD', 'NAD'), ('ETB', 'ETB'), ('ARM', 'ARM'), ('GWE', 'GWE'), ('BWP', 'BWP'), ('VNN', 'VNN'), ('LYD', 'LYD'), ('BGM', 'BGM'), ('NLG', 'NLG'), ('ZWL', 'ZWL'), ('UGX', 'UGX'), ('AFA', 'AFA'), ('GYD', 'GYD'), ('SAR', 'SAR'), ('ESB', 'ESB'), ('SEK', 'SEK'), ('LKR', 'LKR'), ('XUA', 'XUA'), ('BRE', 'BRE'), ('XBB', 'XBB'), ('BYR', 'BYR'), ('AZM', 'AZM'), ('XBA', 'XBA'), ('DOP', 'DOP'), ('XPF', 'XPF'), ('PGK', 'PGK'), ('MVP', 'MVP'), ('BRR', 'BRR'), ('PAB', 'PAB'), ('PEI', 'PEI'), ('SCR', 'SCR'), ('LSL', 'LSL'), ('MLF', 'MLF'), ('BMD', 'BMD'), ('LAK', 'LAK'), ('UYP', 'UYP'), ('HRD', 'HRD'), ('CRC', 'CRC'), ('SKK', 'SKK'), ('BOB', 'BOB'), ('KMF', 'KMF'), ('DZD', 'DZD'), ('MTP', 'MTP'), ('SYP', 'SYP'), ('TJR', 'TJR'), ('XBC', 'XBC'), ('ILS', 'ILS'), ('GNS', 'GNS'), ('IRR', 'IRR'), ('FJD', 'FJD'), ('IQD', 'IQD'), ('ARS', 'ARS'), ('AMD', 'AMD'), ('UYI', 'UYI'), ('CAD', 'CAD'), ('ARA', 'ARA'), ('MAD', 'MAD'), ('UAH', 'UAH'), ('DDM', 'DDM'), ('PHP', 'PHP'), ('YUD', 'YUD'), ('GIP', 'GIP'), ('MVR', 'MVR'), ('XPD', 'XPD'), ('GEK', 'GEK'), ('VES', 'VES'), ('BSD', 'BSD'), ('CHF', 'CHF'), ('GHC', 'GHC'), ('KZT', 'KZT'), ('PLZ', 'PLZ'), ('ALL', 'ALL'), ('RON', 'RON'), ('UYU', 'UYU'), ('JMD', 'JMD'), ('CZK', 'CZK'), ('BOP', 'BOP'), ('MXN', 'MXN'), ('VND', 'VND'), ('MKD', 'MKD'), ('XDR', 'XDR'), ('RUR', 'RUR'), ('ZAR', 'ZAR'), ('BTN', 'BTN'), ('LRD', 'LRD'), ('MTL', 'MTL'), ('GWP', 'GWP'), ('BOL', 'BOL'), ('LUF', 'LUF'), ('XSU', 'XSU'), ('STD', 'STD'), ('BYN', 'BYN'), ('ITL', 'ITL'), ('MUR', 'MUR'), ('PEN', 'PEN'), ('NIO', 'NIO'), ('YUR', 'YUR'), ('ZAL', 'ZAL'), ('BRB', 'BRB'), ('AON', 'AON'), ('QAR', 'QAR'), ('NOK', 'NOK'), ('RSD', 'RSD'), ('CVE', 'CVE'), ('AWG', 'AWG'), ('YUM', 'YUM'), ('TPE', 'TPE'), ('VUV', 'VUV'), ('GTQ', 'GTQ'), ('ZRZ', 'ZRZ'), ('ZWR', 'ZWR'), ('BZD', 'BZD'), ('INR', 'INR'), ('ILP', 'ILP'), ('KPW', 'KPW'), ('VEF', 'VEF'), ('STN', 'STN'), ('TMT', 'TMT'), ('SRD', 'SRD'), ('UGS', 'UGS'), ('SIT', 'SIT'), ('RWF', 'RWF'), ('MZN', 'MZN'), ('IEP', 'IEP'), ('XOF', 'XOF'), ('LTL', 'LTL'), ('ADP', 'ADP'), ('AUD', 'AUD'), ('MGF', 'MGF'), ('SGD', 'SGD'), ('BOV', 'BOV'), ('CLP', 'CLP'), ('CHW', 'CHW'), ('GBP', 'GBP'), ('ZMK', 'ZMK'), ('XPT', 'XPT'), ('MRU', 'MRU'), ('GNF', 'GNF'), ('AZN', 'AZN'), ('BAM', 'BAM'), ('FIM', 'FIM'), ('BDT', 'BDT'), ('GEL', 'GEL'), ('SLL', 'SLL'), ('KRW', 'KRW'), ('BBD', 'BBD'), ('GRD', 'GRD'), ('AFN', 'AFN'), ('BGL', 'BGL'), ('THB', 'THB'), ('FKP', 'FKP'), ('XCD', 'XCD'), ('BHD', 'BHD'), ('BAD', 'BAD'), ('BGO', 'BGO'), ('MWK', 'MWK'), ('ESA', 'ESA'), ('IDR', 'IDR'), ('YDD', 'YDD'), ('XTS', 'XTS'), ('AOR', 'AOR'), ('GHS', 'GHS'), ('USD', 'USD'), ('MKN', 'MKN'), ('HNL', 'HNL')], default='USD', max_length=3),
        ),
    ]