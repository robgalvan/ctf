'''
v7 = strlen(s1);
v8 = 14231234143212433LL;
for ( i = 0; i < v7; ++i )
{
v3 = v8 % 10;
v8 /= 10LL;
s1[i] -= v3;
}
if ( !strcmp(s1, "theresanotherstep") )
'''

v8 = 14231234143212433
a =  "theresanotherstep"
sol = ''
for i in range(len(a)):
	v3 = v8 %10
	v8 = v8/10
	sol += chr(ord(a[i]) + v3)
print sol