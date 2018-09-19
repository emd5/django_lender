# Generated by Django 2.1.1 on 2018-09-19 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=48)),
                ('author', models.CharField(max_length=48)),
                ('year', models.CharField(choices=[('1900', '1900'), ('1901', '1901'), ('1902', '1902'), ('1903', '1903'), ('1904', '1904'), ('1905', '1905'), ('1906', '1906'), ('1907', '1907'), ('1908', '1908'), ('1909', '1909'), ('1910', '1910'), ('1911', '1911'), ('1912', '1912'), ('1913', '1913'), ('1914', '1914'), ('1915', '1915'), ('1916', '1916'), ('1917', '1917'), ('1918', '1918'), ('1919', '1919'), ('1920', '1920'), ('1921', '1921'), ('1922', '1922'), ('1923', '1923'), ('1924', '1924'), ('1925', '1925'), ('1926', '1926'), ('1927', '1927'), ('1928', '1928'), ('1929', '1929'), ('1930', '1930'), ('1931', '1931'), ('1932', '1932'), ('1933', '1933'), ('1934', '1934'), ('1935', '1935'), ('1936', '1936'), ('1937', '1937'), ('1938', '1938'), ('1939', '1939'), ('1940', '1940'), ('1941', '1941'), ('1942', '1942'), ('1943', '1943'), ('1944', '1944'), ('1945', '1945'), ('1946', '1946'), ('1947', '1947'), ('1948', '1948'), ('1949', '1949'), ('1950', '1950'), ('1951', '1951'), ('1952', '1952'), ('1953', '1953'), ('1954', '1954'), ('1955', '1955'), ('1956', '1956'), ('1957', '1957'), ('1958', '1958'), ('1959', '1959'), ('1960', '1960'), ('1961', '1961'), ('1962', '1962'), ('1963', '1963'), ('1964', '1964'), ('1965', '1965'), ('1966', '1966'), ('1967', '1967'), ('1968', '1968'), ('1969', '1969'), ('1970', '1970'), ('1971', '1971'), ('1972', '1972'), ('1973', '1973'), ('1974', '1974'), ('1975', '1975'), ('1976', '1976'), ('1977', '1977'), ('1978', '1978'), ('1979', '1979'), ('1980', '1980'), ('1981', '1981'), ('1982', '1982'), ('1983', '1983'), ('1984', '1984'), ('1985', '1985'), ('1986', '1986'), ('1987', '1987'), ('1988', '1988'), ('1989', '1989'), ('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017')], max_length=4)),
                ('status', models.CharField(choices=[('available', 'Available'), ('checked-out', 'Checked out')], default='Available', max_length=48)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_borrowed', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
