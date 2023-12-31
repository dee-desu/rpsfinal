# Generated by Django 4.2.5 on 2023-09-23 21:49

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.IntegerField(choices=[(1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040), (2041, 2041), (2042, 2042), (2043, 2043), (2044, 2044), (2045, 2045), (2046, 2046), (2047, 2047), (2048, 2048), (2049, 2049), (2050, 2050), (2051, 2051), (2052, 2052), (2053, 2053), (2054, 2054), (2055, 2055), (2056, 2056), (2057, 2057), (2058, 2058), (2059, 2059), (2060, 2060), (2061, 2061), (2062, 2062), (2063, 2063), (2064, 2064), (2065, 2065), (2066, 2066), (2067, 2067), (2068, 2068), (2069, 2069), (2070, 2070), (2071, 2071), (2072, 2072), (2073, 2073), (2074, 2074), (2075, 2075), (2076, 2076), (2077, 2077), (2078, 2078), (2079, 2079), (2080, 2080), (2081, 2081), (2082, 2082), (2083, 2083), (2084, 2084), (2085, 2085), (2086, 2086), (2087, 2087), (2088, 2088), (2089, 2089), (2090, 2090), (2091, 2091), (2092, 2092), (2093, 2093), (2094, 2094), (2095, 2095), (2096, 2096), (2097, 2097), (2098, 2098), (2099, 2099), (2100, 2100), (2101, 2101), (2102, 2102), (2103, 2103), (2104, 2104), (2105, 2105), (2106, 2106), (2107, 2107), (2108, 2108), (2109, 2109), (2110, 2110), (2111, 2111), (2112, 2112), (2113, 2113), (2114, 2114), (2115, 2115), (2116, 2116), (2117, 2117), (2118, 2118), (2119, 2119), (2120, 2120), (2121, 2121), (2122, 2122), (2123, 2123), (2124, 2124), (2125, 2125), (2126, 2126), (2127, 2127), (2128, 2128), (2129, 2129), (2130, 2130), (2131, 2131), (2132, 2132), (2133, 2133), (2134, 2134), (2135, 2135), (2136, 2136), (2137, 2137), (2138, 2138), (2139, 2139), (2140, 2140), (2141, 2141), (2142, 2142), (2143, 2143), (2144, 2144), (2145, 2145), (2146, 2146), (2147, 2147), (2148, 2148), (2149, 2149), (2150, 2150), (2151, 2151), (2152, 2152), (2153, 2153), (2154, 2154), (2155, 2155), (2156, 2156), (2157, 2157), (2158, 2158), (2159, 2159), (2160, 2160), (2161, 2161), (2162, 2162), (2163, 2163), (2164, 2164), (2165, 2165), (2166, 2166), (2167, 2167), (2168, 2168), (2169, 2169), (2170, 2170), (2171, 2171), (2172, 2172), (2173, 2173), (2174, 2174), (2175, 2175), (2176, 2176), (2177, 2177), (2178, 2178), (2179, 2179), (2180, 2180), (2181, 2181), (2182, 2182), (2183, 2183), (2184, 2184), (2185, 2185), (2186, 2186), (2187, 2187), (2188, 2188), (2189, 2189), (2190, 2190), (2191, 2191), (2192, 2192), (2193, 2193), (2194, 2194), (2195, 2195), (2196, 2196), (2197, 2197), (2198, 2198), (2199, 2199), (2200, 2200)])),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='project_thumbnails/')),
                ('locations', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_images/')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='portfolio.project')),
            ],
        ),
    ]
